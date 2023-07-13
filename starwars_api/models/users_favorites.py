from utils.db import db

class User_favorite(db.Model):
    __tablename__ = 'users_favorites'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    people_uid = db.Column(db.Integer, db.ForeignKey('peoples.uid'))

    def __repr__(self):
        return f'<User_favorites {self.id}>'