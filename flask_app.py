from flask import Flask,render_template , request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/poems")
def poems():
    return render_template("Poems.html")

@app.route("/programe")
def programe():
    return render_template("program.html")

@app.route("/edu")
def edu():
    return render_template("edu.html")