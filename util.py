import pickle
import collections
import numpy as np
import pandas as pd
from pythainlp import word_tokenize
from keras.preprocessing import sequence
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
import tensorflow as tf

def load_file(file_dir):
    dataset = pd.read_csv(file_dir , header=None)
    X = dataset.iloc[:,0].values.reshape(-1,1)
    return X
###############################################################################
def make_word_tokenize(datas):
    
    list_data = []
    sample = 0
    
    for data in datas :
	
        sample = sample + 1
        print("tokenizing sample " , sample , "of" , len(datas))

        word_tokenized = word_tokenize(''.join(data) , engine = 'newmm')
        list_data.append(word_tokenized)
        
    return list_data
###############################################################################
def make_dictionary():
    with open('./dic/dictionary.pickle', 'rb') as f :
        dictionary = pickle.load(f)
    
    with open('./dic/reverse_dictionary.pickle', 'rb') as f :
        reverse_dictionary = pickle.load(f)
    
    return dictionary , reverse_dictionary
###############################################################################
def int_represent_word (list_data,dictionary,reverse_dictionary) :
    keys = dict.keys(dictionary)
    i = 0
    for data in list_data:
        i = i+1
        print("Representing word by int in sample " , i , " of " , len(list_data))
        
        for word in range(len(data)):
            if data[word] in keys:
                data[word] = dictionary[data[word]]
            else:
                data[word] = dictionary[reverse_dictionary[0]]
    return list_data
###############################################################################
def padding(list_data):
    
    pad = sequence.pad_sequences(list_data, maxlen = 300)
               
    return pad
###############################################################################
def onehot(y):
    
    onehotencoder = OneHotEncoder(categorical_features = [0])
    onehotencoder.fit(np.array(([1],[2],[3],[4],[5])))
    
    y = onehotencoder.transform(y).toarray()
        
    return y
###############################################################################
def preprocessing(file_dir):

    X = load_file(file_dir)
    X = make_word_tokenize(X)
    dictionary , reverse_dictionary = make_dictionary()
    X = int_represent_word(X , dictionary,reverse_dictionary)
	
    i = 0
    count = 0
    lenght = len(X)
    while (i<lenght) :
        if len(X[i]) > 300 :
            del X[i]
            i-=1
            lenght-=1
        i+=1
	
    X = padding(X)
    
    return X