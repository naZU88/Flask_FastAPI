# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

from pathlib import PurePath
from click import Path
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/image/', methods=['POST', 'GET'])
def image():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads',
        file_name))
        return f"Изображение {file_name} загружено на сервер"
    return render_template('image_form.html')
    
if __name__ == '__main__':
    app.run(debug=True)
