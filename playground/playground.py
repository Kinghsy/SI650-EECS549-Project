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

d = {'a': 1, 'b': 2, 'c': 3}
sorted_d = sorted(d.items(), key = lambda k : k[1], reverse = True)
print(sorted_d)


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