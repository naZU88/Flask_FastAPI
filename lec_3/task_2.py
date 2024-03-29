'''Защита CRSF атак'''

# Защита от CSRF-атак в Flask-WTF осуществляется с помощью генерации токена,
# который добавляется к каждой форме. При отправке формы этот токен проверяется
# на сервере, чтобы убедиться, что запрос был отправлен с того же сайта.

from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

# Если вы хотите отключить защиту от CSRF-атак для определенной формы, вы
# можете использовать декоратор csrf.exempt
           
@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    pass