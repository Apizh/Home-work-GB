from flask import Flask, render_template, request
from flask_wtf import FlaskForm, CSRFProtect
from forms_01 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ee6b0ec4b7576b4b605dad0692aab110e3ed54db9b6489c8e859c88034ccce60'

csrf = CSRFProtect(app)
"""
Генерация надежного секретного ключа
Для получения автоматической генерации,
вместо 'mysecret_key', можно использовать следующий модуль:
>>> __import__('secrets').token_hex()
"""
@app.route('/')
def start_page():
    return 'Hello world'

@app.route('/data/')
def data_page():
    return 'Your data!'


@app.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)


# @app.route('/form', methods=['POST', 'GET'])
# @csrf.exempt
# def my_form():
#     '''Для отправки незащищенной формы без защиты от Cross-Site Request Forgery'''
#     ...
#     return 'No CSRF token protection'



if __name__ == '__main__':
    app.run(debug=True)