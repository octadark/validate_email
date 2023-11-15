from flask import render_template, redirect, request
from app_flask import app
from app_flask.modelos.email import Email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/results')
    Email.save(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html",emails=Email.get_all())

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.delete(data)
    return redirect('/results')