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
    print(x)
    if x == 5 or x == 6:
        name = "Giddeon Jura"
        descriptions = "Strong and caring Gideon fights for those around him and those he cares about."
        color = "White"
        image = "https://vignette.wikia.nocookie.net/duelsoftheplaneswalkers/images/6/67/Gideon_Jura.png/revision/latest?cb=20110215092601"
    if x == 8 or x == 7:
        name = "Jace Beleren"
        descriptions = "Intelligent and loyal Jace uses his illusionary magic to aid his companions in any way he can, from creating a plan of attack so simply assessing the situation."
        color = "Blue"
        image = "https://comicvine1.cbsistatic.com/uploads/original/11122/111221607/6241482-9966752686-dac36.jpg"
    if x == 11:
        name = "Chandra Nalaar"
        descriptions = "Hot-headed and temperamental Chandra is a pyromancer, acting on emotion and often charging with a full plan in motion."
        color = "Red"
        image = "https://pbs.twimg.com/media/DkneOnSWwAAXCWP.jpg"
    if x == 12 or x == 13 or x == 14:
        name = "Lilliana Vess"
        descriptions = "Cunning and mischievous, Lilliana has a complicated past that she tries to make up for, often working for only her benefit but deep down caring for others."
        color = "Black"
        image = "https://i.pinimg.com/474x/e0/d0/1b/e0d01bc23113628b019263e96a0b700e--game-character-character-concept.jpg"
    if x == 10 or x == 9:
        name = "Nissa Revane"
        descriptions = " Being an elf Nissa is in tune with nature, often using natural energy from the lands around her to enhance her abilities. Although she tries not to use violence in her actions if it can be helped."
        color = "Green"
        image = "https://i.redd.it/woznvlwm5rs31.jpg"
    return render_template("results.html", title = name , description = descriptions, color = color, image = image)
