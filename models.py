"""
All data models are here
"""

class Product():
    """
    iHerb product
    """
    def __init__(self):
        self.name = ''
        self.t_img = ''
        self.s_img = ''
        self.l_img = ''

    def __repr__(self):
        r = {
            "name": self.name,
            "t_img": self.t_img,
            "s_img": self.s_img,
            "l_img": self.l_img
        }
        return r
