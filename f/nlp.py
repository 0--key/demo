import nltk

"""
All natural language processing functions are here
"""

pos_replacement = {
    'VB': 'btn-primary',
    'VBP': 'btn-primary', 'NN': 'btn-warning'}


def summ(raw_text):
    """
    Transformates input data into appropriate look&see format
    """
    summ_text = ()
    tagged_word = {}
    for L in tag_text(raw_text):
        word, w_tag = L
        if w_tag in pos_replacement.keys():
            if tagged_word['tag']:
                # join together and enlarge in collocation case
                if len(tagged_word['word']) == 2:
                    size = 'lg'
                else:
                    size = 'sm'
            else:
                size = 'xs' ## gradation for significant data
            tag = pos_replacement[w_tag]
            if tagged_word['tag']:
                    word = tagged_word['word'] + ' ' + word
                    summ_text = summ_text[:-1]
            tagged_word = {'word': word, 'tag': tag, 'size': size}
            print tagged_word
        else:
            size = 'normal' ## gradation for noisy data 
            tagged_word = {'word': word, 'tag': '', 'size': size}
        summ_text = summ_text + (tagged_word,)
    return summ_text


def tag_text(raw_text):
    """
    Converts sentences into tuple of tagged words
    """
    # split text on sentences
    sigma = []
    for i in nltk.sent_tokenize(raw_text):
        sigma.append(nltk.tokenize.wordpunct_tokenize(i))
    tagged_text = []
    for j in nltk.pos_tag_sents(sigma):  # tagged_sentences_list
        for k in j:
            tagged_text.append(k)
    return tagged_text
