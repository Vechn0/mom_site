from flask import Blueprint,render_template
from flask_login import login_required  

bp = Blueprint("main",__name__)


@bp.route("/info")
def info():
    return render_template("info.html")

@bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html")