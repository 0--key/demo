import sqlite3
from settings import item_per_page
from general import clean_data_set, paginate


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
    cur.execute('select id, product_id, small_image, thumbnail \
    from img_index limit ? offset ?', query_var)
    raw_data = cur.fetchall()
    # lets purify the raw data:
    data = clean_data_set(raw_data)
    page_data_set = []
    for i in data:
        q_var = (i[1],)
        cur.execute('select name, sku, manufacturer, manuf_url \
        from products WHERE id=?', q_var)
        product_properties = cur.fetchone()
        page_data_set.append(i+product_properties)
    conn.close()
    return page_data_set, paginator_data
