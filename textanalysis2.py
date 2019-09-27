# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:21:31 2019

@author: RufinoS
"""
import nltk
import random

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

n=3

ngrams= {}

for i in range(len(text) - n):
    gram = text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n])
    
current_gram = text[0:n]
result = current_gram
for i in range(100):
    if current_gram not in ngrams.keys():
        break
    possibilities = ngrams[current_gram]
    nextitem = possibilities[random.randrange(len(possibilities))]
    result += nextitem
    current_gram = result[len(result)-n : len(result)]
    
print(result)

ngrams = {}
words = nltk.word_tokenize(text)

for i in range(len(words) - n):
    gram = ' '.join(words [i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[i+n])
    
currentGram = ' '.join(words[0:n])
result2 = currentGram
for i in range(30):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result2 += " " + nextItem
    rwords = nltk.word_tokenize(result2)
    currentGram = ' '.join(rwords[len(rwords)-n: len(rwords)])
    
print(result2)