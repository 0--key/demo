#import sqlite3


"""
All necessary data models are here
"""

class Product():
    """
    iHerb product
    """
    def __init__(self, g, con):  # it's uniq dict to fulfill
        """
        cells filled with DB data
        g argument is a dictionary with criteria
        """
        self.id = g[0]  # an unique identificator
        cur = con.cursor()
        cur.execute('SELECT products.*, products_var_data.cost, \
        products_var_data.is_in_stock, img_index.image, \
        img_index.small_image, img_index.thumbnail \
        FROM products, products_var_data, img_index WHERE \
        products.id=? AND img_index.product_id=products.id AND \
        products_var_data.product_id=products.id', (self.id, ))
        (self.real_id, self.name, self.sku, self.manufacturer, self.manuf_url, self.weight, self.pack_weight, self.dimension, self.description, self.ingredients, self.warning, self.suggested_use, self.cost, self.is_in_stock, self.img, self.s_img, self.th_img) = cur.fetchone()
        print "hello!"
        print cur.fetchone()
        cur.close()
        """id, name, sku, manufacturer, manuf_url, weight, \
        pack_weight, dimension, description, ingredients, warning, \
        suggested_use, cost, is_in_stock, img, s_img, th_img"""

    def agg_data(self, cur):
        """
        Retrieves data about product
        """
        #q_var = (i[1],)
        cur.execute('SELECT products.*, products_var_data.cost, \
        products_var_data.is_in_stock \
        FROM products, products_var_data WHERE products.id=? AND \
        products_var_data.product_id = products.id', self.id)
        cur.fetchone()


class PageDataSet():
    """
    Data representation model
    """

    def __init__(self, cur_page, item_per_page):
        self.products = []
        #self.page_data = 

"""
How it works test
"""
