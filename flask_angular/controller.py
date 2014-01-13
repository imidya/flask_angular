from flask_angular import app

@app.route('/')
def index():
	return 'index'