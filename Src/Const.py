
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

# print(path_to_data_FCA_fulltext)