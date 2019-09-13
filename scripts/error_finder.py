#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:58:31 2019

@author: s1527110
"""

import argparse
import re

parser = argparse.ArgumentParser(description='Returns a list of all non-matching elements in the 2 provided files for error analysis.')
parser.add_argument("prediction", type = argparse.FileType('r'), help="prediction file path")
parser.add_argument("gold",type = argparse.FileType('r'), help="gold reference transcription path")
parser.add_argument("outfile", type = argparse.FileType('w'), help="path to write errors to")
args = parser.parse_args()

with args.prediction as p:
    predictions = p.readlines()
    
with args.gold as g: 
    gold = g.readlines()
    
p = set(predictions)
g = set(gold)
errors = p - g #find elements that are in predictions but not in gold
errors = list(errors)
matches=[]

for element in errors:
    if element in predictions:
        item = element
        ind = predictions.index(item)
        matches.append(gold[ind])

correct = 0
counter = 0
insertions = 0
deletions = 0
err_phones = []
cons = 0
vowels = 0
unk=0

l_e = [i.split() for i in errors]
l_g = [i.split() for i in matches]

for e in range(0, len(l_e)):
    for c in range(0,len(l_g[e])):
        counter +=1
        if len(l_g[e]) == len(l_e[e]):
            if l_g[e][c] == l_e[e][c]:
                correct +=1
            else:
                err_phones.append(l_e[e][c])
                
        if len(l_g[e]) > len(l_e[e]):
            insertions +=1
        if len(l_g[e]) < len(l_e[e]):
            deletions +=1
        else:
            unk +=1
            
        

    
print("Here are the first 20 wrong phones: ", err_phones[0:190], '\nThere were ', insertions, ' insertions, and ', deletions,' deletions, with ', unk, ' unknown errors.\n',correct,' phones were correct, out of ',counter,' in total. This script classified ', len(err_phones))

vowel_match = re.compile('(?:E|e|I|i|@|3|V|A|u|U|o|0|Q|7|a|2|\*|~|1|9|6)')
cons_match = re.compile('(?:b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|z|R|P|W|H|L|N|5|4|S|Z|C|D|T|V)')

for err in err_phones:
    
     
        


zipped = tuple(zip(errors, matches))
dong = []
for element in zipped:
    dong.append(str(element))
    dong.append('\n')

dong.insert(0, "PREDICTED ON LEFT    GOLD ON RIGHT \n")
        
with args.outfile as f:
    f.writelines(dong)
