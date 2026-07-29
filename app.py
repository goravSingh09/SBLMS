from flask import Flask

from config import Config
from models.db import db
from models.student import Student
from models.admin import Admin
from services.admin_service import create_default_admin
from routes.admission import admission_bp
from routes.admin import admin_bp
from routes.home import home_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
    create_default_admin()

app.register_blueprint(home_bp)
app.register_blueprint(admission_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)