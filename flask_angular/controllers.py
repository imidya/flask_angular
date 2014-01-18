from flask import render_template
from flask_angular import app


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<resource>')
@app.route('/<resource>/<id>')
def angular(resource, id):
	return render_template('index.html')