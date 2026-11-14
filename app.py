import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", proyecto="Mi primera app con flask")


if __name__ == "__main__":
    app.run(debug=True)
