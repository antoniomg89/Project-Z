from flask import Flask, render_template, url_for, request, redirect, jsonify
#from pymongo import MongoClient
import os
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

app.secret_key = os.urandom(24)

#MONGO_URL = os.environ.get('MONGO_URL')
#if not MONGO_URL:
#client = MongoClient('localhost', 27017)

#else:
#    client = MongoCLient(MONGO_URL)

#db = client.test_database
#qrdb = db.qrdb

from src.qrclass import servQR
gen = False
tamqr = None
bordeqr = None
informacionqr = None
qr = servQR()

@app.route('/',)
def statusQR():
    return jsonify(status='OK')

@app.route('/status',)
def statusQR():
    return jsonify(status='OK')

@app.route('/genQR')
def genQR():
    #os.remove("./static/images/img1.png")
    if getgen() == False:
        informacionqr = "TestQR"
        qr.generarQR(informacionqr, 10, 5)
        image_qr = qr.getImageQR()
        image_qr.save('./static/images/img.png')
        return render_template('QRGen.html', filename='./static/images/img.png')

    return render_template('QRGen.html', filename='./static/images/img1.png')

@app.route('/registroQR', methods=['GET','POST'])
def regQR():
    if request.method == 'POST':
        tamqr = request.form['tamaño']
        bordeqr = request.form['borde']
        informacionqr = request.form['informacion']
        defQR(tamqr,bordeqr,informacionqr)

        return redirect(url_for('showQR'))

@app.route('/mostrarQR')
def showQR():
        return render_template('QRGen.html', filename='./static/images/img1.png')


def defQR(t,b,i):
    tamqr = t
    bordeqr = b
    informacionqr = i
    qr.generarQR(informacionqr, tamqr, bordeqr)
    image_qr = qr.getImageQR()
    image_qr.save('./static/images/img1.png')

    #if qrdb.find_one({"info": informacionqr,"tam": tamqr, "brd": bordeqr}) is None:
    #    post = {"info": informacionqr, "tam": tamqr, "brd": bordeqr}
    #    qrdb.insert_one(post)

    gen = True

def getgen():
    return gen

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
