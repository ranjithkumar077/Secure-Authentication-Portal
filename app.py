import os
from flask import Flask
from flask_login import LoginManager
from config import Config
from models.user_model import db, User

# We can initialize login manager here
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure database directory exists
    db_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database')
    os.makedirs(db_dir, exist_ok=True)

    db.init_app(app)
    
    # We can import routes here to avoid circular imports
    from routes.auth_routes import auth_bp, bcrypt
    bcrypt.init_app(app)
    
    login_manager.init_app(app)
    
    app.register_blueprint(auth_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
