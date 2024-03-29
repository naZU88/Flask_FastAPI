'''Работаем с шаблонизатором Jinjer для создания динамики'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

'''
@app.route("/index/")
def html_index():
    return render_template('index.html', name='Харитон')  # чтобы работать с полноценными HTML файлами нужно использовать функцию render_template. Функция принимает 
#бесконечно много именованных переменных. Важно - шаблоны она ищет в папке templates
'''

@app.route('/index/')
def index():
    context = {
    'title': 'Личный блог',
    'name': 'Харитон',
    }
    return render_template('index.html', **context) #чтобы не передавать в одну строку переменные, лучше их хранить словаре и распаковывать через **

if __name__ == "__main__":
    app.run()
