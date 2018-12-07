# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
#
# example_sent = "This is a sample sentence, showing off the stop words filtration."
#
# stop_words = set(stopwords.words('english'))
#
# print(stop_words)
#
#
# word_tokens = word_tokenize(example_sent)
#
# filtered_sentence = [w for w in word_tokens if not w in stop_words]
#
# print(filtered_sentence)
#
# filtered_sentence = []
#
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#
# print(word_tokens)
# print(filtered_sentence)

# d = {'a': 1, 'b': 2, 'c': 3}
# sorted_d = sorted(d.items(), key = lambda k : k[1], reverse = True)
# print(sorted_d)


# class test:
#     l = []
#     def __init__(self, a):
#         # self.l = []
#         self.l.append(a)
#
# t = test(1)
# print(t.l)
#
# t = test(2)
# print(t.l)

# from nltk.tokenize import word_tokenize
# import nltk
# from nltk.stem.wordnet import WordNetLemmatizer
#
#
# print(WordNetLemmatizer().lemmatize('made','v'))

# text = word_tokenize("that could is a good solution, but we should carefully thought about it")
# pos_tag = nltk.pos_tag(text)
# print(pos_tag)
# print(pos_tag[2][1])

# stoplabel = []
# f = open("..\DataSrc\stoplabel.txt", "r")
# content = f.read().splitlines()
# print(content)

#
# list = [4, 3, 2, 1]
# list.remove(4)
# print(list)
# if 5 in list:
#     list.remove(5)
# print(list)

import sys
sys.path.append("..\\Src")
import main

result = main.main_driver("trade", "act")
print(result[0][0])