from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    text = ""
    for i in range(1,667):
        text += f"<p>{i}</p>"
    return text