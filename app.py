from flask import Flask, render_template, request, redirect, url_for
import os

from functions.function_app import file_name
from databases.requests import add_cloth,get_cloths,get_cloth_by_id


app = Flask(__name__)

@app.route("/admin")
def home():
    return render_template('admin.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload_files():
    data = {
        'img_paths': [],
        'name':request.form['name'],
        'description':request.form['description'],
        'price':request.form['price'],
        'count':request.form['count'],
    } 

    for file in request.files.getlist('archivos'):
        name_file = f'{file_name()}.jpg'
        data['img_paths'].append(f'static/img/{name_file}')
        file.save(os.path.join('static/img', name_file))
    add_cloth(data)
    print(data)
    return ''



if __name__ == '__main__':
    app.run(debug=True, port=7000)


