#Генерация URL адресов

from flask import Flask  

app = Flask(__name__)

#фукция url_for - генерирует URL адресс. В больших взрослых проектах - это полезная практика. Функция url_for принимает имя view функции в качестве
#первого аргумента и любое количество ключевых аргументов. Каждый ключ соответствует переменной в URL адресе. Отсутствующие в адресе переменные
#добавляются к адресу в качестве параметров запроса,

@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>'
    text += f'Функция {url_for("test_url", num=42,
    data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=42,
    data="new_data", pi=3.14515) = }<br>'
    return text

#также данная функция используется при генерации пути к статике в шаблонах. Пример:
# Данную строчку <link rel="stylesheet" href="/static/css/bootstrap.min.css">
# Можно заменить следующим образом <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">


if __name__ == '__main__':
    app.run()
