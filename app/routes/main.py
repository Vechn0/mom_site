from flask import Blueprint,render_template

bp = Blueprint("main",__name__)


@bp.route("/info")
def info():
    return render_template("info.html")
