from werkzeug.security import generate_password_hash

from models.db import db
from models.admin import Admin


def create_default_admin():
    """
    Create default admin if it doesn't exist.
    """

    admin = Admin.query.filter_by(username="admin").first()

    if admin:
        return

    new_admin = Admin(
        full_name="System Administrator",
        username="admin",
        password=generate_password_hash("admin123"),
        role="Super Admin",
        is_active=True
    )

    db.session.add(new_admin)
    db.session.commit()