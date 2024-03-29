#Обработка ошибок
from flask import Flask, request, render_template
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

#Обработка ошибок в Flask происходит с помощью декоратора errorhandler(). Этот
# декоратор позволяет определить функцию-обработчик ошибок, которая будет
# вызываться в случае возникновения ошибки в приложении

@app.errorhandler(404) #декоратор реагирует на ошибку 404
def page_not_found(e): #функция принимает текст ошибки
    logger.warning(e)
    context = {
'title': 'Страница не найдена',
'url': request.base_url,
}
    return render_template('404.html', **context), 404

if __name__ == '__main__':
    app.run()
