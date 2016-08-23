# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:05:46 2016

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
#what are we changing to change the readability?
    #if Noun score is low, will we change Nouns to be less difficult?
    #if Verb score is high, will we change Verbs to give a challenge?

#take word and pos_tag, find verbs, if there's a adverb in front of the verb\\
# find a synonym for the adverb *can you assess difficulty of adverb

#could I use my previous code to determine the difficulty of the adverb\\
# reduce list of synonyms to a list whose score is greater than the adverb's score
# pick random word from reduced list
#       could have a safety where the average value of new words can only be a limited\\
#        amount greater than the average value of the whole book before hand. 
#        increase difficulty of book in 1/2 increments or .2 increments

#   if decreasing difficulty first assess difficulty of current adverb. If at lowest\\
#    difficulty remove adverb all together
#for inserting adverbs (embellishments) need to determine the tone of the sentence
    #ex: determine if sentence is negative/positive, important/unimportant to determine what word to insert
        # need to determine tone of words


#what if the word is too hard?
#   

#deconstructing the text into sentences and words --> need to reconstruct


from nltk.corpus import wordnet as wn

#for synonyms:
#print wn.synsets('word')

#if want similar to also call \\
# similar_tos()
'''for ss in wn.synsets('trying'):
    print (ss)
    for sim in ss.similar_tos():
        print('    {}'.format(sim))
'''
        
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
        
    
def random_syn(current_word):
    """
    Takes a word found in a sentence, searches for it's synonyms and chooses
    one of those synonyms randomly to eventually replace that word
    
    WARNING: needs checks for word level and apporopriate usage
    """
    syn_list = []
    #puts synonmyms from synsets and similar sets into a list
    for ss in wn.synsets(current_word):
        syn_list.append(str(ss.name().split(".")[0]))
        #print '\n','\n'
        for sim in ss.similar_tos():
            #print sim.name().split(".")[0]
            syn_list.append(str(sim.name().split(".")[0]))
            #print sim.name().split(".")[0]
    #print syn_list
    #removes duplicates
    y = set(syn_list)
    #print y
    z = list(y)
    #print z 
    syn_list = z[:]
    #print syn_list
    if len(syn_list) == 0:
        syn_choice = None
    else:
        syn_choice = random.choice(syn_list)
    return syn_choice 
    

#tokenizer
f = open("./Maxs_Pet_copy.txt")
raw = f.read()


final_words = []
word_sent_token = []
pos_tag_sent_list = []
lem_ready_word_list = []
sent_dict = {}

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
        #makes words lowercase
        word = word.lower()
        lem_ready_word_list.append((word, pos_tag))
        
sent_object_list = []

#iterates through sentence    
sent_count = 0
#matches sentence to its tokenized parts
for sent in sent_tokenize_list:
    sent_count += 1
    word_sent_count = 0
    for word_sent in pos_tag_sent_list:
        word_sent_count += 1
        if sent_count == word_sent_count:
            sent_dict[sent] = word_sent
            break

for sent in sent_dict:
    y = []
    for tuple_pair in sent_dict[sent]:
        word = tuple_pair[0]
        pos_tag = tuple_pair[1]
        #makes each word into a word object
        new_word = Word(word, pos_tag)
        #print new_word.get_word()
        y.append(word)
    #makes each sentence into a sentence object
    new_sent = Sentence(sent, word)
    sent_object_list.append(new_sent)

for sent in sent_object_list:
    print sent.get_sentence()
    
#print len(sent_tokenize_list)
#print sent_tokenize_list
#print pos_tag_sent_list
#print lem_ready_word_list
#print final_words

'''
f = open("./StoryCorpus_copy/Left_Right_Emma.txt")
raw = f.read()
'''


       #finds Verb/Adverb pairs and chooses a synonym to replace the adverb
#        if sent.get_words()[i].get_pos_tag() == 'RB':
#            pass
word_list = []



#figuring out how to work with synsets and object oriented programming
for sent in sent_object_list:
    #print sent.get_sentence()
    for word in sent.get_words():
        #print word.get_word()
        if word.get_pos_tag() == 'ADV':
            print "adverb here!"
#        for ss in wn.synsets(words_list.get_word()):
#            print (ss)
#            for sim in ss.similar_tos():
#                print('    {}'.format(sim))




#to replace adverbs with synonyms


for sent in sent_object_list:
    #print "NEW SENTENCE"
    #print "\n"
    #iterates through the indecies of the word list in each sentence object
    for i in range(1,(len(sent.get_words())-1)):
        current_word = sent.get_words()[i].get_word()
        #print "First Word" 
        #print current_word
        prev_word = sent.get_words()[i-1].get_word()
        next_word = sent.get_words()[i+1].get_word()
        #finds Verb/Adverb pairs and chooses a synonym to replace the adverb
        if sent.get_words()[i].get_pos_tag() == 'RB':
            if sent.get_words()[i+1].get_pos_tag() == 'VBD':
                print "Found a pair: ", current_word, " ", next_word
                print "\n"
                syn_choice = random_syn(current_word)
                if syn_choice == None:
                    syn_choice = current_word
                print syn_choice
                
                
            if sent.get_words()[i-1].get_pos_tag() == 'VBD':
                print "Found a pair: ", prev_word, " ", current_word
                print "\n"
                syn_choice = random_syn(current_word)
                if syn_choice == None:
                    syn_choice = current_word
                print syn_choice
            sent.get_words()[i].set_word(syn_choice)
            #print "Synonym"
            #print sent.get_words()[i].get_word()
            #print '\n'

    
