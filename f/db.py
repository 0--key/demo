import sqlite3
from settings import item_per_page
from general import clean_data_set, paginate, process_product_data
from models import Product

"""
Resolves interactions with DB
"""


def page_data(paginator):
    """
    Extracts paginated data out from db
    paginator = {'cur_page': 1, 'item_per_page': 25}
    """
    (start_page, item_per_page) = (paginator['cur_page'],
                                   paginator['item_per_page'])
    conn = sqlite3.connect('scraped.db')
    cur = conn.cursor()
    # Prepare paginator data:
    cur.execute('SELECT COUNT(*) FROM img_index')
    img_number = cur.fetchone()
    total_pages_num = img_number[0] / item_per_page + 1
    (paginator_data, offset) = paginate(paginator, total_pages_num)
    # Prepare page dataset
    query_var = (item_per_page, offset)
    cur.execute('SELECT * FROM img_index LIMIT ? OFFSET ?', query_var)
    raw_data = cur.fetchall()
    # lets purify the raw data:
    data = clean_data_set(raw_data)
    page_data_set = []
    for i in data:
        q_var = (i[1],)
        cur.execute('SELECT * FROM products WHERE id=?', q_var)
        product_properties = process_product_data(cur.fetchone())
        page_data_set.append(i+product_properties)
    conn.close()
    catalogue = get_catalogue()
    return page_data_set, paginator_data, catalogue


def get_cat_tree():
    """
    Extracts categories relations out from DB
    {'first_category': {'child':
    CREATE TABLE categories (id integer primary key autoincrement, category, parent_id, depth, foreign key (parent_id) references categories(id));
    """
    conn = sqlite3.connect('scraped.db')
    cur = conn.cursor()
    cur.execute('SELECT category FROM products_var_data')
    raw_categories = cur.fetchall()
    #print set(raw_categories), len(set(raw_categories)), raw_categories, len(raw_categories)
    for i in set(raw_categories):
        categories = i[0].split('/')[1:]
        depth = 1
        p_id = 1
        for j in categories:
            j = j.replace(';', '')
            # does this category exists already:
            try:
                cur.execute('SELECT id FROM categories WHERE depth=? \
                AND category=?', (depth, buffer(j)))
                n = cur.fetchone()
                if n:  # skip insertion
                    p_id = n[0]
                    depth = depth + 1
                    continue
                else:
                    #print j
                    #
                    cur.execute('INSERT INTO categories(category, \
                    parent_id, depth) VALUES (?,?,?)', (buffer(j), p_id, depth))
                    #print (buffer(j), p_id, depth)
                    p_id = cur.lastrowid
                    depth = depth + 1
                    conn.commit()
            except ValueError:
                print j
                continue
    conn.close()    

def get_catalogue():
    """
    Extracts catalogue metadata
    catalogue_data = ({'name': 'cosmetics', 'count': 127, 'depth': 1}, ...)
    """
    conn = sqlite3.connect('scraped.db')
    cur = conn.cursor()
    # Prepare paginator data:
    cur.execute('SELECT category FROM categories')
    catalogue_data = []
    for i in cur.fetchall()
        catalogue_data.append(i[0])
    conn.close()
    return catalogue_data


"""
create table categories (id integer primary key autoincrement, category, parent_id, depth, foreign key (parent_id) references categories(id));
insert into categories values (NULL, 'top', 0, 1);
"""
