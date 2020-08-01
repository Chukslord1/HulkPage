from flask import *
app = Flask(__name__)

application=app


@app.route("/")
def index():
    return render_template("index2.html")


if __name__ == "__main__":
    app.run(debug=True)
