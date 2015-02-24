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
    catalogue_data = ()
    for i in raw_categories:
        categories = i[0].split('/')[1:]
        depth = 1
        p_id = 1
        for j in categories:
            # does this category exists already:
            cur.execute('SELECT id FROM categories WHERE depth=? \
            AND category=?', (depth, j))
            n = cur.fetchone()
            if n:  # skip insertion
                p_id = n
                depth = depth + 1
                continue
            else:
                cur.execute('INSERT INTO categories VALUES ("NULL", \
                ?,?,?)', (j, p_id, depth))
                print (j, p_id, depth)
                p_id = cur.lastrowid
                depth = depth + 1
    conn.close()

def get_catalogue():
    """
    Extracts catalogue metadata
    catalogue_data = ({'name': 'cosmetics', 'count': 127, 'depth': 1}, ...)
    """
    conn = sqlite3.connect('scraped.db')
    cur = conn.cursor()
    # Prepare paginator data:
    cur.execute('SELECT category FROM products_var_data')
    raw_categories = cur.fetchall()
    catalogue_data = ()
    for i in raw_categories:
        categories = i[0].split('/')[1:]
        #print cat_list
        d = 0  # deepth counter
        for j in categories:  # fullfill the catalogue tree
            for k in catalogue_data:
                if k['name'] == j:  # this categore is already exists
                    k['count'] = k['count'] + 1
                    break
            new_category = {'name': j, 'depth': d, 'count': 1}
            catalogue_data = catalogue_data + (new_category,)
            d = d + 1
    conn.close()
    return catalogue_data


"""
create table categories (id integer primary key autoincrement, category, parent_id, depth, foreign key (parent_id) references categories(id));
insert into categories values (NULL, 'top', 0, 1);
"""
