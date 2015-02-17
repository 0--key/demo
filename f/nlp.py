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
            size = 'xs' ## gradation for significant data
            tag = pos_replacement[w_tag]
            tagged_word = {'word': word, 'tag': tag, 'size': size}
            print tagged_word
        else:
            size = 'normal' ## gradation for noisy data 
            tagged_word = {'word': word, 'tag': '', 'size': size}
        t_text = t_text + (tagged_word,)
    return t_text, tagged_text



def tag_text_review(raw_text):
    # split text on sentences
    sigma = []
    for i in nltk.sent_tokenize(raw_text):
        sigma.append(nltk.tokenize.wordpunct_tokenize(i))
    tagged_text = []
    for j in nltk.pos_tag_sents(sigma):  # tagged_sentences_list
        for k in j:
            tagged_text.append(k)
    return tagged_text
