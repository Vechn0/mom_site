from app.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import login_manager

#https://vk.com/filesfedsite



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(80),unique=True,nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    def __repr__(self):
        return f"<User {self.username}>"
    

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    type = db.Column(db.Integer, nullable=False)  # 0 - изображение, 1 - видео, 2 - аудио
   




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

login_manager.login_view = "main.login"
    



