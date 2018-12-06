import os
from whoosh.index import create_in
from whoosh.fields import *
import json
from Const import path_to_FCA_abstract_raw

def BM25_score(lines, query):
    with open(path_to_FCA_abstract_raw) as f:
        lines = f.readlines()

    #build schema, if the store is ture, it can be searched.
    schema = Schema(title = TEXT(stored = True), path = ID(stored = False),
                    content = TEXT(stored = True))
                    #build a path 'indexdir/' to store the information of schema
    indexdir = 'indexdir/'
    if not os.path.exists(indexdir):
        os.mkdir(indexdir)
    ix = create_in(indexdir, schema)
    writer = ix.writer()
    for i in range(len(lines)):
        writer.add_document(title = str(i),path = '/' + str(i), content = lines[i])
    writer.commit()
    searcher = ix.searcher()
    # search the document that include query and get the BM25 score
    results = searcher.find("content", query, limit=None)
    return_value = [[dict(item)['title'], item.score]for item in results]
    return return_value
