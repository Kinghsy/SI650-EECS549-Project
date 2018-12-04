
import xml.etree.ElementTree as ET
import Const
import re
from nltk.tokenize import word_tokenize




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
    catchphrases = []                   # inital version consists of sentences
    catchphrases_origin = []            # origin version consists of words
    catchphrases_clear = []             # clear version removes stop words
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
        text = re.sub(u"\s[\w]*&#?[\w]*;[\w]*\s", u"\w", text)

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
        for sen in self.sentences:
            clean_sen = CleanSentence(sen)
            word_tokens = word_tokenize(clean_sen)
            filtered_words = [w for w in word_tokens if not w in Const.stop_words]
            self.sentences_origin.extend(word_tokens)
            self.sentences_clear.extend(filtered_words)


class DocList:

    doc_size = 0
    doc_list = []
    folder_path = ""

    def __init__(self, path):
        self.doc_size = 0
        self.folder_path = path




if __name__ == '__main__':

    path = Const.path_to_data_FCA_fulltext
    filename = "06_1.xml"
    doc1 = Doc(path, filename, 0)




    # print(doc1.sentences)
    # #print(doc1.sentences)
    # print("\n")
    # print(doc1.sentences_origin)
    # print("\n")
    # print(doc1.sentences_clear)



# path = Const.PathGenerator(Const.path_to_data_FCA_fulltext, "06_1.xml")
# print(path)
#
# text = open(path).read()
# text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+",u"",text)
# text = re.sub('"id=', 'id="', text)
# text = re.sub(u"\s[\w]*&#?[\w]*;[\w]*\s", u"\w", text)
# # print(text)
# tree = ET.fromstring(text)
#
# print(tree.tag)
# print(tree[3])
# for ele in tree:
#     print(ele)