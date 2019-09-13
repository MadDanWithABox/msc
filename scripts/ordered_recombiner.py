#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:45:04 2019

@author: s1527110
"""

with open('g.txt','r') as g:
    graph = g.readlines()
with open('m.txt','r') as m:
    morph = m.readlines()    
with open('p.txt','r') as p:
    phone = p.readlines()

with open('unsplit/disjoint/o-m-train.txt','r') as tr:
    m_tr = tr.readlines()

with open('unsplit/disjoint/o-m-tst.txt','r') as ts:
    m_ts = ts.readlines()
    
with open('unsplit/disjoint/o-m-val.txt','r') as v:
    m_v = v.readlines()

p_tr = []
p_ts = []
p_v = []

g_tr = []
g_ts = []
g_v = []

m_tst=[]
m_tra=[]
m_val=[]

for element in m_tr:
    ind = morph.index(element)
    gpop = graph.pop(ind)
    g_tr.append(gpop)
    ppop = phone.pop(ind)
    p_tr.append(ppop)
    mpop = morph.pop(ind)
    m_tra.append(mpop)
    
for element in m_ts:
    ind = morph.index(element)
    gpop = graph.pop(ind)
    g_ts.append(gpop)
    ppop = phone.pop(ind)
    p_ts.append(ppop)
    mpop = morph.pop(ind)
    m_tst.append(mpop)
    
for element in m_v:
    ind = morph.index(element)
    gpop = graph.pop(ind)
    g_v.append(gpop)
    ppop = phone.pop(ind)
    p_v.append(ppop)
    mpop = morph.pop(ind)
    m_val.append(mpop)

        
with open('unsplit/disjoint/o-g-train.txt','w') as a:
    a.writelines(g_tr)
        
with open('unsplit/disjoint/o-g-tst.txt','w') as b:
    b.writelines(g_ts)
    
with open('unsplit/disjoint/o-g-val.txt','w') as c:
    c.writelines(g_v)
    
with open('unsplit/disjoint/o-p-train.txt','w') as d:
    d.writelines(p_tr)
        
with open('unsplit/disjoint/o-p-tst.txt','w') as e:
    e.writelines(p_ts)
    
with open('unsplit/disjoint/o-p-val.txt','w') as f:
    f.writelines(p_v)