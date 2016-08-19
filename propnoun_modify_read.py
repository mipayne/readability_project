# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 10:21:51 2016

@author: Madelyn
"""
#NOT USED
#NOT USED
#NOT USED
#TOO MANY PROPER PRONOUNS ARE ALSO ON THE WORDCATEGORIES.XLSX SHEET
from __future__ import division
import nltk
from nltk import sent_tokenize, word_tokenize, WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet
from unidecode import unidecode

        
f = open('./resources/converted/StoryCorpus/Hen_Pens_Joke.txt')
raw = f.read()        
#print raw
final_words = []
word_sent_token = []
pos_tag_sent_list = []
lem_ready_word_list = []


#tokenize
sent_tokenize_list = sent_tokenize(raw)#breaks raw text into list of its sentences
#breaks each sentence into a  list of its parts
for sent in sent_tokenize_list:
    word_sent_token.append(word_tokenize(sent))# DOWNSIDE: breaks up contractions\
#creates list of tuples for each part of each sentence (word, pos_tag) 
for sent in word_sent_token:
    pos_tag_sent_list.append(nltk.pos_tag(sent))

propernouns=[]
for sent in pos_tag_sent_list:
    for tuple_pair in sent:
        word = tuple_pair[0] 
        pos_tag = tuple_pair[1]
        #print tuple_pair
        #print pos_tag
        if pos_tag == 'NNP':
            #print 'hi'
            propernouns.append(word)
    #propernouns = [word for word,pos in pos_tag_sent_list if pos == 'NNP']
#print propernouns

# list_of_files = glob.glob('./resources/converted/StoryCorpus/*.txt')
#    
#    final_words = []
#    book_words = {}
#    
#    for fileName in list_of_files:
#        f = open( fileName)
#        raw = f.read()
#        
#        
#        final_words = []
#        word_sent_token = []
#        pos_tag_sent_list = []
#        lem_ready_word_list = []
    