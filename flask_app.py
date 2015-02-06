import sqlite3
from flask import Flask, render_template
app = Flask(__name__)

def purify_url(raw_url):
    return str(raw_url).replace('%','%25')

@app.route('/')
def hello_world():
    return render_template('index.htm')

@app.route('/about')
def about():
    return render_template('about.htm')


@app.route('/search')
def search_item():
    name = 'Anton Kosinov'
    conn = sqlite3.connect('/home/kosmic/mysite/scraped.db')
    cur = conn.cursor()
    query = 'select id, product_id, small_image, thumbnail from products01_img_idxs limit 40 offset 100'
    cur.execute(query)
    raw_data = cur.fetchall()
    # lets purify data:
    data = []
    for k in raw_data:
        j = list(k)
        if '%' in j[2]:
            j[2] = purify_url(j[2])
            j[3] = purify_url(j[3])
        data.append(tuple(j))
    #data = cur.fetchall()
    # lets purify data:
    #data = []
    #for j in raw_data:
        #if '%' in j[2]:
            #j[2] = purify_url(j[2])
            #j[3] = purify_url(j[3])
        #data.append(j)
    entire_data = []
    for i in data:
        query = "select name, sku, manufacturer, manuf_url from products01 WHERE id=%s" % i[1]
        cur.execute(query)
        product_properties = cur.fetchone()
        entire_data.append(i+product_properties)
    conn.close()
    return render_template('search.htm', name=name, products=entire_data)


if __name__ == '__main__':
    app.run()




