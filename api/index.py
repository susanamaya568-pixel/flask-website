from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return {
        "message": "About Page"
    }


# Vercel이 app 객체를 인식
app = app
