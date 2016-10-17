# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:42:30 2016

@author: Madelyn
"""


from nltk import load_parser
cp = load_parser('grammars/book_grammars/sql0.fcfg', trace = 3)
query = 'What cities are located in China'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)