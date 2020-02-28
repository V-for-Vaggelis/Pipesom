# app.py
import os
import urllib.request
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename          # import flask

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data_files') #directory where uploaded files go to
ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)             # create an app instance
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# serve the home page
@app.route("/")
def home():
    return render_template("index.html")

# handle file upload
@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'filename' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['filename']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			return redirect('/')
		else:
			flash('Allowed file type is csv')
			return redirect(request.url)



if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
