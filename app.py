from flask import Flask, render_template, request, redirect, url_for
import datetime
from tools import redblue  # Removed encryption 

app = Flask(__name__)

# In-memory logs
attack_log = []
defense_log = []

@app.route('/')
def entry():
    return render_template("entry.html")

@app.route('/vm-setup')
def vm_setup():
    return render_template("vm_setup.html")

@app.route('/dashboard')
def index():
    return render_template("index.html", attack_log=attack_log, defense_log=defense_log)

@app.route('/attack', methods=['POST'])
def red_team_attack():
    attack = request.form['attack']
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    attack_log.append({"time": timestamp, "event": attack})
    return redirect(url_for('index'))

@app.route('/defend', methods=['POST'])
def blue_team_defend():
    defense = request.form['defense']
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    defense_log.append({"time": timestamp, "event": defense})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
