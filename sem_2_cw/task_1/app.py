# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        return 'Hi, dear!'
    return render_template('base.html')
    
if __name__ == '__main__':
    app.run(debug=True)
