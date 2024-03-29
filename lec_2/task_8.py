#Перенаправления
from flask import Flask, redirect, url_for

# Для перенаправления в Flask используется функция redirect(). Она принимает
# URL-адрес, на который нужно перенаправить пользователя, и возвращает объект
# ответа, который перенаправляет пользователя на указанный адрес

app = Flask(__name__)

@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
