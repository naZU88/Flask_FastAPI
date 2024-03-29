# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/task_5', methods=['GET', 'POST'])
def task_5():
    if request.method == 'POST':
        res = 0
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        operation = request.form.get('operation')
        if operation == 'plus':
            res = num1 + num2
        elif operation == 'minus':
            res = num1 - num2
        elif operation == 'mult':
            res = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return 'На ноль делить нельзя!'
            res = num1 / num2
        return str(res)

    return render_template('task_5.html')


if __name__ == '__main__':
    app.run(debug=True)
