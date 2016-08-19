# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:58:12 2016

@author: Madelyn
"""
#final_words = ["san", "francisco", "new", "york", "do", "n't", "we", "'ll", 'please', '.', 'it', "'s"]


check_word_list = ["what's", "it's", "i'm", "you've", "you'll", \
    "i've", "he'd", "he's", "we'll", "you're", "i'll", "don't", \
    "wouldn't", "wasn't", "isn't", "won't", "didn't", "doesn't",\
    "can't", "couldn't", 'san francisco', 'new york', ' cool', "let's", \
    "don't", "wouldn't", "wasn't", "isn't", "won't", "didn't", "doesn't",\
    "can't", "couldn't", 'act- e', 'arrive ', 'sent  ']
#check_word_list = set(check_word_list)

contraction_list = ["what's", "it's", "i'm", "you've", "you'll",\
    "i've", "he'd", "he's", "we'll", "you're", "i'll", "don't", \
    "wouldn't", "wasn't", "isn't", "won't", "didn't", "doesn't",\
    "can't", "couldn't", "let's", "don't", "wouldn't", "wasn't",\
    "isn't", "won't", "didn't", "doesn't", "can't", "couldn't"]

#contraction_list = set(contraction_list)

def string_modify(final_words):
    '''
    concatenates parts of contractions into 1 word, removes halves from\
    and adds whole contractions to final_words list
    
    Inputs: word list
    Outputs: modified word list
    '''
    cntrc_mapping_dict = {'you':["'ve","'ll","'re"], 'would':["n't"],\
        'wo':["n't"], 'what':["'s"], 'we':["'ll"], 'was':["n't"], 'let':["'s"],\
        'it': ["'s"], 'is': ["n't"], 'i':["'ve","'m","'ll"], 'he':["'s","'d"],\
        'do':["n't"], 'does':["n't"], 'did':["n't"],'could':["n't"],'ca':["n't"]}
        
    new_words = []
    final_words_modify = final_words[:]
                
    for i in range(len(final_words)):
        if i < (len(final_words) - 1):#avoid index error for last word's next_word
            current_word = final_words[i]
            next_word = final_words[i+1]
            #searches cntrc_mapping_dict for half of contraction, if ending to\
            #   that contraction is a value to its key, concatenates them
            if current_word in cntrc_mapping_dict.keys():
                for key in cntrc_mapping_dict:
                    if current_word == key:
                        for ending in cntrc_mapping_dict[key]:
                            if next_word == ending:
                                new_word = current_word + next_word
                                new_words.append(new_word)
                                final_words_modify.remove(current_word)
                                final_words_modify.remove(next_word)
            #allows exception of specific two word proper names
            elif current_word == 'san':
                if next_word == 'francisco':
                    new_word = current_word + ' ' + next_word
                    new_words.append(new_word)
                    final_words_modify.remove(current_word)
                    final_words_modify.remove(next_word)
            elif current_word == 'new':
                if next_word == 'york':
                    new_word = current_word + ' ' + next_word
                    new_words.append(new_word)
                    final_words_modify.remove(current_word)
                    final_words_modify.remove(next_word)
        else: 
            break
        
    
    final_words_modify.extend(new_words)
    return final_words_modify

#final_words_modify = string_modify(final_words)
#print final_words_modify


#remove duplicates
#apply custom_stopwords
#remove punctuation (without removing words with dashes and apostrophes)
