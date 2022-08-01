import translator
from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/englishToFrench")
def en_to_fr():
    text = request.args.get('textToTranslate')
    return translator.englishToFrench(text=text)

@app.route("/frenchToEnglish")
def fr_to_en():
    text = request.args.get('textToTranslate')
    return translator.frenchToEnglish(text=text)


if __name__ == "__main__":
    app.run()
