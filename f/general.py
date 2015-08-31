import logging
from flask import Markup
"""
All general functions are here
"""


replacement = {"'": '%27', '.': '%2E', '+': '%2B', '`': '%60',
               '#': '%23', ' ': '%20', '%': '%25', '\xc2': '%194',
               '\xb7': '%183',
               '\xc3': '%195', '\xa9': '%169',
               '\xe9': '%233'}


def clean_data_set(raw_data_set):
    """Replaces prohibited symbols out from data set"""
    data = []
    for k in raw_data_set:
        j = list(k)
        for l in replacement.keys():
            if l in str(j[2]):
                j[2] = str(j[2]).replace(l, replacement[l])
                j[3] = str(j[3]).replace(l, replacement[l])
                j[4] = str(j[4]).replace(l, replacement[l])
            else:
                pass
        data.append(tuple(j))
    return data


def process_product_data(raw_data_set):
    """Replace manufacturer name out from product name"""
    l = list(raw_data_set)
    l[1] = ", ".join(l[1].split(", ")[1:])
    l[8] = Markup(l[8])
    return tuple(l)


def get_page_range(n, pages_tot):
    """Returns pagination range"""
    m = 6  # pagination length
    l = n - m / 2 + 1
    r = n + m / 2
    if l < 1:
        l = l + abs(l) + 1
        r = l + m
    if r > pages_tot:
        r = pages_tot
        l = r - m
    p_range = range(l, r)
    return p_range


def paginate(paginator, pages_num):
    """Cooke pagination values"""
    cur_page = paginator['cur_page']
    per_page = paginator['item_per_page']
    pag_data = []
    page_range = get_page_range(cur_page, pages_num)
    for i in page_range:
        if i == cur_page:
            act = 1
        else:
            act = 0
        pag_data.append({'n': i, 'active': act})
    offset = (cur_page - 1) * per_page
    """
    paginator = (
        {'n': 1, 'active': 1},
        {'n': 2, 'active': 0},
        {'n': 3, 'active': 0},
        {'n': 4, 'active': 0},
        {'n': 5, 'active': 0},
        )
    offset = 10
    """
    return pag_data, offset
