#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:41:20 2019

@author: s1527110
"""
import re

def stripchars(s, chars):
	return re.sub('[%s]+' % re.escape(chars), '', s)

with open('g2mp_random.txt','r') as f:
    fl = f.read()

q=[]
x=[]
l=[]

z = re.findall('acc:  \d+\.\d+', fl)
for element in z:
    p= stripchars(element, ":acc ")
    q.append(p)



z = re.findall('ppl: +\d+\.\d+', fl)
for element in z:
    p=stripchars(element, "ppl: ")
    x.append(p)


z=re.findall('xent: +\d+\.\d+',fl)
for element in z:
    o=stripchars(element, "xent: ")
    l.append(o)

with open('acc.txt', 'w+') as g:
    for item in q:
         g.write("%s\n" % item)
    
with open('ppl.txt', 'w+') as g:
    for item in x:
         g.write("%s\n" % item)
    
with open('xent.txt', 'w+') as g:
    for item in l:
         g.write("%s\n" % item)