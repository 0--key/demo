import sqlite3
from flask import Flask, render_template
from f.general import purify_url
from f.db import page_data


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.htm', home=True)


@app.route('/about')
def about():
    return render_template('about.htm', about=True)


@app.route('/contact')
def contact():
    return render_template('contact.htm', contact=True)


@app.route('/projects/ui')
def ui_design():
    return render_template('ui.htm')


@app.route('/projects/teal')
def teal():
    return render_template('teal.htm')


@app.route('/projects/iherb/', defaults={'page': 1})
@app.route('/projects/iherb/page/<int:page>')
def iherb_visualization(page):
    paginator = {'cur_page': page, 'item_per_page': 25}
    (products, pagination) = page_data(paginator)
    return render_template('iherb.htm', products=products,
                           pagination=pagination)


if __name__ == '__main__':
    app.run(debug=True)
