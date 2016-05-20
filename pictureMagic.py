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
@app.route('/', methods=['GET', 'POST'])
def homepage():
	try:
		if request.method == 'POST':
			flash("POST")
			pdb.set_trace()
			f = request.files['file']
			if (f):
				flash('(POST)-file exists (should be uploaded now)')
				f.save('/static/uploads/' + secure_filename(f.filename))
		else:
			flash("GET")
			
	except Exception as e:
		flash ("except")
		flash(e)
	
	pdb.set_trace()	
	flash("rendering template...")
	return render_template('index.html')

# Bei Ausfuehrung dieses Skripts: Server starten:
if __name__ == '__main__':
    # lokal (zum Testen):
	app.run()
	# im Netzwerk: (DEBUG auf False setzen!)
	#app.run(host='0.0.0.0')