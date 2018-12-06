# -*- coding: utf-8 -*-

import pickle
from Const import path_to_lda, path_to_index, path_to_dictionary

def myLDA(label_list):
    with open(path_to_lda, "rb") as f_lda:
        lda = pickle.load(f_lda)
    with open(path_to_index, "rb") as f_index:
        index = pickle.load(f_index)
    with open(path_to_dictionary, "rb") as f_dictionary:
        dictionary = pickle.load(f_dictionary)
    query_bow = dictionary.doc2bow(label_list)
    query_lda = lda[query_bow]
    sims = index[query_lda]
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
    return sort_sims
