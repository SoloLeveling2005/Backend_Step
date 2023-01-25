from flask import Flask, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Solo2005@localhost:5432/microservices'
db = SQLAlchemy(app)


class Users(db.Model):
    with app.app_context():
        __tablename__ = 'authentication_users'
        db.Model.metadata.reflect(db.engine)


@app.route('/auth/<username>/<password>', methods=['GET'])
def get_users(username, password):
    with app.app_context():
        user = Users.query.filter_by(username=username, password=password).first()
        if user is not None:
            return jsonify({'status': 'success', 'user_id': user.id})
        else:
            return jsonify({'status': 'failure'})

@app.route('/reg/<username>/<password>', methods=['POST'])
def create_user(username,password):
    with app.app_context():
        user = Users.query.filter_by(username=username, password=password).first()
        if user is not None:
            print(user)
            return jsonify({'status': 'failure'})
        else:
            new_user = Users(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            user = Users.query.filter_by(username=username, password=password).first()
            return jsonify({'status': 'success', 'user_id': user.id})


if __name__ == '__main__':
    app.run()
