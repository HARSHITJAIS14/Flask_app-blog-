from flaskblog import db,login_manager
from flask import current_app
from datetime import  datetime 
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(60),nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    #here backref show the command we will type in post to get the user...
    posts=db.relationship('Post',backref='author',lazy=True)       

    def get_reset_token(self,expires_sec=1800):
        s=Serializer(current_app.config['SECRET_KEY'])
        token=s.dumps({'user_id': self.id})
        return token
    @staticmethod
    def verify_reset_token(token,expires_sec=1800):
        s=Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=expires_sec)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(120),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) 
    #here user_id column is created which takes an integer which will be linked to the id column of user table
    #this shows that whatever user_id will be of a post will link this post with that user in user table 
    #now the posts in User shows a relation that 1 user can relate to many post and author method is created in post that gives the user related to that post

    def __repr__(self):
        return f"Post('{self.title}',' {self.date_posted}')"