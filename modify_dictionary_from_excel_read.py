# -*- coding: utf-8 -*-

"""
Created on Wed Jun 22 16:00:43 2016

@author: Madelyn
"""
import pyexcel
'''
#for original book_values.py
sheet_list = []

from pyexcel.cookbook import split_a_book
split_a_book('./resources/WordCategories.xlsx', 'output.xlsx')
import glob
outputfiles = glob.glob('*_output.xlsx')#splits book to be single sheets
for file in sorted(outputfiles):
    sheet_list.append(file)#adds each new sheet to a list
'''
#for Book_values_w_book_tot_modify
sheet_list = []

sheet_list.append('./resources/All_output.xlsx')
sheet_list.append('./resources/Easy_output.xlsx')

def create_dictionary(sheet_list):
    '''
    creates allsheet_dict and ezsheet_dict
    '''

    for i in sheet_list:
        if i == './resources/All_output.xlsx':
            allsheet = pyexcel.get_sheet(file_name = sheet_list[0], name_columns_by_row=0)
            allsheet_od = allsheet.to_dict()#makes ordered dict
            allsheet_dict = dict(allsheet_od)#makes ordinary dict
            #print "ALL: ",allsheet_dict
        elif i == './resources/Easy_output.xlsx':
            ezsheet = pyexcel.get_sheet(file_name = sheet_list[1], name_columns_by_row=0)
            ezsheet_dict = dict(ezsheet.to_dict())
            #print "EZ: ",ezsheet_dict
        else:
            print "You don't have the appropriate sheet names"
    return (allsheet_dict, ezsheet_dict)
 

word_count_dict_All = {}

def make_word_count_dict(my_dict, word_count_dict):
    '''
    Takes word count from each category and puts them into their own dictionary
    
    Inputs: the original dictionary and the resulting word_count dictionary
    Outputs: returns word_count dictionary and original dictionary
    '''
    for key in my_dict:
        value = my_dict[key]
        word_count = int(value[0])#1st value of each All column is integer
        word_count_dict[key] = word_count
    return word_count_dict
    

def extra_clean_dict(my_dict):
    '''
    Removes the word count from the dictionary
    Is separated from first clean because some 1st values were not numbers
    '''
    for key in my_dict.keys():
        if key == '': #takes care of case where key is blank for some reason
            del my_dict[key]
    return my_dict
    

def clean_dict(my_dict):
    '''
    Removes empty spaces ('') from a dictionary
    
    Inputs: dictionary
    Outputs: revised dictionary
    '''
    for key in my_dict:
        value = my_dict[key]
        for elm in value:
            if type(elm) == long:
                value.remove(elm)#gets rid of first elm of each value list which is word_count
        while '' in value:#gets rid of blanks in all value lists
            value.remove('')
    del my_dict['Total Words'] #gets rid of total words key
    return my_dict


from unidecode import unidecode

def lower_dict(my_dict):
    '''
    str in the lists for each key are made lowercase and ascii
    '''
    for key in my_dict:
        y = []
        for x in my_dict[key]:
            #excel automatically makes 'True' and 'False' bools; can't lower bools
            # --> if statement makes them unicode strings again
            if type(x) == bool:
                x = unicode(x)
            x = x.lower()
            x = unidecode(x)
            y.append(x)
        my_dict[key] = y
    return my_dict

def modify_dictionary(dictionary):
    '''
    calls all the dictionary modifiers at once
    '''
    dictionary = extra_clean_dict(dictionary)
    dictionary = clean_dict(dictionary)         
    dictionary = lower_dict(dictionary)
    return dictionary


#allsheet_dict, ezsheet_dict = create_dictionary(sheet_list)
#allsheet_dict = modify_dictionary(allsheet_dict)
#ezsheet_dict = modify_dictionary(ezsheet_dict)
#allsheet_word_count = make_word_count_dict(allsheet_dict, word_count_dict_All)


def find_non_alnum(allsheet_dict):
    '''
    finds non_alnum_words and contractions in dictionary
    '''
    non_alnum_words = []
    contraction_list = []
    for key in allsheet_dict:
        for word in allsheet_dict[key]:
            if word.isalnum() == False:
                non_alnum_words.append(word)
                if "'" in word:
                    contraction_list.append(word)
                    
    non_alnum_words = set(non_alnum_words)                
    contraction_list = set(contraction_list) 
    
    return (non_alnum_words, contraction_list)

#non_alnum_words, contraction_list = find_non_alnum(allsheet_dict)
#print non_alnum_words
#print contraction_list

def create_custom_stopword_list(dictionary):
    '''
    create custom_stopwords
    '''
    from nltk.corpus import stopwords
    s = stopwords.words('english')
    y= []
    for word in s: 
        y.append(unidecode(word))  
    s = y[:]
    for key in dictionary:
        for word in dictionary[key]:
            if word in s:
                s.remove(word)
    s.remove('should')
    more_stopwords = ['one', 'two', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',\
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
        'w', 'x', 'y', 'z', 'mom', 'dad']
    s.extend(more_stopwords)
    return s

#custom_stopwords = create_custom_stopword_list(allsheet_dict)
#print custom_stopwords
