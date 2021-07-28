from flask import Flask, render_template, request

app = Flask(__name__, template_folder = "templates", static_url_path="/static")

#home page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ranks")
def ranks():
    return render_template("ranks.html")

@app.route("/about")
def about():
    return render_template("about.html")
    
#run app
if __name__ == "__main__":
    app.run(debug=True)