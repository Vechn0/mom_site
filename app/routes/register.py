from flask import Blueprint,render_template
from flask import request,flash
from app.models import User
from app.forms import RegistersForm, LoginsForm
from app.extensions import db
bp = Blueprint("auth",__name__)



@bp.route("/",methods=["GET","POST"])
def login():
    form = LoginsForm()
    if request.method == "POST":
        
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                pass
                #доделать логированных пользователей
            else:
                flash("Неверный логин или пароль","danger")
    else:

        return render_template("login.html",form=form)

@bp.route("/register",methods=["GET","POST"])
def register():
    form = RegistersForm()
    if request.method == "POST":
        
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            password2 = form.password2.data
            if password != password2:
                flash("Пароли не совпадают","danger")
                return render_template("register.html",form=form)
            user = User.query.filter_by(username=username).first()
            if user:
                flash("Пользователь с таким именем уже существует","danger")
                return render_template("register.html",form=form)
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return render_template("success.html")
        
        else:
            flash("Неверный логин или пароль","danger")
    else:

        
        return render_template("register.html",form=form)