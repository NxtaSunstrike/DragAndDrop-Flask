from flask import Flask, render_template, request, redirect, url_for
from random import sample
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


def file_name():
    symbols = "0123456789abcdefghijklmnopqrstuvwxyz_".upper()
    result_string = sample(symbols, 20)
    return "".join(result_string)


@app.route('/upload', methods=['POST', 'GET'])
def upload_files():
    for file in request.files.getlist('archivos'):
        file.save(os.path.join('static/img', file_name() + ".jpg"))     
    return ''


if __name__ == '__main__':
    app.run(debug=True, port=7000)


