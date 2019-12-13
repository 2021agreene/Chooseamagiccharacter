from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/personality', methods = ["GET", "POST"])
def ok():
    user_input = dict(request.form)
    q1 = user_input["question1"]
    q2 = user_input["question2"]
    q3 = user_input["question3"]
    q4 = user_input["question4"]
    q5 = user_input["question5"]
    x = model.question1(q1) + model.question2(q2) + model.question3(q3) + model.question4(q4) + model.question5(q5)
    if x == 5 or x == 6:
        name = "Giddien"
        personality = "It Works!"
    return render_template("results.html", topping = name , personality = personality)
