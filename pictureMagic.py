# -*- coding: utf-8 -*-
from flask import Flask, request, url_for, render_template, flash, send_from_directory
from werkzeug import secure_filename
import pdb

# configuration (hier nicht in separater Konfigdatei, weil sehr klein)
DEBUG = True   #in Produktionsphase immer auf False belassen!
SECRET_KEY = 'f66e225e9aae5b642a58aa93848d31c213c49cd264180694'

# application
app = Flask(__name__)
app.config.from_object(__name__) # from_object, weil keine separate Konfigdatei

# view
@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def homepage():
	imgList = {}
	counter = 0
	try:
		if request.method == 'POST':
			flash("POST")
			f = request.files['file']
			if (f):
				filename = secure_filename(f.filename)
				speicherort =  'static/uploads/'+filename
				f.save(speicherort)
				imgList[counter] = filename
				counter += 1
				pdb.set_trace()
				return render_template('index.html', filename=filename, imgList=imgList)
				
		else: #GET
			pdb.set_trace()
			flash("GET")
			return render_template('index.html')

	except Exception as e:
		pdb.set_trace()
		flash(e)
		return render_template('index.html')

# einzelnes Bild anzeigen lassen
@app.route('/<filename>', methods=['GET'])
def files(filename):
	return send_from_directory('static/uploads/', filename)	
	
# Bei Ausfuehrung dieses Skripts: Server starten:
if __name__ == '__main__':
    # lokal (zum Testen):
	app.run()
	# im Netzwerk: (DEBUG auf False setzen!)
	#app.run(host='0.0.0.0')