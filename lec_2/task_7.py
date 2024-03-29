#Функция abort
import logging
from flask import Flask, render_template, request, abort

app = Flask(__name__)
logger = logging.getLogger(__name__)

def get_blog(id):
    return None


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

#В этом примере мы используем функцию abort() внутри get_blog_by_id для вызова
#ошибки 404 в случае отсутствия статьи в базе данных.    

@app.route('/blog/<int:id>')
def get_blog_by_id(id):
# делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)
    
# возвращаем найденную в БД статью
@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
'title': 'Страница не найдена',
'url': request.base_url,
}
    return render_template('404.html', **context), 404

if __name__ == '__main__':
    app.run()

@app.errorhandler(500)
def page_not_found(e):
    logger.error(e)
    context = {
'title': 'Ошибка сервера',
'url': request.base_url,
}
    return render_template('500.html', **context), 500

# Некоторые коды ошибок
# ● 400: Неверный запрос
# ● 401: Не авторизован
# ● 403: Доступ запрещен
# ● 404: Страница не найдена
# ● 500: Внутренняя ошибка сервера