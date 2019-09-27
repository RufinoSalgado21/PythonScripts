# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:10:41 2019

@author: RufinoS
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
from nltk.corpus import stopwords

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
               
#tokenize sentences and words
sentences = nltk.sent_tokenize(paragraph)

sentences

words = nltk.word_tokenize(paragraph)

#stemming text
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    new_words = [stemmer.stem(word) for word in words]
    sentences[i] = ' '.join(new_words)
#loop through list of sentences
#for each word in each sentence, stem the word
#join all the words into a sentence again

#create lemmatizer object
#for each word in each sentence, find lemmatizer
sentences2 = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()
for i in range(len(sentences2)):
    words = nltk.word_tokenize(sentences2[i])
    new_words = [lemmatizer.lemmatize(word) for word in words]
    sentences2[i] = ' '.join(new_words)
    
#remove stop words from paragraph
sentences3 = nltk.sent_tokenize(paragraph)
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences3[i])
    new_words = [word for word in words if word not in stopwords.words(
            'english')]
    sentences3[i] = ' '.join(new_words)
    
#parts of speech tagging
words = nltk.word_tokenize(paragraph)
tagged_words = nltk.pos_tag(words)
word_tags = []
for tw in tagged_words:
    word_tags.append(tw[0]+"_"+tw[1])
    
    
#named entity recognition
#searches for words representing objects, places, names, organizations etc. 
#basically nouns
named_ents = nltk.ne_chunk(tagged_words)
named_ents.draw()



    