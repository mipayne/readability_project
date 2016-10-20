# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:42:30 2016

@author: Madelyn
"""

import nltk
from nltk import load_parser
cp = load_parser('grammars/book_grammars/sql0.fcfg', trace = 3)
query = 'What cities are located in China'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
#print(q)


#assign every propositional symbol value
val = nltk.Valuation([('P', True), ('Q', True), ('R', False)])
dom = set()
g = nltk.Assignment(dom)

#initialize a model that uses val
m = nltk.Model(dom, val)
#every model comes with an evaluate() method, which will determine the \
#   semantic value of logial expressions, such as formulas of propositonal logic; depend on P, Q, and R
print(m.evaluate('(P & Q)', g))
print(m.evaluate('-P -> Q', g))

#using Frist Order Logic
read_expr = nltk.sem.Expression.fromstring
#use signature to associate types with non-logical constants
sig = {'walk': '<e, t>'}
expr = read_expr('walk(angus)', signature=sig)
print(expr.function.type)
print(expr.argument.type)

NotFnS = read_expr('-north_of(f,s)')
print(NotFns)
SnF = read_expr('north_of(s, f)')

