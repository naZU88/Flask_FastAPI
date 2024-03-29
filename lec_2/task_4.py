#Обработка POST запросов

from flask import Flask, request, render_template

app = Flask(__name__)


# POST запросы используются для отправки данных на сервер. Они отличаются от GET
# запросов тем, что данные, передаваемые в POST запросах, не видны в URL
# Также POST запросы могут содержать большее количество данных, чем GET

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('post_form.html')

#POST GET запросы можно оформить другим образом, отдельными функциями
@app.get('/submit')
def submit_get():
    return render_template('form.html')

@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run()