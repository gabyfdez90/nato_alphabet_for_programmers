from flask import Flask, render_template, jsonify
from http import HTTPStatus
from flask_cors import CORS
from app.nato_translator import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/<string:word>")
def get_translation(word):
    code_words_list = translate_word(word)
    return jsonify(
        {
        "status":"OK",
        "words_list":code_words_list,
        "origin_word": word
        }
    ), HTTPStatus.OK