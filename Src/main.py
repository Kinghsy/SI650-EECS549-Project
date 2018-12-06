#import os, json, pickle
from collections import Counter
#from whoosh.index import create_in
#from whoosh.fields import *
from Const import BOUND, ideal_length, path_to_FCA_abstract_raw, path_to_data_FCA_fulltext
import myBM25, myLDA, ProcessDoc

def count_lda_result(lda_result):
    count = {}
    for item in lda_result:
        count[item[0]] = item[1]
    return Counter(count)

def main(queries, label):

    with open(path_to_FCA_abstract_raw) as f:
        lines = f.readlines()

    #queries = "1 2 3 4"
    #label = ['murder', 'trade', 'business']
    labels = ' '.join(label)

    final_query = queries + " " + labels
    result = myBM25.BM25_score(lines, final_query)
    id_result = [int(item[0]) for item in result]
    print(id_result)
    
    if len(id_result) > BOUND:
        ranks = id_result
    elif len(id_result) == 0:
        lda_result = myLDA.myLDA(final_query.split())
        ranks = [item[0] for item in lda_result[:ideal_length]]
    else:
        ranks = id_result
        cou = Counter()
        for i in id_result:
            lda_result = myLDA.myLDA(lines[i].split())
            cou += count_lda_result(lda_result)
        potential_list = cou.most_common(ideal_length)
        for i in potential_list:
            if i[0] not in ranks:
                ranks.append(i[0])
    
    docu_list = ProcessDoc.DocList(path_to_data_FCA_fulltext)
    return docu_list

ranks = main("trade", [])
print(ranks)
# print(len(ranks))