from flask.templating import render_template
from app import app

@app.route('/')
def home():
    thor = "Welcome, Marvel Fan"
    return render_template('index.html', thor=thor)