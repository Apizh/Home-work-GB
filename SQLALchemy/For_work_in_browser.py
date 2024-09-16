from datetime import datetime, timedelta
from flask import Flask, render_template, jsonify
from SQLALchemy.database_tables import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/my_database.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/users/')
def data_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/user/<username>')
def user_by_username(username):
    users = User.query.filter_by(username=username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/post/author/<int:user_id>')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title,
              'content': post.content,
              'created_at': post.created_at
              } for post in posts])
    else:
        return jsonify({'DataBase Error': f'Not posts found for {user_id}'}), 404


@app.route('/post/last-week/')
def get_post_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title,
              'content': post.content,
              'created_at': post.created_at
              } for post in posts])
    else:
        return jsonify({'DataBase Error': 'Not posts found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
