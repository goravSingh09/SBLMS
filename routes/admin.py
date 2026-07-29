from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    session
)

from werkzeug.security import check_password_hash

from forms.admin_login_form import AdminLoginForm
from models.admin import Admin

admin_bp = Blueprint(
    "admin",
    __name__
)


@admin_bp.route("/admin/login", methods=["GET", "POST"])
def login():

    form = AdminLoginForm()

    if form.validate_on_submit():

        admin = Admin.query.filter_by(
            username=form.username.data
        ).first()

        if admin and check_password_hash(
            admin.password,
            form.password.data
        ):

            session["admin_id"] = admin.id
            session["admin_name"] = admin.full_name

            flash(
                "Login Successful!",
                "success"
            )

            return redirect(
                url_for("admin.dashboard")
            )

        flash(
            "Invalid Username or Password",
            "danger"
        )

    return render_template(
        "admin/login.html",
        form=form
    )


@admin_bp.route("/admin/dashboard")
def dashboard():

    if "admin_id" not in session:

        flash(
            "Please login first.",
            "warning"
        )

        return redirect(
            url_for("admin.login")
        )

    return render_template(
        "admin/dashboard.html"
    )
@admin_bp.route("/admin/logout")
def logout():

    session.clear()

    flash(
        "Logged out successfully.",
        "success"
    )

    return redirect(
        url_for("admin.login")
    )