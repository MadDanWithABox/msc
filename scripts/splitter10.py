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
g_tr=[]

morph=[]
m_test=[]
m_val=[]
m_tr=[]

phone=[]
p_test=[]
p_val=[]
p_tr=[]

'''Read in files'''

with open('g.txt','r') as g:
    graph = g.readlines()
with open('m.txt','r') as m:
    morph = m.readlines()    
with open('p.txt','r') as p:
    phone = p.readlines()
    
    
test = 894
val = 1340
train = 6697

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
    
counter = 0   
while counter < train:
    index = random.randint(0, len(graph))
    gpop = graph.pop(index)
    g_tr.append(gpop)
    ppop = phone.pop(index)
    p_tr.append(ppop)
    mpop = morph.pop(index)
    m_tr.append(mpop)
    counter+=1
    

print('train set: ', len(g_tr), '\n', 'test set: ', len(g_test), '\n', 'val set: ', len(g_val))

'''
Write to files Train, Val, Test
'''
with open('./10/g-10-train.txt','w') as g_t:
    for item in g_tr:
        g_t.write(" ".join(item))
        
with open('./10/m-10-train.txt','w') as m_t:
    for item in m_tr:
        m_t.write(" ".join(item))
        
with open('./10/p-10-train.txt','w') as p_t:
    for item in p_tr:
        p_t.write(" ".join(item))
        
with open('./10/g-10-val.txt','w') as g_v:
    for item in g_val:
        g_v.write(" ".join(item))
        
with open('./10/m-10-val.txt','w') as m_v:
    for item in m_val:
        m_v.write(" ".join(item))
        
with open('./10/p-10-val.txt','w') as p_v:
    for item in p_val:
        p_v.write(" ".join(item))
        
with open('./10/g-10-tst.txt','w') as g_ts:
    for item in g_test:
        g_ts.write(" ".join(item))
        
with open('./10/m-10-tst.txt','w') as m_ts:
    for item in m_test:
        m_ts.write(" ".join(item))
        
with open('./10/p-10-tst.txt','w') as p_ts:
    for item in p_test:
        p_ts.write(" ".join(item))

with open('./10/bpe/g-10-train.txt','w') as g_t:
    for item in g_tr:
        g_t.write(item)
        
with open('./10/bpe/m-10-train.txt','w') as m_t:
    for item in m_tr:
        m_t.write(item)
        
with open('./10/bpe/p-10-train.txt','w') as p_t:
    for item in p_tr:
        p_t.write(item)
        
with open('./10/bpe/g-10-val.txt','w') as g_v:
    for item in g_val:
        g_v.write(item)
        
with open('./10/bpe/m-10-val.txt','w') as m_v:
    for item in m_val:
        m_v.write(item)
        
with open('./10/bpe/p-10-val.txt','w') as p_v:
    for item in p_val:
        p_v.write(item)
        
with open('./10/bpe/g-10-tst.txt','w') as g_ts:
    for item in g_test:
        g_ts.write(item)
        
with open('./10/bpe/m-10-tst.txt','w') as m_ts:
    for item in m_test:
        m_ts.write(item)
        
with open('./10/bpe/p-10-tst.txt','w') as p_ts:
    for item in p_test:
        p_ts.write(item)
