try:
		if request.method == 'POST':
			flash("try-if(POST)")
			f = request.files['file']
			if (f):
				flash('try-if(POST)-if(file)')
				f.save('/static/uploads/' + secure_filename(f.filename))
		else:
			flash("try-else")
	except Exception as e:
		flash ("except")
		flash(e)