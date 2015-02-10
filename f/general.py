"""
All general functions are here
"""


def purify_url(raw_url):
    """Replases prohibited symbols out from raw url"""
    return str(raw_url).replace('%', '%25')


def clean_data_set(raw_data_set):
    """Puryfies data set"""
    data = []
    for k in raw_data_set:
        j = list(k)
        if '%' in j[2]:
            j[2] = purify_url(j[2])
            j[3] = purify_url(j[3])
        data.append(tuple(j))
    return data


def get_page_range(n, pages_tot):
    """Returns pagination range"""
    m = 10  # pagination length
    l = n - 5
    r = n + 6
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
