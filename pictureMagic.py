# -*- coding: utf-8 -*-
from flask import Flask, request, url_for, render_template, flash, send_from_directory
from werkzeug import secure_filename

# configuration (hier nicht in separater Konfigdatei, weil sehr klein)
DEBUG = True   #in Produktionsphase immer auf False belassen!
SECRET_KEY = 'f66e225e9aae5b642a58aa93848d31c213c49cd264180694'

# application
app = Flask(__name__)
app.config.from_object(__name__) # from_object, weil keine separate Konfigdatei

# view
@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['GET'])
def homepage():
	return render_template('index.html')

@app.route('/up', methods=['GET', 'POST'])
def up(): # handle file uploads
	try:
		if request.method=='POST':  # this is executed for EVERY picture the user uploads.
			f = request.files['file']
			filename = secure_filename(f.filename) # this replaces " " by "_" and removes any "(" oder ")" in the filename. (and possibly some other stuff I don't know)
			speicherort = 'static/uploads/'+filename
			f.save(speicherort)
	except Exception as e:
		flash(e)

	return render_template('index.html')

# einzelnes Bild anzeigen lassen #fancy zusatz, nicht noetig.
@app.route('/<filename>', methods=['GET'])
def files(filename):
	return send_from_directory('static/uploads/', filename)
	
# Bei Ausfuehrung dieses Skripts: Server starten:
if __name__ == '__main__':
    # lokal (zum Testen):
	app.run()
	# im Netzwerk: (DEBUG auf False setzen!)
	#app.run(host='0.0.0.0')