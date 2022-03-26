from werkzeug.utils import secure_filename
from PIL import Image, ImageFilter
import os
import pytesseract
import json
import base64
from requests import get

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import StreamingResponse
from io import BytesIO

if os.environ.get('DOCKER', '') == "yes":
    DOWNLOAD_FOLDER = 'C:\\Users\\zuric\\Documents\\EntornosPython\\Docker2\\resultados\\images'
    UPLOAD_FOLDER = 'C:\\Users\\zuric\\Documents\\EntornosPython\\Docker2\\resultados\\texto'
else:
    DOWNLOAD_FOLDER = '..\\resultados\\images'
    UPLOAD_FOLDER = '..\\resultados\\images'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = FastAPI()

#@app.route("http://localhost:5000/download/<filename>/download/*.*", methods=['GET'])
"""
@app.get("/") #'http://localhost:5050/download/2.PNG
def main():
    def iterfile():  
        with open('..\\resultados\\images\\2.PNG', mode="rb") as file_like:  
            yield from file_like  
    return StreamingResponse(iterfile(), media_type="image/jpeg")

@app.post("/")
def image_filter(img: UploadFile = File(...)):
    original_image = Image.open(img.file)
    original_image = original_image.filter(ImageFilter.BLUR)

    filtered_image = BytesIO()
    original_image.save(filtered_image, "JPEG")
    filtered_image.seek(0)

    return StreamingResponse(filtered_image, media_type="image/jpeg")

"""

nombreimagen = "1.png"
imgruta = os.path.join(DOWNLOAD_FOLDER, nombreimagen)

# Jinja2 template instance for returning webpage via template engine
templates = Jinja2Templates(directory="templates")
@app.get('/getimagen', response_class=HTMLResponse)
async def getimagen(request: Request):
    img = Image.open(os.path.join(imgruta))
    text = pytesseract.image_to_string(img)
    result = json.dumps(text)
    return templates.TemplateResponse("imagen.html", {"request": request, "img": img, "text": text, "result": result})




@app.get("/jsontexto")
async def jsontexto():
    #Este seria el json del texto extraido de la imagen:
    #Convertimos imagen a Texto
    img = Image.open(os.path.join(imgruta))
    text = pytesseract.image_to_string(img)
    result = json.dumps(text)
    result2 = json.loads(result)
    return {'json': result}, {'texto': result2}

@app.get('/imagen') # Asi mostramos la imagen leida
async def imagen():
    if os.path.exists(imgruta):
        img = Image.open(os.path.join(imgruta))
        text = pytesseract.image_to_string(img)
        result = json.dumps(text)
        return FileResponse(imgruta)
    return {"error": "El archivo no existe"}


"""
@app.get('/imagen/<filenane>')
def imagen(filename):
    if os.path.exists(filename): 
        return FileResponse(filename)

    return {"error": "El archivo no existe"}
"""
"""
@app.get('/imagen')
def imagen():
    imagen = get("http://localhost:5000/download/3.png")
    return imagen
    #return render_template("imagen.html", imagen=imagen)"""



#print(jsontexto())

#print(img)
#print(text)

"""@app.post("/jsonimage")
def jsonimage():
    #Este seria el json de la imagen:
    data = {}
    with open(imgruta, mode='rb') as file:
        img = file.read()
    data['img'] = base64.b64encode(img)
    result = json.dumps(data)
    return result
print(jsonimage())"""


"""@app.get('/')
def index():
         return {'mensaje': '¡Ha creado el servicio FastApi correctamente! '}"""


"""@app.get('/query/{uid}')
def query(uid):
        msg = f'El uid que consulta es: {uid}'
        return {'success': True, 'msg': msg}"""

"""
@app.get("/") #Escucha en la raiz del proyecto (raiz = @app.get("/"))
def raiz():
    return RedirectResponse(url="/docs/")

@app.get("http://localhost:5050/download/<filename>")
#@app.get("/download/<filename>", methods=['GET'])
def image_endpoint():
    #img = Image.open(os.path.join(app.config['..\\resultados\\images', filename], secure_filename(f.filename)))
    #img.show()
    #text = pytesseract.image_to_string(img)
    return {"mensaje": "Prueba de mensaje"}
"""


"""
@app.get("/download/{filename}" , response_class=FileResponse)
async def image_endpoint(filename):
    #if os.path.isfile(os.path.join('..\\resultados\\images', filename)):
    img = Image.open(os.path.join(app.config['..\\resultados\\images'], secure_filename(filename)))
    text = pytesseract.image_to_string(img)
    print(text)
    data = {}
    with open('..\\resultados\\images\\logo.jpg', mode='rb') as file:
        img = file.read()
    data['img'] = base64.encodebytes(img).decode('utf-8')
#print(json.dumps(data))
    result = json.dumps(data)
    #return FileResponse('..\\resultados\\images')
    #return result
    msg = f'El uid que consulta es: <filename> {filename}'
    return {'success': True, 'msg': msg}
 """ 


"""@app.get("/")
async def main():
    return FileResponse("\\resultados\\images\\logo.jpg'")"""

"""
@app.post(DOWNLOAD_FOLDER)
async def image_endpoint():
    img = Image.open(os.path.join(app.config['DOWNLOAD_FOLDER'], secure_filename(f.filename)))
    text = pytesseract.image_to_string(img)
    try:
        text = pytesseract.image_to_string(img)#, config=tessdata_dir_config)
    except Exception as e:
        return render_template('results.html', text=NO_VALID_IMAGE)
    return Response(content=img, media_type="image/png")"""

"""router = APIRouter()
@app.route('/uploader', methods = ['POST', ])
@router.post("/uploaded")
def upload_file():
    NO_VALID_IMAGE = "No se ha proporcionado una imagen valida."
    img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    text = pytesseract.image_to_string(img)
    try:
        text = pytesseract.image_to_string(img)  # , config=tessdata_dir_config)
    except Exception as e:
        return render_template('results.html', text=NO_VALID_IMAGE)
    return "succes"

app.include_router(router)"""

if __name__ == '__main__':
    app.run(debug = True)
    
    #uvicorn.run('myapp:app', host='localhost', port=5050)
