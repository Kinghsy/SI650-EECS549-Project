
import xml.etree.ElementTree as ET
import Const
import re
import os
from nltk.tokenize import word_tokenize
from collections import defaultdict
import pickle




def CleanSentence(text_origin):
    # filter all nonsense punctuation
    # alter into lowercase chars
    # replace some abbr with full text
    # replace some symbol with words, specifically @ $ &

    text = text_origin.lower()
    text = re.sub(r"[^A-Za-z0-9()@&$\''\`\\_\n]", " ", text)
    text = re.sub(r"\n", " ", text)

    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"cannot", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)

    text = text.replace('&', ' and')
    text = text.replace('@', ' at')
    text = text.replace('$', ' dollar')

    return text



class Doc:

    doc_id = 0
    name = ""
    link = ""
    catchphrases = []  # inital version consists of sentences
    catchphrases_origin = []  # origin version consists of words
    catchphrases_clear = []  # clear version removes stop words
    sentences = []
    sentences_origin = []
    sentences_clear = []

    def __init__(self, path, filename, id):

        self.doc_id = id

        direc = Const.PathGenerator(path, filename)
        text = open(direc).read()
        # clear some typo in the .xml file
        text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", text)
        text = re.sub('"id=', 'id="', text)
        text = re.sub(u"&#?[\w]*;", u"\w", text)

        # phrase the .xml file using ElementTree
        tree = ET.fromstring(text)
        for item in tree:
            if item.tag == 'name':
                self.name = item.text
            if item.tag == 'AustLII':
                self.link = item.text
            if item.tag == 'catchphrases':
                for item2 in item:
                    self.catchphrases.append(item2.text)
            if item.tag == 'sentences':
                for item2 in item:
                    self.sentences.append(item2.text)

        # build origin version & clear version
        for sen in self.catchphrases:
            clean_sen = CleanSentence(sen)
            word_tokens = word_tokenize(clean_sen)
            filtered_words = [w for w in word_tokens if not w in Const.stop_words]
            self.catchphrases_origin.extend(word_tokens)
            self.catchphrases_clear.extend(filtered_words)
        # for sen in self.sentences:
        #     clean_sen = CleanSentence(sen)
        #     word_tokens = word_tokenize(clean_sen)
        #     filtered_words = [w for w in word_tokens if not w in Const.stop_words]
        #     self.sentences_origin.extend(word_tokens)
        #     self.sentences_clear.extend(filtered_words)



class DocList:

    doc_size = 0
    doc_list = []
    folder_path = ""

    def __init__(self, path, year):
        self.doc_size = 0
        self.folder_path = path
        file_list = os.listdir(self.folder_path)
        print(file_list)
        xml_files = []
        for file in file_list:
            if (not os.path.isdir(file)) and (file[0:2] == year):
                xml_files.append(file)
        for xml_name in xml_files:
            print(xml_name)
            newDoc = Doc(self.folder_path, xml_name, self.doc_size)
            print(self.doc_size)
            self.doc_size = self.doc_size + 1
            self.doc_list.append(newDoc)



if __name__ == '__main__':

    path = Const.path_to_data_FCA_fulltext
    # filename = "06_1.xml"
    # doc1 = Doc(path, filename, 0)
    # pickle.dump(doc1, open("a.dat", 'wb'), True)
    # doc2 = pickle.load(open("a.dat", 'rb'))
    # print(doc2.catchphrases)
    # print(doc2.catchphrases_clear)
    #  print(docu_list.doc_list)
    # pickle.dump(docu_list, open("..\DataSrc\FCA_06.dat", 'wb'), True)
    # docu_list = pickle.load(open("..\DataSrc\FCA_06.dat", 'rb'))

    docu_list = DocList(path, "06")
    print(docu_list.doc_size)
    d = defaultdict(lambda : 0)
    print("start dict")
    for doc in docu_list.doc_list:
        print(doc.doc_id)
        for word in doc.catchphrases_clear:
            d[word] = d[word] + 1
    print("end dict")
    pickle.dump(d, open("..\DataSrc\FCA_06_label_full.dat", 'wb'), True)

    docu_list1 = DocList(path, "07")
    print(docu_list1.doc_size)
    dd = defaultdict(lambda : 0)
    print("start dict")
    for doc in docu_list1.doc_list:
        print(doc.doc_id)
        for word in doc.catchphrases_clear:
            dd[word] = dd[word] + 1
    print("end dict")
    pickle.dump(dd, open("..\DataSrc\FCA_07_label_full.dat", 'wb'), True)

    docu_list2 = DocList(path, "08")
    print(docu_list2.doc_size)
    ddd = defaultdict(lambda : 0)
    print("start dict")
    for doc in docu_list2.doc_list:
        print(doc.doc_id)
        for word in doc.catchphrases_clear:
            ddd[word] = ddd[word] + 1
    print("end dict")
    pickle.dump(ddd, open("..\DataSrc\FCA_08_label_full.dat", 'wb'), True)

    docu_list3 = DocList(path, "08")
    print(docu_list3.doc_size)
    dddd = defaultdict(lambda : 0)
    print("start dict")
    for doc in docu_list3.doc_list:
        print(doc.doc_id)
        for word in doc.catchphrases_clear:
            dddd[word] = dddd[word] + 1
    print("end dict")
    pickle.dump(dddd, open("..\DataSrc\FCA_09_label_full.dat", 'wb'), True)

    sorted(d.items(), key = lambda x: x[1], reverse=True)
    list = []
    print("end sort")
    for x,y in d:
        list.append(x)
    print(list)
    print(d)


