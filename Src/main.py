from collections import Counter
import myBM25, myLDA, Const
import nltk

def count_lda_result(lda_result):
    count = {}
    for item in lda_result:
        count[item[0]] = item[1]
    return Counter(count)

def main_driver(queries, label):

    with open(Const.path_to_FCA_abstract_raw) as f:
        abstract = f.readlines()
    abstract_lower = [item.lower() for item in abstract]
    
    with open(Const.path_to_title_file, encoding = "iso-8859-1") as f:
        title_list = f.readlines()
    
    with open(Const.path_to_link_file) as f:
        link_list = f.readlines()

    #queries = "1 2 3 4"
    #label = ['murder', 'trade', 'business']
    labels = ' '.join(label)

    final_query = queries + " " + labels
    result = myBM25.BM25_score(abstract_lower, final_query)
    id_result = [int(item[0]) for item in result]
    #print(id_result)
    
    if len(id_result) > Const.BOUND:
        ranks = id_result
    elif len(id_result) == 0:
        lda_result = myLDA.myLDA(final_query.split())
        ranks = [item[0] for item in lda_result[:Const.ideal_length]]
    else:
        ranks = id_result
        cou = Counter()
        for i in id_result:
            lda_result = myLDA.myLDA(lines[i].split())
            cou += count_lda_result(lda_result)
        potential_list = cou.most_common(Const.ideal_length)
        for i in potential_list:
            if i[0] not in ranks:
                ranks.append(i[0])
    
    return [(title_list[i], link_list[i], abstract[i]) for i in ranks]
    #docu_list = ProcessDoc.DocList(path_to_data_FCA_fulltext)
    #return docu_list

if __name__ == "__main__":
    ranks = main_driver("trade", [])
    for i in ranks:
        print(i)
# print(len(ranks))