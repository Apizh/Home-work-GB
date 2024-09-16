from flask import Flask
from SQLALchemy.database_tables import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db.init_app(app)


@app.route('/')
def index():
    """Создаем пустую старницу со строкой Hello World"""
    return 'Hello World'


@app.cli.command('init-db')
def init_db():
    """Для создания пустых таблиц и схемы описанной в db в модуле database_tables"""
    db.create_all()
    print('Initializing user Database')


@app.cli.command('add-jhon')
def add_jhon():
    """Добавление нового пользователя в базу данных"""
    john = User(username='Johny', email='johny@example.com')
    db.session.add(john)
    db.session.commit()
    print(f'User has been added in user Database')


@app.cli.command('del-jhon')
def del_jhon():
    """Функция для удаления пользователя из таблицы User базы данных db"""
    user = User.query.filter_by(username='Johny').first()
    db.session.delete(user)
    db.session.commit()
    print(f'{user} has been removed from the user Database')


@app.cli.command('rename-email')
def rename_email():
    """Функция для замены почты User по совпадению"""
    user = User.query.filter_by(email='johny@example.com').first()
    user.email = 'second_johny@example.com'
    db.session.commit()
    print(f'The {user.username} email has been changed in the database.')


@app.cli.command('data-filling-table')
def data_filling_table():
    """Функция для наполнения таблиц User and Post базы данных db"""
    # Наполняем таблицу фиктивными пользователями
    count_users = 5
    for i in range(1, count_users + 1):
        new_user = User(username=f'Jhon_{i}', email=f'Jhon{i}@example.com')
        db.session.add(new_user)
    db.session.commit()

    # Наполняем таблицу фиктивными статьями
    for post in range(1, count_users ** 2):
        author = User.query.filter_by(username=f"Jhon_{post % count_users + 1}").first()
        new_post = Post(title=f"Post title{post}", content=f"Post content {post}", author=author)
        db.session.add(new_post)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
