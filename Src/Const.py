
# file includes all constants
# like the file path
# or other parameters
# for the convenience of debuging and adjusting

import os

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

data_file_name = "DataSrc"
dataset_1 = "FCA 2006-2009"
path_to_data_FCA_fulltext = os.path.join(os.getcwd(), "..", data_file_name, dataset_1, "fulltext")
def PathGenerator(dir, subdir):
    return os.path.join(dir, subdir)

path_to_FCA_abstract_raw = os.path.join(os.getcwd(), "..", data_file_name, "FCA_abstract_raw.txt")
path_to_label_file = os.path.join(os.getcwd(), "..", data_file_name, "FCA_label.txt")

model_file = "lda_model"
path_to_lda = os.path.join(os.getcwd(), model_file, "lda.pkl")
path_to_index = os.path.join(os.getcwd(), model_file, "index.pkl")
path_to_dictionary = os.path.join(os.getcwd(), model_file, "dictionary.pkl")

BOUND = 20
ideal_length = 100

# print(path_to_data_FCA_fulltext)
