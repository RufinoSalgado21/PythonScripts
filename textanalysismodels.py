# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:57:19 2019

@author: RufinoS
"""

import nltk
import re
import heapq
import numpy as np
#regular expression library

paragraph = """Thank you all so very much. Thank you to the Academy. 
               Thank you to all of you in this room. I have to congratulate 
               the other incredible nominees this year. The Revenant was 
               the product of the tireless efforts of an unbelievable cast
               and crew. First off, to my brother in this endeavor, Mr. Tom 
               Hardy. Tom, your talent on screen can only be surpassed by 
               your friendship off screen … thank you for creating a t
               ranscendent cinematic experience. Thank you to everybody at 
               Fox and New Regency … my entire team. I have to thank 
               everyone from the very onset of my career … To my parents; 
               none of this would be possible without you. And to my 
               friends, I love you dearly; you know who you are. And lastly,
               I just want to say this: Making The Revenant was about
               man's relationship to the natural world. A world that we
               collectively felt in 2015 as the hottest year in recorded
               history. Our production needed to move to the southern
               tip of this planet just to be able to find snow. Climate
               change is real, it is happening right now. It is the most
               urgent threat facing our entire species, and we need to work
               collectively together and stop procrastinating. We need to
               support leaders around the world who do not speak for the 
               big polluters, but who speak for all of humanity, for the
               indigenous people of the world, for the billions and 
               billions of underprivileged people out there who would be
               most affected by this. For our children’s children, and 
               for those people out there whose voices have been drowned
               out by the politics of greed. I thank you all for this 
               amazing award tonight. Let us not take this planet for 
               granted. I do not take tonight for granted. Thank you so very much."""
              
dataset = nltk.sent_tokenize(paragraph)

#1 clean the text of punctuation and nonwords
for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r'\W', ' ', dataset[i])
    #remove nonwords, replace with space
    dataset[i] = re.sub(r'\s+',' ', dataset[i]) 
    #remove multiple spaces, replace with one space
    
#2 create a histogram
    #create a dictionary
word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data)
    #get words, for each word, if not already in the dictionary
    #insert and start count
    #if in the dict, increment the existing count
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1 
        else:
            word2count[word] += 1

#3 filter the words to the most frequent
#returns 100 largest keys
freq_words = heapq.nlargest(100, word2count, key = word2count.get)

#BOW model
x = []
for data in dataset:
    vector = []
    for word in freq_words:
        if word in nltk.word_tokenize(data):
            vector.append(1)
        else:
            vector.append(0)
    x.append(vector)
    #PRODUCES an array with 21 values per freq_word, 1 if the word appears
    #in said sentence, 0 if not

#produces list of lists per sentence counting when one of the 
#filtered words appears 
x = np.asarray(x)
#produces 2d array of BOW with 21 days of 100 columns for each frequent word


#tdidf model
#1 preprocess text the same as BOW
#2 create histogram
#3 filter freq words
word_idf = {}

#for each of the frequent words,
#if it appears in a given sentence, increase count
#after cycling throught the dataset, divide the entire number of sentences
#by the number of their occurences
for word in freq_words:
    doc_count = 0
    for data in dataset:
        if word in nltk.word_tokenize(data):
            doc_count += 1        
    word_idf[word] = np.log(len(dataset) / doc_count+1)
#produces a dict with the frequent words and their idf values
    
#produce TF matrix
tf_matrix = {}
for word in freq_words:
    doc_tf = []
    #for each sentence...
    for data in dataset:
        frequency = 0
        #..and each word in each sentence...
        for w in nltk.word_tokenize(data):
            #...if the freq_word appears in the sentence...
            if w == word:
                frequency += 1
                #...increase frequency...
        #...then find the tf score for said word by dividing frequency by
        #the number of total words in the sentence...
        tf_word = frequency / len(nltk.word_tokenize(data))
        doc_tf.append(tf_word)
        #...then add this value to the end of the list...
    tf_matrix[word] = doc_tf
    #...finally add the list of values, one per frequent word, until
    #you have a dict of lists containing tf scores for each freq word
    #compared against each sentence in the text.
    #ex: {'the': [0.0, 0.2,...]}
    
tfidf_matrix = []
#for each key in the tf_matrix...
for word in tf_matrix.keys():
    tfidf = []
    #...iterate over each value for each respective key...
    for value in tf_matrix[word]:
        #..multiplying the value by the corresponding idf score...
        score = value*word_idf[word]
        tfidf.append(score)
    #..then append these new scores to the tfidf matrix.    
    tfidf_matrix.append(tfidf)
    
#convert the dict of tdidf values into an array
#the array currently represents the words as rows
#and
x = np.asarray(tfidf_matrix, dtype=)
x = np.transpose(x)