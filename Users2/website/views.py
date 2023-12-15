from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
   return render_template("home.html", user=current_user)

@views.route('/user')
@login_required
def user():
   return render_template("userDash.html", user=current_user)

@views.route('/chef')
@login_required
def chef():
   return render_template("chefDash.html", user=current_user)