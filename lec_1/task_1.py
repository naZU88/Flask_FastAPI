'''Первые шаги - создаем функцию Hello world'''

from flask import Flask  #импортируем Flask

app = Flask(__name__) #создаем экземпляр класса Flask и передаем ему __name__ чтобы он знал где искать нужные файлы

@app.route('/') #декорируем функцию hello_world, чтобы она запускалась пре переходе по корневому адресу
def hello_world():
    return 'Hello World!' #функция выводит данные по указанному в декораторе адресу


if __name__ == '__main__':
    app.run()
