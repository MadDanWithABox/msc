#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:24:47 2019

@author: s1527110
"""

import argparse
import statistics

parser = argparse.ArgumentParser(description='Returns WER for given prediction and gold standard file.')
parser.add_argument("prediction", type = argparse.FileType('r'), help="prediction file path")
parser.add_argument("gold",type = argparse.FileType('r'), help="gold reference transcription path")
args = parser.parse_args()

print("Calculating Phone error rate please wait...")

with args.prediction as p:
    predictions = p.readlines()
    
with args.gold as g:
    gold = g.readlines()
    
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

print("LD for 1st item= ",pers[0])

mean = statistics.mean(pers[1:10])
print("Avg LD for first 10 items= ", mean)

mean_tot= statistics.mean(pers)
print("Total PER = ", mean_tot*100, "%")