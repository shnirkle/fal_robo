from flask import Flask


app = Flask(__name__)

CLS = None


@app.route("/")
def index():
    with open("static/index.html") as indexhtml:
        data = indexhtml.read()
    return data


@app.route("/image")
def image():
    image = CLS.f


def run(cls):
    CLS = cls
    try:
        app.run()
    except Exception as e:
        return 1
    return 0

if __name__ == "__main__":
    app.run()