from flask import Flask, render_template, request
from f.db import page_data
from f.nlp import summ

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


@app.route('/iml')
def img_launcher():
    return render_template('iml.htm')


@app.route('/projects/teal', methods=['POST', 'GET'])
def teal():
    if request.method == 'POST':
        input_text = request.form['input_text']
        t_words = summ(input_text)
    else:
        t_words = ()
        input_text = ''
    return render_template('teal.htm', tagged_words=t_words,
                           input_text=input_text)


@app.route('/projects/iherb/', defaults={'page': 1})
@app.route('/projects/iherb/page/<int:page>')
def iherb_visualization(page):
    paginator = {'cur_page': page, 'item_per_page': 24}
    (products, pagination) = page_data(paginator)
    return render_template('iherb.htm', products=products,
                           pagination=pagination)


if __name__ == '__main__':
    app.run(debug=True)
