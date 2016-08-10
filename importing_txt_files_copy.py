# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 16:28:20 2016

@author: Madelyn
"""
from __future__ import division
import nltk
from nltk import sent_tokenize, word_tokenize, WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet
from unidecode import unidecode

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''
        
import glob

def import_txt(multiple_txts):
    '''
    tokenize, pos_tag, and lemmatize words from files in StoryCorpus
    Returns: book_words, a dictionary s.t. book_words[fileName] = list
    '''
    list_of_files = glob.glob(multiple_txts)
    
    final_words = []
    book_words = {}
    
    for fileName in list_of_files:
        f = open( fileName)
        raw = f.read()
        
        
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
        #pos_tag
        for sent in pos_tag_sent_list:
            for tuple_pair in sent:
                word = tuple_pair[0]
                pos_tag = tuple_pair[1]
                #gives correct pos_tag
                wordnet_pos = get_wordnet_pos(pos_tag)
                #makes words lowercase
                word = word.lower()
                lem_ready_word_list.append((word, wordnet_pos, pos_tag))
        
        #lemmatize
        for tuple_pair in lem_ready_word_list:
            word = tuple_pair[0]
            wordnet_pos = tuple_pair[1]
            pos_tag = tuple_pair[2]
            #makes sure words with no equivalent wordnet pos_tag still get lemmatized
            if wordnet_pos == '':
                lem_word = wordnet_lemmatizer.lemmatize(word)
                if type(lem_word) == unicode:
                    lem_word = unidecode(lem_word)
                final_words.append((lem_word, pos_tag))
                
                    #insert code to assign tags according to WordCategories.xlsx (ex: negatives, pronoun)
            #general lemmatization
            else:
                lem_word = wordnet_lemmatizer.lemmatize(word, pos=wordnet_pos)
                if type(lem_word) == unicode:
                    lem_word = unidecode(lem_word)
                final_words.append((lem_word, pos_tag))
                
        
        book_words[fileName] = final_words
        


    #print len(sent_tokenize_list)
    #print sent_tokenize_list
    #print pos_tag_sent_list
    #print lem_ready_word_list
    #print final_words
    
    return (book_words)
    