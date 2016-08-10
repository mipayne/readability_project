# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:33:22 2016

@author: Madelyn
"""
import modify_dictionary_from_excel
import book_tot_modify

sheet_list = []
'''
from pyexcel.cookbook import split_a_book

split_a_book('./resources/WordCategories.xlsx', 'output.xlsx')
import glob
outputfiles = glob.glob('*_output.xlsx')#splits book to be single sheets
for file in sorted(outputfiles):
    sheet_list.append(file)#adds each new sheet to a list
'''

sheet_list.append('./resources/All_output.xlsx')
sheet_list.append('./resources/Easy_output.xlsx')

   
allsheet_dict, ezsheet_dict = modify_dictionary_from_excel.create_dictionary(sheet_list)
allsheet_dict = modify_dictionary_from_excel.modify_dictionary(allsheet_dict)
ezsheet_dict = modify_dictionary_from_excel.modify_dictionary(ezsheet_dict)


custom_stopwords = modify_dictionary_from_excel.create_custom_stopword_list(allsheet_dict)

modified_book_words = book_tot_modify.book_tot_modify('./StoryCorpus_copy/1.2/*.txt')
for book in 

'''
list1dot2 = []
list1dot3 = []
list1dot5 = []
list1dot6 = []
list1dot8to2 = []
list2or3 = []
cat_list = {}

modified_book_words = book_tot_modify.book_tot_modify('./StoryCorpus_copy/1.2/*.txt')
for book in modified_book_words:
    final_words_modify3, final_words_modify4 = modified_book_words[book]
    list1dot2.extend(final_words_modify4)
cat_list['1.2'] = list1dot2
    
modified_book_words = book_tot_modify.book_tot_modify('./StoryCorpus_copy/1.3/*.txt')
for book in modified_book_words:
    final_words_modify3, final_words_modify4 = modified_book_words[book]
    list1dot3.extend(final_words_modify4)
cat_list['1.3'] = list1dot3
   
modified_book_words = book_tot_modify.book_tot_modify('./StoryCorpus_copy/1.5/*.txt')
for book in modified_book_words:
    final_words_modify3, final_words_modify4 = modified_book_words[book]
    list1dot5.extend(final_words_modify4)
cat_list['1.5'] = list1dot5
    
modified_book_words = book_tot_modify.book_tot_modify('./StoryCorpus_copy/1.6/*.txt')
for book in modified_book_words:
    final_words_modify3, final_words_modify4 = modified_book_words[book]
    list1dot6.extend(final_words_modify4)
cat_list['1.6'] = list1dot6


modified_book_words = book_tot_modify.book_tot_modify('./StoryCorpus_copy/1.8-1.9-2/*.txt')
for book in modified_book_words:
    final_words_modify3, final_words_modify4 = modified_book_words[book]
    list1dot8to2.extend(final_words_modify4)
cat_list['1.8-1.9-2'] = list1dot8to2  
  
modified_book_words = book_tot_modify.book_tot_modify('./StoryCorpus_copy/2-3/*.txt')
for book in modified_book_words:
    final_words_modify3, final_words_modify4 = modified_book_words[book]
    list2or3.extend(final_words_modify4)
cat_list['2-3'] = list2or3

for key in cat_list:
    print key
    print cat_list[key]
    print '\n'
'''
    
    