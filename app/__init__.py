from flask import Flask

from app.extensions import db,migrate
from app.config import Config
from app.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app,db)

    from app.routes import main,register
    app.register_blueprint(register.bp)
    app.register_blueprint(main.bp)
    
    
    
    return app