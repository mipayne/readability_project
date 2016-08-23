# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:00:50 2016

@author: Madelyn
"""
from __future__ import division
import nltk
from nltk import sent_tokenize, word_tokenize, WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet
from unidecode import unidecode
import collections
import random
import book_tot_modify_read


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
class Sentence(object):
    """A sentence in a book"""
    def __init__(self, sentence, words):
        """sentence is the sentence taken from a list of sentences
        words are a list of word objects
        """
        self.sentence = sentence
        self.words = words
        
    def get_sentence(self):
        return self.sentence
        
    def get_words(self):
        return self.words

class Word(object):
    """A word in a sentence.
    
    Attributes:
    original word
    pos_tag
    """
    def __init__(self, word, lem_word, pos_tag):
        self.word = word
        self.pos_tag = pos_tag
        self.lem_word = lem_word
    def get_word(self):
        return self.word
    
    def set_word(self, new_word):
        self.word = new_word
        
    def get_pos_tag(self):
        return self.pos_tag
        
    def set_pos_tag(self, new_pos_tag):
        self.pos_tag = new_pos_tag
        
    def get_lem_word(self):
        return self.lem_word
        
    def set_lem_word(self, new_lem_word):
        self.lem_word = new_lem_word
        
'''
f = open("./StoryCorpus_copy/Left_Right_Emma.txt")
raw = f.read()
'''

#Mean Length Utterance (MLU) calculator and orderer
#uses (lines 214-310) and (lines 398-685)
    #Morpheme counting rules from --> http://www.sltinfo.com/mean-length-of-utterance/
        #according to these rules should have 100 sentences (these books to don't have that many words)
import glob
list_of_files = glob.glob('./resources/converted/StoryCorpus/*.txt')

MLU_dict = {}

morpheme1_list = []
VBDN_list = []
NNS_list = []
VBN_list = []
VBD_list = []
VBZ_list = []
VBG_list = []
POS_list = []
WP_list = []
be_list = []
#mlu_ready_list = []
#morpheme_count = 0
#sent_count = 0

for fileName in list_of_files:
    f = open(fileName)
    raw = f.read()

    final_words = []
    word_sent_token = []
    pos_tag_sent_list = []
    lem_ready_sent_list = []
    mlu_ready_list = []
    sent_dict = collections.OrderedDict()
    #tokenize
    sent_tokenize_list = sent_tokenize(raw)#breaks raw text into list of its sentences
    #breaks each sentence into a  list of its parts
    for sent in sent_tokenize_list:
        word_sent_token.append(word_tokenize(sent))# DOWNSIDE: breaks up contractions\
    #creates list of tuples for each part of each sentence (word, pos_tag) 
    for sent in word_sent_token:
        pos_tag_sent_list.append(nltk.pos_tag(sent))
    '''
    #pos_tag
    for sent in pos_tag_sent_list:
        #pos_tag_sent_list is a list of lists
            #list_outside = sentences
            #list_inside = (word,pos_tag)
        for tuple_pair in sent:
            word = tuple_pair[0]
            pos_tag = tuple_pair[1]
            #makes words lowercase
            word = word.lower()
            lem_ready_word_list.append((word, pos_tag))
    print 'LEM_READY'
    print lem_ready_word_list
    '''
     #pos_tag
    for sent in pos_tag_sent_list:
        lem_ready_word_list = []
        for tuple_pair in sent:
            word = tuple_pair[0]
            pos_tag = tuple_pair[1]
            #gives correct pos_tag
            wordnet_pos = get_wordnet_pos(pos_tag)
            #makes words lowercase
            word = word.lower()
            lem_ready_word_list.append((word, wordnet_pos, pos_tag))
        lem_ready_sent_list.append(lem_ready_word_list)
    #print lem_ready_sent_list
            
     #lemmatize
    for sent in lem_ready_sent_list:
        lem_sent = []
        for tuple_trip in sent:
            word = tuple_trip[0]
            wordnet_pos = tuple_trip[1]
            pos_tag = tuple_trip[2]
            #makes sure words with no equivalent wordnet pos_tag still get lemmatized
            if wordnet_pos == '':
                lem_word = wordnet_lemmatizer.lemmatize(word)
                if type(lem_word) == unicode:
                    lem_word = unidecode(lem_word)
                lem_sent.append((word, lem_word, pos_tag))
                #final_words.append((lem_word, pos_tag))
            
                #insert code to assign tags according to WordCategories.xlsx (ex: negatives, pronoun)
        #general lemmatization
            else:
                lem_word = wordnet_lemmatizer.lemmatize(word, pos=wordnet_pos)
                if type(lem_word) == unicode:
                    lem_word = unidecode(lem_word)
                lem_sent.append((word, lem_word, pos_tag))
                #final_words.append((lem_word, pos_tag))
        mlu_ready_list.append(lem_sent)
    #print mlu_ready_list
    
    sent_object_list = []
    
    #iterates through sentence    
    sent_count = 0
    #matches sentence to its tokenized parts
    for sent in sent_tokenize_list:
        sent_count += 1
        word_sent_count = 0
        for word_sent in mlu_ready_list:
            word_sent_count += 1
            if sent_count == word_sent_count:
                sent_dict[sent] = word_sent
                break
    
    for sent in sent_dict:
        y = []
        for tuple_trip in sent_dict[sent]:
            word = tuple_trip[0]
            lem_word = tuple_trip[1]
            pos_tag = tuple_trip[2]
            #makes each word into a word object
            new_word = Word(word, lem_word, pos_tag)
            #print new_word.get_word()
            y.append(new_word)
        #makes each sentence into a sentence object
        new_sent = Sentence(sent, y)
        sent_object_list.append(new_sent)
    
    #for sent in sent_object_list:
        #print sent.get_sentence()

    
    morpheme_count = 0
    sent_count = 0
    for sent in sent_object_list:
        sent_count += 1
        #iterates through the indecies of the word list in each sentence object
        for i in range(1,(len(sent.get_words())-1)):
            current_word = sent.get_words()[i].get_word()
            prev_word = sent.get_words()[i-1].get_word()
            next_word = sent.get_words()[i+1].get_word()
            #searches for special instances to count morphemes in very first word
            if i == 1:
                #weird characters don't count as morphemes
                if prev_word in ('=======', '<', '>'):
                    morpheme_count = morpheme_count
                elif sent.get_words()[i-1].get_pos_tag() == 'NNS':
                    if prev_word == "pants" or prev_word == "clothes":
                        morpheme_count += 1
                        morpheme1_list.append(prev_word)
                    else:
                        NNS_list.append(prev_word)
                        morpheme_count += 2
                elif sent.get_words()[i-1].get_pos_tag() == 'VBZ':
                    if prev_word != 'does'and sent.get_words()[i-1].get_lem_word() != 'be':
                        VBZ_list.append(prev_word)
                        morpheme_count += 2
                    else:
                        morpheme1_list.append(prev_word)
                        morpheme_count += 1
                elif sent.get_words()[i-1].get_pos_tag() == ('VBD' or 'VBN'):
                    if sent.get_words()[i-1].get_lem_word() == 'be':
                        morpheme_count += 1
                        morpheme1_list.append(prev_word)
                    elif prev_word[-2:] =='ed':
                        VBDN_list.append(prev_word)
                        morpheme_count += 2
                    else:
                        morpheme1_list.append(prev_word)
                        morpheme_count += 1
                elif sent.get_words()[i-1].get_pos_tag() == 'VBG':
                    if prev_word[-3:] == 'ing':
                        VBG_list.append(prev_word)
                        morpheme_count += 2
                    else:
                        morpheme1_list.append(prev_word)
                        morpheme_count += 1
                #pucntuation does not count as morphemes
                elif sent.get_words()[i-1].get_pos_tag() not in ('.', ',', '``',"''", ':', '-'):
                    morpheme_count += 1
                    morpheme1_list.append(prev_word)
                    
            #searches for special instances to count morphemes
            else:
                if current_word in ('=======', '<', '>'):
                    morpheme_count = morpheme_count
                elif sent.get_words()[i].get_pos_tag() == 'POS':
                    if current_word == "'s":
                        if prev_word != 'let':
                            morpheme1_list.append(current_word)
                            morpheme_count += 1
                elif current_word == "'t":
                    if prev_word != ("don" and "won"):
                        morpheme_count += 1
                        morpheme1_list.append(current_word)
                elif sent.get_words()[i].get_pos_tag() == 'NNS':
                    if current_word == "pants" or current_word == "clothes":
                        morpheme_count += 1
                        morpheme1_list.append(current_word)
                    else:
                        NNS_list.append(current_word)
                        morpheme_count += 2
                elif sent.get_words()[i].get_pos_tag() == 'VBZ':
                    if current_word != 'does'and sent.get_words()[i].get_lem_word() != 'be':
                        VBZ_list.append(current_word)
                        morpheme_count += 2
                    else:
                        morpheme_count += 1
                        morpheme1_list.append(current_word)
                elif sent.get_words()[i].get_pos_tag() == ('VBD' or 'VBN'):
                    if sent.get_words()[i].get_lem_word() == 'be':
                        morpheme_count += 1
                        morpheme1_list.append(current_word)
                    elif current_word[-2:] =='ed':
                        VBDN_list.append(current_word)
                        morpheme_count += 2
                    else:
                        morpheme_count += 1
                        morpheme1_list.append(current_word)
                elif sent.get_words()[i].get_pos_tag() == 'VBG':
                    if current_word[-3:] == 'ing':
                        morpheme_count += 2
                        VBG_list.append(current_word)
                    else:
                        morpheme_count += 1
                        morpheme1_list.append(current_word)
                elif sent.get_words()[i].get_pos_tag() not in ('.', ',', '``',"''", ':', '-'):
                    morpheme_count += 1
                    morpheme1_list.append(current_word)
    MLU_dict[fileName] = (morpheme_count, sent_count, float(morpheme_count)/sent_count)

ordered_list = []

for book in MLU_dict:
    book_name = book[32:-4]
    morpheme_count, sent_count, MLU = MLU_dict[book]
    tuple_count = 0
    first_book = False
    #first book check
    if len(ordered_list) == 0:
        first_book = True
        ordered_list.append((book, MLU))
    for tuple_pair in ordered_list:
        temp_list = []
        if first_book == True:
            break
        tuple_count += 1
        #order books by decreasing MLU score
        if MLU > tuple_pair[1]:
            temp_list = ordered_list[:(tuple_count-1)]
            temp_list.append((book, MLU))
            temp_list.extend(ordered_list[(tuple_count-1):])
            ordered_list = temp_list[:]
            break
        elif tuple_count == len(ordered_list):
            ordered_list.append((book, MLU))
            break
#print ordered_list

            
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])
    
MLU10up = []
MLUunder1 = []
MLU1 = []
MLU2 = []
MLU3 = []
MLU4 = []
MLU5 = []
MLU6 = []
MLU7 = []
MLU8 = []
MLU9 = []
  
book_count = 0
for book in ordered_list:
    number = truncate(book[1],0)
    if len(number) > 2:
        MLU10up.append(book)
    elif number[0] == '0':
        #print book
        MLUunder1.append(book)
    elif number[0] == '1':
        MLU1.append(book)
    elif number[0] == '2':
        MLU2.append(book)
    elif number[0] == '3':
        MLU3.append(book)
    elif number[0] == '4':
        MLU4.append(book)
    elif number[0] == '5':
        MLU5.append(book)
    elif number[0] == '6':
        MLU6.append(book)
    elif number[0] == '7':
        MLU7.append(book)
    elif number[0] == '8':
        MLU8.append(book)
    elif number[0] == '9':
        MLU9.append(book)
'''        
print MLU1 
print MLU2
print MLU3 
print MLU4 
print MLU5 
print MLU6 
print MLU7 
print MLU8
print MLU9 
print MLU10up        
'''



#creating categories
modified_book_words = book_tot_modify_read.book_tot_modify('./resources/converted/StoryCorpus/*.txt')
MLU1_words = []
MLU2_words = []
MLU3_words = []
MLU4_words = []
MLU5_words = []
MLU6_words = []
MLU7_words = []
MLU8_words = []
MLU9_words = []
MLU10up_words = []

#matches books that were ordered into MLUbooks with the books in modified_book_words list\
    #in order to collect words found each MLU category, hoping it would reveal a general
    #upward trend of word difficulty with increasing MLU Score (IT DOES NOT SHOW A TREND\
    #LIKE THAT)
for book in modified_book_words:
    final_words_modify3, final_words_modify4 = modified_book_words[book]
    for MLU1book in MLU1:
        if book == MLU1book[0]:
            MLU1_words.append(final_words_modify4)
    for MLU2book in MLU2:
        if book == MLU2book[0]:
            for word in final_words_modify4:
                if word not in MLU1_words:
                    MLU2_words.append(word)
    for MLU3book in MLU3:
        if book == MLU3book[0]:
            for word in final_words_modify4:
                if word not in (MLU1_words and MLU2_words):
                    MLU3_words.append(word)
    for MLU4book in MLU4:
        if book == MLU4book[0]:
            for word in final_words_modify4:
                if word not in (MLU1_words and MLU2_words and MLU3_words):
                    MLU4_words.append(word)
    for MLU5book in MLU5:
        if book == MLU5book[0]:
            for word in final_words_modify4:
                if word not in (MLU1_words and MLU2_words and MLU3_words and MLU4_words):
                    MLU5_words.append(word)
    for MLU6book in MLU6:
        if book == MLU6book[0]:
            for word in final_words_modify4:
                if word not in (MLU1_words and MLU2_words and MLU3_words and MLU4_words and MLU5_words):
                    MLU6_words.append(word)
    for MLU7book in MLU7:
        if book == MLU7book[0]:
            for word in final_words_modify4:
                if word not in (MLU1_words and MLU2_words and MLU3_words and \
                    MLU4_words and MLU5_words and MLU6_words):
                    MLU7_words.append(word)
    for MLU8book in MLU8:
        if book == MLU8book[0]:
            for word in final_words_modify4:
                if word not in (MLU1_words and MLU2_words and MLU3_words and \
                    MLU4_words and MLU5_words and MLU6_words and MLU7_words):
                    MLU8_words.append(word)
    for MLU9book in MLU9:
        if book == MLU9book[0]:
            for word in final_words_modify4:
                if word not in (MLU1_words and MLU2_words and MLU3_words and \
                    MLU4_words and MLU5_words and MLU6_words and MLU7_words\
                    and MLU8_words):
                    MLU9_words.append(word)
    for MLU10upbook in MLU10up:
        if book == MLU10upbook[0]:
            for word in final_words_modify4:
                if word not in (MLU1_words and MLU2_words and MLU3_words and \
                    MLU4_words and MLU5_words and MLU6_words and MLU7_words\
                    and MLU8_words and MLU9_words):
                    MLU10up_words.append(word)
                    
#works but doesn't give useful results. The lists don't have progressively harder words.\
#   this will not work as a basis to level up and down synonyms
'''
#prints MLU words                    
print MLU1_words
print MLU2_words
print MLU3_words
print MLU4_words    
print MLU5_words
print MLU6_words
print MLU7_words
print MLU8_words
print MLU9_words
print MLU10up_words
'''
'''
#prints information related to MLU's
for book in MLU_dict:
    morpheme_count, sent_count, MLU = MLU_dict[book]
    print book[32:-4]
    print "Morphemes: ", morpheme_count
    print "Sentences: ", sent_count
    print "MLU: ", MLU
    print '\n'
'''