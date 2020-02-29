# app.py
import os
import urllib.request
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename          # import flask
from corr_matrix import corr_mat
from som_analysis import analyze_som
from data_reader import read_data


UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static') #directory where uploaded files go to
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

			# delete all previous entries
			for file_name in os.listdir('static/'):
				if file_name.endswith('.csv'):
					os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file_name))

			# save the file
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')

			# delete all previous produced images
			for file_name in os.listdir('static/'):
				if file_name.endswith('.png'):
					os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file_name))

			# get correlation matrix
			headers, clear_X, _ = read_data("{}/{}".format(UPLOAD_FOLDER, filename), False, False)
			corr_mat(headers, clear_X)

			# do som analysis
			headers, clear_X, droped = read_data("{}/{}".format(UPLOAD_FOLDER, filename), True, True)
			analyze_som(headers, clear_X)

			files = os.listdir('static/')

			# return redirect('/')
			return render_template("results.html", files=files) #render results and return a listo of all static files
		else:
			flash('Allowed file type is csv')
			return redirect(request.url)



if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
