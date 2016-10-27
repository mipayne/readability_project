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

#perform automated inference to show the validity of the argument
#NotFnS = read_expr('-north_of(f,s)')
#print(NotFnS)
#SnF = read_expr('north_of(s, f)')
#R = read_expr('all x.all y. (north_of(x,y) -> -north_of(y,x))')
#prover = nltk.inference.Prover9()
#prover.config_prover9(r'./bin')
#prover.prove(NotFnS, [SnF, R])


#truth in model
dom = {'b','o', 'c'}
v = """bertie => b
olive => o 
cyril => c
boy => {b}
girl => {o}
dog => {c}
walk => {o, c}
see => {(b, o), (c, b), (o, c)}
"""
val= nltk.Valuation.fromstring(v)
#test truth
print ('o', 'c') in val['see']#True

print ('b',) in val['boy']#True

#if you used bindings, in (variable, value) format
g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
print g#{'y':'c', 'x':'o'}

m = nltk.Model(dom, val)
print m.evaluate('see(olive,y)',g)
#clear all bindings from an assignment
g.purge()
print m.evaluate('see(olive,y)', g)#Undefined

#Model building
a3 = read_expr('exists x.(man(x) & walks(x))')
c1 = read_expr('mortal(socrates)')
c2 = read_expr('-mortal(socrates)')
mb = nltk.Mace(5)
#can't use mace
mb.config_prover9(r'./bin/')
print(mb.build_model(None, [a3, c1]))

