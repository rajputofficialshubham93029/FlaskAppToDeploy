from flask import Flask , render_template
app = Flask(___name__)

@app.route("/")
def hello():
    return render_template("hello.html")