from flask import Flask, render_template, request, redirect, url_for, jsonify,send_from_directory, abort
from werkzeug.utils import secure_filename
from PIL import Image
import os
import base64
import webbrowser
from requests import get
#import pytesseract
#C:\Program Files\Tesseract-OCR
#tessdata_dir_config = '--tessdata-dir"C:\\Program Files\\Tesseract-OCR\\tessdata"'
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#from gtts import gTTS
#from playsound import playsound

if os.environ.get('DOCKER', '') == "yes":
    UPLOAD_FOLDER = 'C:\\Users\\zuric\\Documents\\EntornosPython\\Docker2\\resultados\\images'
else:
    UPLOAD_FOLDER = '..\\resultados\\images'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS  #Partimos la cadena 1 vez y devuelve una lista con 2 valores

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")

def home():
    return render_template('home.html')

@app.route('/uploader', methods = ['POST', ])
def upload_file():
    if request.method == 'POST' and request.files:
        f = request.files['image']
        if f and allowed_file(f.filename.lower()):
            filename = secure_filename(f.filename)
            numero = 1
            ext = filename.rsplit ('.', 1) [1]
            filename = str(numero) + '.' + "png"   #filename = str(numero) + '.' + str(ext) Asi mantenemos la extension, pero quiero cambiarla
            """while (os.path.isfile(filename)):   #No lo voy a usar por que cada imagen que cree luego la borro
                numero += 1 
                filename = numero + '.' + ext"""
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return render_template('home.html')
            #return redirect(url_for("localhost:5050/imagen", filename=filename))
            return render_template('results.html', text=("Imagen Subida Correctamente", filename, UPLOAD_FOLDER)) , webbrowser.open_new("http:localhost:5050/imagen")
        return "Archivo no permitido"
        
        """img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        text = pytesseract.image_to_string(img)
        try:
            text = pytesseract.image_to_string(img)#, config=tessdata_dir_config)
        except Exception as e:
            return render_template('results.html', text=NO_VALID_IMAGE)

        if not os.environ.get('DOCKER', '') == "yes":
            myobj = gTTS(text=text, slow=False)
            myobj.save(app.config['UPLOAD_FOLDER'] + "/speech.mp3")
            playsound(app.config['UPLOAD_FOLDER'] + "/speech.mp3") """        
    return render_template('home.html')


@app.route("/download/<filename>", methods=['GET'])
#@app.route("http://localhost:5000/download/<filename>/download/*.*", methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('..\\resultados\\images', filename)):
            return send_from_directory('..\\resultados\\images\\filename', filename, as_attachment=True)
        
if __name__ == '__main__':
    app.run(debug = True)
