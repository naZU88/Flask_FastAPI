# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.


from pathlib import PurePath, Path
from venv import logger

from flask import Flask, render_template, request, abort

app = Flask(__name__)
list_users = { 'superBoy': "12345",
              "killer": "45678"}


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        if request.form.get('login') in list_users and list_users[request.form.get('login')] == request.form.get('password'):
            return f"Привет, {request.form.get('login')}"
        else:
            abort(404)
    return render_template('main.html')

@app.errorhandler(404)
def page_error(e):
    logger.warning(e)
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
