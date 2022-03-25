from werkzeug.utils import secure_filename
from PIL import Image
import os
import pytesseract
import json
import base64

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

if os.environ.get('DOCKER', '') == "yes":
    DOWNLOAD_FOLDER = 'C:\\Users\\zuric\\Documents\\EntornosPython\\Docker2\\resultados\\images'
    UPLOAD_FOLDER = 'C:\\Users\\zuric\\Documents\\EntornosPython\\Docker2\\resultados\\texto'
else:
    DOWNLOAD_FOLDER = '..\\resultados\\images'
    UPLOAD_FOLDER = '..\\resultados\\images'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = FastAPI()

#@app.route("http://localhost:5000/download/<filename>/download/*.*", methods=['GET'])

"""@app.get('/')
def index():
         return {'mensaje': '¡Ha creado el servicio FastApi correctamente! '}"""

"""
@app.get('/query/{uid}')
def query(uid):
        msg = f'El uid que consulta es: {uid}'
        return {'success': True, 'msg': msg}


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
# Jinja2 template instance for returning webpage via template engine
templates = Jinja2Templates(directory="templates")

@app.get('/get-webpage', response_class=HTMLResponse)
async def get_webpage(request: Request):
    return templates.TemplateResponse("results.html", {"request": request, "message": "Contact Us"})

"""
@app.get("/download/")
async def main():
    return FileResponse("Hola")"""

#Convertimos la imagen a Json
"""data = {}
with open('..\\resultados\\images\\logo.jpg', mode='rb') as file:
    img = file.read()
data['img'] = base64.encodebytes(img).decode('utf-8')
#print(json.dumps(data))"""

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
