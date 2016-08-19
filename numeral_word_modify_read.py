# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:29:12 2016

@author: Madelyn
"""

#final_words = ['cool', '4']
#final_words = ['just', 'four', 'fishing', 'go', 'to', 'black', '4', '8', 'them', 'big', 'fat', 'five', 'they', '2', 'now', 'like', 'red', 'twelve', 'right', 'ten', 'fish', 'jump', 'see', 'catching', 'bark', 'what', '3', '7', 'three', 'do', 'water', 'along', 'come', 'on', 'greet', 'swimming', 'one', 'twin', 'another', 'boat', 'little', 'two', 'splash', 'too', '6', 'raft', 'white', 'more', 'catch', '11', '10', '12', 'look', 'can', 'meet', 'and', 'seven', 'brown', 'dog', 'at', 'want', 'in', 'scar', 'dozen', 'dotted', 'no', '1', 'hot', '5', '9', 'puppy', 'beach', 'dive', 'spot', 'eight', 'whale', 'skinny', 'a', 'hungry', 'together', 'the', 'bowwow', 'yaketyyak', 'doggypaddle']

#up to 20 

def num_modify(final_words):
    numeral_word_map = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',\
    '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven',\
    '12': 'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen',\
    '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen',\
    '20':'twenty'}

    final_words_modify = final_words [:]
    
    for word in final_words:
        if len(word) > 20:
            final_words_modify.remove(word)
        key_count = 0
        for key in numeral_word_map:
            key_count += 1
            if word == key:
                final_words_modify.append(numeral_word_map[key])
                final_words_modify.remove(word)
            elif key_count == len(numeral_word_map):
                break
                
    return final_words_modify
    
#final_words_modify = num_modify(final_words)
#print final_words_modify