import sqlite3
from settings import item_per_page
from general import purify_url, clean_data_set


"""
Resolves interactions with DB
"""


def dumb_extractor(offset):
    """
    Extracts entire dataset begins from a
    """
    conn = sqlite3.connect('scraped.db')
    cur = conn.cursor()
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
    return page_data_set
