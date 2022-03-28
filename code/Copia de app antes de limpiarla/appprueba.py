from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import os
#import pytesseract
#C:\Program Files\Tesseract-OCR
#tessdata_dir_config = '--tessdata-dir"C:\\Program Files\\Tesseract-OCR\\tessdata"'
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from gtts import gTTS
from playsound import playsound

if os.environ.get('DOCKER', '') == "yes":
    UPLOAD_FOLDER = 'C:\\Users\\zuric\\Documents\\EntornosPython\\Docker2\\resultados\\images'
else:
    UPLOAD_FOLDER = 'C:\\Users\\zuric\\Documents\\EntornosPython\\Docker2\\resultados\\images'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")

def home():
    return render_template('home.html')

@app.route('/uploader', methods = ['POST', ])
def upload_file():
    NO_VALID_IMAGE = "No se ha proporcionado una imagen valida."
    if request.method == 'POST' and request.files:
        f = request.files['image']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
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

        return render_template('results.html', text=("Imagen Subida Correctamente", UPLOAD_FOLDER))

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)

"""

"""