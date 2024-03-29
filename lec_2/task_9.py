#Flash сообщения
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


#функция flash(). Она принимает
# сообщение и категорию, к которой это сообщение относится, и сохраняет его во
# временном хранилище

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
    # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')

# Категории сообщений в flash позволяют различать типы сообщений и выводить их
# по-разному. Категория по умолчанию message. Но вторым аргументом можно
# передавать и другие категории, например warning, success и другие

if __name__ == '__main__':
    app.run()