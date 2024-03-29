'''Работа с типами данных'''

from flask import Flask  #импортируем Flask

app = Flask(__name__)



@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"' #этот пример нужен чтобы показать, что в случае использования пути как переменной, нужно обозначать тип данных, иначе будет ошибка


@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


if __name__ == "__main__":
    app.run()