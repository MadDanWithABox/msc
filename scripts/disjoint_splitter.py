#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:29:59 2019

@author: s1527110
"""

import re
import random

val_list=[]
trn_list=[]
tst_list=[]

with open('m.txt','r') as m:
    word_list = m.readlines()


regex = re.compile(r".*({[a-z=]+}).*")
matches=[]

for element in word_list:
        m = re.search(regex, element)
        if m:
                root = m.group(1)
                matches.append(root)

target = len(word_list) / 20
while len(val_list) < target:
        randroot = random.choice(matches) # select a random {root}
        found_words = [w for w in word_list if randroot in w] # get all words with given root in them


        val_list.extend(found_words)
        word_list = [w for w in word_list if w not in val_list] # remove all the words we just added

target = len(word_list) / 5
while len(tst_list) < target:
        randroot = random.choice(matches) # select a random {root}
        found_words = [w for w in word_list if randroot in w] # get all words with given root in them


        tst_list.extend(found_words)
        word_list = [w for w in word_list if w not in tst_list] # remove all the words we just added

trn_list=word_list



with open('separate_train/o-m-train.txt','w') as m_t:
    for item in trn_list:
        m_t.write(" ".join(item))
with open('separate_test/o-m-tst.txt','w') as m_ts:
    for item in tst_list:
        m_ts.write(" ".join(item))
with open('separate_val/o-m-val.txt','w') as m_v:
    for item in val_list:
        m_v.write(" ".join(item))
