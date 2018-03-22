from flask import Flask, render_template, request, session

from flask_session import Session

import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)




@app.route("/", methods = ['GET', "POST"])
def index():
    print('hoeren')
    if session.get("notes") is None:
        session['notes'] = []
    else:
        session['notes'] = session.get("notes")
    if request.method == 'POST':

        if request.form.get('submit') == 'Submit':
            note = request.form.get('note')
            session['notes'].append(note)
        else:
            session['notes'][:] = []
    return render_template("template.html", notes =session['notes'])

@app.route("/des")
def des():
    return('desmond')
@app.route('/day')
def day():
    now = datetime.datetime.now()

    new_year = now.month == 9 and now.day == 29
    return render_template("day.html", boal = new_year)


@app.route('/loops')
def loops():
    names = ['desmond', 'Rowan', 'Marloes']
    return render_template('loops.html', names=names)



@app.route('/een')
def een():
    return render_template('een.html')


@app.route('/twee', methods=["POST", "GET"])
def twee():
    name = request.form.get('name')
    if request.method == "GET":
        return "mag niet "
    # haal de naam op van de input filt
    return render_template('twee.html', name=name)
