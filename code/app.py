from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os, webbrowser
from requests import get
from gtts import gTTS
from playsound import playsound

if os.environ.get('DOCKER', '') == "yes":
    UPLOAD_FOLDER = '/usr/src/resultados/images'
    UPLOAD_FOLDER_AUDIO = '/usr/src/resultados/audio'
    url2 = "http://192.168.99.102:5050/getimagen" #ip de docker
    url3 = "http://192.168.99.102:5050//jsontexto"
else:
    UPLOAD_FOLDER = '..\\resultados\\images'
    UPLOAD_FOLDER_AUDIO = '..\\resultados\\audio'
    url2 = "http://localhost:5050/getimagen"
    url3 = "http://localhost:5050/jsontexto"
#url2 = "http://192.168.99.102:5050/getimagen" #ip de docker
#url3 = "http://192.168.99.102:5050//jsontexto"

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS  #Partimos la cadena 1 vez y devuelve una lista con 2 valores

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_AUDIO'] = UPLOAD_FOLDER_AUDIO

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/uploader', methods = ['POST', ])
def upload_file():
    if request.method == 'POST' and request.files:
        f = request.files['image']
        
        #respuesta = requests.post('http://localhost:5050/imagen', filename=filename)
        #texto = respuesta.json() Intentaba hacerlo asi, pero no me salio
        
        if f and allowed_file(f.filename.lower()):
            filename = secure_filename(f.filename)
            numero = 1
            #ext = filename.rsplit ('.', 1) [1]
            filename = str(numero) + '.' + "png"   #filename = str(numero) + '.' + str(ext) Asi mantenemos la extension, pero quiero cambiarla
            """while (os.path.isfile(filename)):   #No lo voy a usar por que cada imagen que cree luego la borro
                numero += 1 
                filename = numero + '.' + ext"""
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('results.html', text=("Imagen Subida Correctamente","Nombre: " +  filename,"Destino: " + UPLOAD_FOLDER)) , webbrowser.open_new(url2)
    return render_template('home.html')

@app.route('/recibirjson')
def pasaratexto():
    jsontexto = get(url3).json()
    return render_template('results.html', jsontexto=jsontexto)

@app.route('/convertiraudio')
def convertiraudio():
    jsontexto2 = get(url3).json()
    myobj = gTTS(text=jsontexto2, slow=False)
    myobj.save(app.config['UPLOAD_FOLDER_AUDIO'] + '/audio.mp3')
    playsound('C://Users//zuric//Documents//EntornosPython//Docker2//resultados//audio//audio.mp3')
    return render_template("results.html", myobj=myobj, jsontexto2=jsontexto2, text=("Destino: " + UPLOAD_FOLDER_AUDIO))
"""
@app.route('/recibirprueba', methods = ['POST', ])
def recibirprueba():
    if request.method == 'POST' and request.files:
        url4 = 'http://localhost:5050/uploadfile'
        filename = get(url4).json()
        #jsontexto = get('http://localhost:5050/uploadfile/').json()

        return render_template('results.html', filename=filename)"""
        
if __name__ == '__main__':
    app.run(debug = True)
