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
