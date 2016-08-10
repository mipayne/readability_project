# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:04:40 2016

@author: Madelyn
"""
'''
import pyexcel
sheet = pyexcel.get_sheet(file_name = './Story_Difficulty_Orders.xlsx', name_columns_by_row=0)

path_dict = dict(sheet.to_dict())
print path_dict
'''
'''
for key in path_dict:
    print key
    print path_dict[key]
'''


'''
import pandas as pd
df = pd.read_csv('./Story_Difficulty_Orders-Sheet1.csv')
column_list = []
column = df["Path for children with approximately equal NVQS levels"]
print column

story_dict = {}

for key in path_dict:
    y = []
    for i in range(len(path_dict[key])):
        if i == 0:
            story_dict[path_dict[key][i]]= [key]
        elif dict[path][i] in story_dict:
            for x in :
'''                
                
import xlrd

book = xlrd.open_workbook('./Story_Difficulty_Orders.xlsx')

first_sheet = book.sheet_by_index(0)
print first_sheet.row_values(0)

path_dict = {}
value_count = 0
for value in first_sheet.row_values(0):
    print value
    book_count = 0
    value_count += 1
    #skip row 1
    for i in range(2,10):
        for book in first_sheet.row(i):
            book_count += 1
            if book_count == value_count:
                y = []
                pass
                if value in path_dict.keys:
                    y.extend(path_dict[value])
                y.append(first_sheet.row(i)[book_count-1])
                path_dict[value]= y
            break
        
print path_dict.keys               
'''                    
    for book in first_sheet.row(2):
        
        if book_count == count:
            path_dict[value] = [book]
        if count = 1:
            path_dict[value] = [book]
        if count = 2:
            path_dict[value]
        
#skip row 1
count = 0 
for value in first_sheet.row_value(2):
    count +=1
    if count = 1:
'''