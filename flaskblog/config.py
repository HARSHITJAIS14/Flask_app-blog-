import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'app.hjais@gmail.com'
    MAIL_PASSWORD = 'qbydohzlghiwxnee'
    MAIL_DEFAULT_SENDER = 'app.hjais@gmail.com'

