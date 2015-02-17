import nltk

"""
All natural language processing functions are here
"""

pos_replacement = {
    'VB': 'btn-primary',
    'VBP': 'btn-primary', 'NN': 'btn-warning'}

def tag_text(raw_text):
    # split text on sentences
    sigma = []
    for i in nltk.sent_tokenize(raw_text):
        sigma.append(nltk.tokenize.wordpunct_tokenize(i))
    tagged_text = []
    for j in nltk.pos_tag_sents(sigma):  # tagged_sentences_list
        for k in j:
            tagged_text.append(k)
    t_text = ()
    for L in tagged_text:
        word, w_tag = L
        if w_tag in pos_replacement.keys():
            tag = pos_replacement[w_tag]
            tagged_word = {'word': word, 'tag': (tag, 0)}
            print tagged_word
        else:
            tagged_word = {'word': word, 'tag': ('', 0)}
        t_text = t_text + (tagged_word,)
    return t_text
