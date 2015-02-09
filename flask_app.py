import sqlite3
from flask import Flask, render_template
from f.general import purify_url
from f.db import dumb_extractor


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.htm', home=True)


@app.route('/about')
def about():
    return render_template('about.htm', about=True)


@app.route('/projects/ui')
def ui_design():
    return render_template('ui.htm')


@app.route('/projects/iherb')
def iherb_visualization():
    entire_data = dumb_extractor(20)
    return render_template('iherb.htm', products=entire_data)


if __name__ == '__main__':
    app.run(debug=True)
