#coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá mundo cruel!!!"

@app.route("/resposta")
def resposta():
    return "Sim, tudo bem"


if __name__ == '__main__':
    app.run(debug=True,port=8000)
