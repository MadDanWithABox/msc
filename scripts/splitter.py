#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:01:01 2019

@author: s1527110
"""


import random
counter = 0
graph = []
g_test=[]
g_val=[]

morph=[]
m_test=[]
m_val=[]

phone=[]
p_test=[]
p_val=[]


'''Read in files'''

with open('g.txt','r') as g:
    graph = g.readlines()
with open('m.txt','r') as m:
    morph = m.readlines()    
with open('p.txt','r') as p:
    phone = p.readlines()
    
    
test = len(graph)/5
val = len(graph)/20
print("Lexicon size: ",len(graph)) #just a test to make sure the files are correctly read in, should be lexicon size


'''Randomly sample items in vocab to train, test, dev sets'''

while counter < val:
    index = random.randint(0, len(graph))
    gpop = graph.pop(index)
    g_val.append(gpop)
    ppop = phone.pop(index)
    p_val.append(ppop)
    mpop = morph.pop(index)
    m_val.append(mpop)
    counter+=1

counter = 0   
while counter < test:
    index = random.randint(0, len(graph))
    gpop = graph.pop(index)
    g_test.append(gpop)
    ppop = phone.pop(index)
    p_test.append(ppop)
    mpop = morph.pop(index)
    m_test.append(mpop)
    counter+=1

g_train = graph
m_train = morph
p_train = phone
    
print('train set: ', len(g_train), '\n', 'test set: ', len(g_test), '\n', 'val set: ', len(g_val))

"""
Write to files Train, Val, Test
"""
with open('train/g-train.txt','w') as g_t:
    for item in g_train:
        g_t.write(" ".join(item))
        
with open('train/m-train.txt','w') as m_t:
    for item in m_train:
        m_t.write(" ".join(item))
        
with open('train/p-train.txt','w') as p_t:
    for item in p_train:
        p_t.write(" ".join(item))
        
with open('val/g-val.txt','w') as g_v:
    for item in g_val:
        g_v.write(" ".join(item))
        
with open('val/m-val.txt','w') as m_v:
    for item in m_val:
        m_v.write(" ".join(item))
        
with open('val/p-val.txt','w') as p_v:
    for item in p_val:
        p_v.write(" ".join(item))
        
with open('test/g-tst.txt','w') as g_ts:
    for item in g_test:
        g_ts.write(" ".join(item))
        
with open('test/m-tst.txt','w') as m_ts:
    for item in m_test:
        m_ts.write(" ".join(item))
        
with open('test/p-tst.txt','w') as p_ts:
    for item in p_test:
        p_ts.write(" ".join(item))
