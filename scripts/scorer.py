#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:03:43 2019

@author: s1527110
"""
import statistics
import argparse

parser = argparse.ArgumentParser(description='Returns WER for given prediction and gold standard file.')
parser.add_argument("prediction", type = argparse.FileType('r'), help="prediction file path")
parser.add_argument("gold",type = argparse.FileType('r'), help="gold reference transcription path")
args = parser.parse_args()

print("Calculating accuracy, please wait...")

with args.prediction as p:
    predictions = p.readlines()
    
with args.gold as g:
    gold = g.readlines()

errors=[]
binary=[]
counter = 0
total = len(gold)
for line1 in predictions:
    for line2 in gold:
        if line1==line2:
            binary.append(1)
            counter+=1
        else:
            binary.append(0)
            #errors.append(line1)
            #errors.append(line2)
            
index=0
while index < len(predictions):
    if binary[index] == 0:
        errors.append(predictions[index] + gold[index])
        index+=1
    else:
        index+=1




print("This is gold line 1: ",gold[7])
print("This is predicted line 1: ",predictions[7])
print("If these look weird, look at fixing your data")

print("E:",len(errors), "   G:",len(gold))
#print(counter)
score = counter/total
percentage = score*100
percentage = 100-percentage


print('Total WER = ', percentage)

################## PER calculator ###############
def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

pers=[]
counter = 0
for line in predictions:
    per = levenshteinDistance(predictions[counter], gold[counter])/len(gold[counter])
    pers.append(per)
    counter+=1

###########Error classifier###########

'''   
p = set(predictions)
g = set(gold)
wrong = p - g #find elements that are in predictions but not in gold
wrong = list(wrong)

matches=[]

for element in wrong:
    if element in predictions:
        
        item = element
        ind = predictions.index(item)
        try:
            matches.append(wrong[ind])
        except:
            print('error')
        
        

correct = 0
insertions = 0
deletions = 0
err_phones = []
unk=0

l_e = [i.split() for i in wrong]
l_g = [i.split() for i in matches]

for e in range(0, len(l_e)):
    for c in len(l_g[e]):
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
'''    
#print("Here are the first 20 wrong phones: "+ wrong[0:19]+ '\nThere were '+ insertions+ ' insertions, and '+ deletions+' deletions, with '+ unk+ ' unknown errors.')


mean = statistics.mean(pers[1:10])
print("Avg LD for first 10 items= ", mean)

mean_tot= statistics.mean(pers)
print("Total PER = ", mean_tot*100, "%")

with open('outfile.txt', 'w') as f:
    for item in errors:
        f.write("%s\n" % item)