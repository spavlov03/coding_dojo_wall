from flask import render_template, redirect, request,session,flash
from flask_app import app
from flask_app.models import user,post,comment
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if "user_id" in session:
        return redirect("/wall")
    return render_template('index.html')
@app.route("/register",methods=["POST"])
def register(): 
    if not user.User.validate_user(request.form):
        return redirect("/")
    data = {
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "email":request.form['email'],
            "password":bcrypt.generate_password_hash(request.form['password'])
        }
    user_id = user.User.register(data)
    session['user_id'] = user_id

    return redirect("/wall")

@app.route('/login',methods=["POST"])
def login():
    users = user.User.get_user_info_by_email(request.form)
    #print("USERS EMAILS ARE",users_emails)
    if not users:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(users.password, request.form['password']):
        flash("invalid Password","login")
        return redirect('/')
    session['user_id'] = users.id
    return redirect("/wall")
@app.route("/wall")
def dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id": session['user_id']}
    return render_template('wall.html',user = user.User.get_user_by_id(data),all_posts=post.Post.get_all_posts_with_creator(),all_comments=comment.Comment.get_all_comments())
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
