from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models import comment

@app.route('/post_comment/<post_id>',methods=["POST"])
def wall_comment(post_id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "com_content": request.form['com_content'],
        "post_id": post_id,
        'user_id': session['user_id']
    }
    comment.Comment.save_comment(data)
    return redirect('/wall')
