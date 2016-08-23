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
'''
Brown's Rules for counting morphemes:

'''

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
        
    def get_lem_word(self):
        return self.lem_word
        
    def set_lem_word(self, new_lem_word):
        self.lem_word = new_lem_word
        #if len(lem_word) > len(word):
            #morpheme_count += 2
    
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
'''

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
        

    
sent_count = 0
for sent in sent_tokenize_list:
    sent_count += 1
    word_sent_count = 0
    for word_sent in pos_tag_sent_list:
        word_sent_count += 1
        if sent_count == word_sent_count:
            sent_dict[sent] = word_sent
            break

for sent in sent_dict:
    for tuple_pair in sent_dict[sent]:
        y = []
        word = tuple_pair[0]
        pos_tag = tuple_pair[1]
        word.Word(word, pos_tag)
        print word
        #y.append(word)
    sent.Sentence(sent, word)





#print len(sent_tokenize_list)
#print sent_tokenize_list
#print pos_tag_sent_list
#print lem_ready_word_list
print final_words
'''
'''
f = open("./StoryCorpus_copy/Left_Right_Emma.txt")
raw = f.read()
'''
#Mean Length Utterance (MLU) calculator
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
    #print "POS_TAG"    
    #print pos_tag_sent_list
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
    for sent in sent_tokenize_list:
        sent_count += 1
        word_sent_count = 0
        for word_sent in mlu_ready_list:
            word_sent_count += 1
            if sent_count == word_sent_count:
                sent_dict[sent] = word_sent
                break
    '''   
        for word_sent in pos_tag_sent_list:
            word_sent_count += 1
            if sent_count == word_sent_count:
                sent_dict[sent] = word_sent
                break
    '''
    
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
        #print "NEW SENTENCE"
        #print "\n"
        #iterates through the indecies of the word list in each sentence object
        for i in range(1,(len(sent.get_words())-1)):
            current_word = sent.get_words()[i].get_word()
            prev_word = sent.get_words()[i-1].get_word()
            next_word = sent.get_words()[i+1].get_word()
            if i == 1:
                #print current_word
                #print sent.get_words()[i-1].get
                #print sent.get_words[i-1]
                if prev_word in ('=======', '<', '>'):
                    morpheme_count = morpheme_count
                    #print prev_word, sent.get_words()[i-1].get_pos_tag()
                elif sent.get_words()[i-1].get_pos_tag() == 'NNS':
                    if prev_word == "pants" or prev_word == "clothes":
                        #print "found pants or clothes"
                        morpheme_count += 1
                        morpheme1_list.append(prev_word)
                    else:
                        NNS_list.append(prev_word)
                        #print 'found NNS'
                        morpheme_count += 2
                elif sent.get_words()[i-1].get_pos_tag() == 'VBZ':
                    if prev_word != 'does'and sent.get_words()[i-1].get_lem_word() != 'be':
                        VBZ_list.append(prev_word)
                        #print 'found VBZ'
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
                #elif sent.get_words()[i-1].get_pos_tag() in ('.', ',', '``',"''", ':', '-'):
                    #pass
                    #print prev_word, sent.get_words()[i-1].get_pos_tag()
                elif sent.get_words()[i-1].get_pos_tag() not in ('.', ',', '``',"''", ':', '-'):
                    morpheme_count += 1
                    morpheme1_list.append(prev_word)
                #else:
                    #print "No points for you!!!!", prev_word
            else:
                if current_word in ('=======', '<', '>'):
                    morpheme_count = morpheme_count
                    #print current_word, sent.get_words()[i].get_pos_tag()
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
                        #print "found pants or clothes"
                        morpheme_count += 1
                        morpheme1_list.append(current_word)
                    else:
                        #print 'found NNS'
                        NNS_list.append(current_word)
                        morpheme_count += 2
                elif sent.get_words()[i].get_pos_tag() == 'VBZ':
                    if current_word != 'does'and sent.get_words()[i].get_lem_word() != 'be':
                        #print 'found VBZ'
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
                        #print current_word
                        VBDN_list.append(current_word)
                        morpheme_count += 2
                    else:
                        morpheme_count += 1
                        morpheme1_list.append(current_word)
                elif sent.get_words()[i].get_pos_tag() == 'VBG':
                    if current_word[-3:] == 'ing':
                        #print current_word
                        morpheme_count += 2
                        VBG_list.append(current_word)
                    else:
                        morpheme_count += 1
                        morpheme1_list.append(current_word)
                    #print current_word, sent.get_words()[i].get_pos_tag()
                #elif sent.get_words()[i].get_pos_tag() in ('.', ',', '``',"''", ':', '-'):
                    #pass
                    #print current_word, sent.get_words()[i].get_pos_tag()
                elif sent.get_words()[i].get_pos_tag() not in ('.', ',', '``',"''", ':', '-'):
                    morpheme_count += 1
                    morpheme1_list.append(current_word)
                #else:
                    #print "No points for you!!!!", current_word
    MLU_dict[fileName] = (morpheme_count, sent_count, float(morpheme_count)/sent_count)

ordered_list = []

for book in MLU_dict:
    book_name = book[32:-4]
    if book_name == "The_Bat":#the bat is here!
        print book_name
    morpheme_count, sent_count, MLU = MLU_dict[book]
    tuple_count = 0
    first_book = False
    if len(ordered_list) == 0:
        first_book = True
        ordered_list.append((book, MLU))
    for tuple_pair in ordered_list:
        temp_list = []
        if first_book == True:
            break
        tuple_count += 1
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


#print book_tot_modify_read.book_tot_modify('./resources/converted/StoryCorpus/*.txt')
#creating categories
#WARNING!!! NOT WORKING YET
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

#NOT WORKING!!! returns all empty lists

'''
#prints information related to MLU's
for book in MLU_dict:
    morpheme_count, sent_count, MLU = MLU_dict[book]
    print book[32:-4]
    print "Morphemes: ", morpheme_count
    print "Sentences: ", sent_count
    print "MLU: ", MLU
    print '\n'
    
            
print "Morpheme1: ", morpheme1_list
#getting punctuation and '>', '<'
print "Plural nouns: "
print NNS_list
#getting '======='
'''

                    
            
                    
        #finds Verb/Adverb pairs and chooses a synonym to replace the adverb
#        if sent.get_words()[i].get_pos_tag() == 'RB':
#            pass
word_list = []


'''
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
'''


'''
#to replace adverbs with synonyms


for sent in sent_object_list:
    #print "NEW SENTENCE"
    #print "\n"
    #iterates through the indecies of the word list in each sentence object
    for i in range(1,(len(sent.get_words())-1)):
        current_word = sent.get_words()[i].get_word()
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
'''