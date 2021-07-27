from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="/templates")

@app.route("/")
def index():
    return render_template("index.html")
    