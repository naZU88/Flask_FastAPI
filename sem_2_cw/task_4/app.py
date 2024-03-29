# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        result = len(request.form.get('text').split())
        return f'Результат - {result}'
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
