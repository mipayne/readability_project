# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:30:58 2016

@author: Madelyn
"""

def book_tot_modify(multiple_txts):
    modified_book_words = {}
    #import sys
    #sys.path.insert(0, '/Users/Madelyn/Desktop/UROP/py_codes/project_codes')

    import modify_dictionary_from_excel_read
    import importing_txt_files_read 
    import fixing_strings_read
    import stopwords_modify_read
    import punctuation_modify_read
    import numeral_word_modify_read
    
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
    
       
    allsheet_dict, ezsheet_dict = modify_dictionary_from_excel_read.create_dictionary(sheet_list)
    allsheet_dict = modify_dictionary_from_excel_read.modify_dictionary(allsheet_dict)
    ezsheet_dict = modify_dictionary_from_excel_read.modify_dictionary(ezsheet_dict)
    
    
    custom_stopwords = modify_dictionary_from_excel_read.create_custom_stopword_list(allsheet_dict)

    removed_words = []
    
    book_words = importing_txt_files_read.import_txt(multiple_txts)
    
    #print book_words
    
    removed_propnouns = []
    
    #uses pos_tag to identify proper nouns and removes them from word list   
    for book in book_words:
        final_words = book_words[book]
        #print final_words
        temp_list = []
        for word in final_words:
            #print word[1]
            if word[1] != "NNP" and word[1] != "NNPS":
                temp_list.append(word[0])
            else:
                removed_propnouns.append(word[0])
                #print "prop-noun!!!!!!"
                #print word[0]
        book_words[book] = temp_list
                
    #print book_words
    #print removed_propnouns            

    for book in book_words:
        #print "This is a book: ", book
        fileName = book
        final_words = book_words[book]
        final_words_modify1 = fixing_strings_read.string_modify(final_words)
        #print 'final_words_modify1:'
        #print final_words_modify1
        #print '\n'
        final_words_modify2 = numeral_word_modify_read.num_modify(final_words_modify1)
        #print final_words_modify2
        bookset= set(final_words_modify2)
        book_words[book] = list(bookset)
        final_words_modify_set = book_words[book]
    
        final_words_modify3, removed_words = \
            punctuation_modify_read.punct_modify(final_words_modify_set, removed_words)
        #print 'word_count_words'
        #print final_words_modify3
        
        final_words_modify4, removed_words = \
            stopwords_modify_read.stopword_modify(final_words_modify3, custom_stopwords, removed_words)
        #print 'removed_words:'
    #    print removed_words
        #print 'final_words_final'
        #print final_words_modify4
        modified_book_words[fileName] = (final_words_modify3, final_words_modify4)
    return modified_book_words

'''
modified_book_words = book_tot_modify('./resources/converted/StoryCorpus/*.txt')
#count = 0
for book in modified_book_words:
    #count += 1
    final_words_modify3, final_words_modify4 = modified_book_words[book]
    print book
    print final_words_modify4
    print '\n'
#print count
'''