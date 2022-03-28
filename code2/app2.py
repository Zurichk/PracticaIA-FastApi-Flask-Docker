from PIL import Image
import os, pytesseract, json
#FastApi
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if os.environ.get('DOCKER', '') == "yes":
    DOWNLOAD_FOLDER = '/usr/src/resultados/images'
    UPLOAD_FOLDER = '/usr/src/resultados/images'
else:
    DOWNLOAD_FOLDER = '..\\resultados\\images'
    UPLOAD_FOLDER = '..\\resultados\\images'

DOWNLOAD_FOLDER = '..\\resultados\\images'
UPLOAD_FOLDER = '..\\resultados\\images'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = FastAPI()

nombreimagen = "1.png"
imgruta = os.path.join(DOWNLOAD_FOLDER, nombreimagen)

templates = Jinja2Templates(directory="templates")
@app.get("/")
def read_root():
    return {"Probando": "Contenedor Docker"}

@app.get('/getimagen', response_class=HTMLResponse)
async def getimagen(request: Request):
    img = Image.open(os.path.join(imgruta))
    text = pytesseract.image_to_string(img)
    result = json.dumps(text)
    return templates.TemplateResponse("imagen.html", {"request": request, "img": img, "text": text, "result": result})

@app.get("/jsontexto")
async def jsontexto():
    #El json del texto extraido de la imagen:
    #Convertimos imagen a Texto
    img = Image.open(os.path.join(imgruta))
    text = pytesseract.image_to_string(img)
    json_compatible = jsonable_encoder(text)
    return JSONResponse(content=json_compatible)

@app.get('/imagen') # Asi mostramos la imagen leida
async def imagen():
#async def imagen(miimagen): 
    if os.path.exists(imgruta):
        img = Image.open(os.path.join(imgruta))
        text = pytesseract.image_to_string(img)
        return FileResponse(imgruta)
    return {"error": "El archivo no existe"}

"""
@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
"""

if __name__ == '__main__':
    app.run(debug = True)
    
    #uvicorn.run('myapp:app', host='localhost', port=5050)
