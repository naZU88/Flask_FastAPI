#Обработка GET запросов

from flask import Flask  
from markupsafe import request

app = Flask(__name__)


#request — глобальный объект Flask, который даёт доступ к локальной информации для каждого контекста запроса
#Дополнительные параметры собираются в словаре args объекта request. И раз
#перед нами словарь, можно получить значение обратившись к ключу через метод
#get()

@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень
        {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'



if __name__ == '__main__':
    app.run()