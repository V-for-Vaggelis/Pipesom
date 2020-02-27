# app.py
from flask import Flask, render_template           # import flask
app = Flask(__name__)             # create an app instance



@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
