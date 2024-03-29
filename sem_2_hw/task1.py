# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, redirect, render_template, request, make_response, url_for

app = Flask(__name__)

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        response = make_response(render_template('hello.html', name=request.form.get('name')))
        name = request.form.get('name')
        email = request.form.get('email')
        response.set_cookie('name', str(name))
        response.set_cookie('email', str(email))
        return response
    return render_template('form.html')



@app.post('/hello')
def hello():
    response = make_response(render_template('form.html'))
    response.set_cookie('name', '', max_age=0)
    response.set_cookie('email', '', max_age=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
