from flask import Flask

app = Flask(__name__)


@app.route("/")
def helloworld():
    return "hello pycharm first basic "


if __name__ == "__main__":
    app.run()
