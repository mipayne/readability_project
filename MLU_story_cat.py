# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:00:50 2016

@author: Madelyn
"""

import modify_dictionary_from_excel_read
import book_tot_modify_read

sheet_list = []

sheet_list.append('./resources/All_output.xlsx')
sheet_list.append('./resources/Easy_output.xlsx')

allsheet_dict, ezsheet_dict = modify_dictionary_from_excel_read.create_dictionary(sheet_list)
allsheet_dict = modify_dictionary_from_excel_read.modify_dictionary(allsheet_dict)
ezsheet_dict = modify_dictionary_from_excel_read.modify_dictionary(ezsheet_dict)


custom_stopwords = modify_dictionary_from_excel_read.create_custom_stopword_list(allsheet_dict)

MLU1 = []
MLU2 = []
MLU3 = []
MLU4 = []
MLU5 = []
MLU6 = []
MLU7 = []
MLU8 = []
MLU9 = []
MLU10 = []
cat_list = {}




