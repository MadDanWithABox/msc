"""
Created on Thu Jun 13 12:01:01 2019

@author: s1527110
"""
filename = 'unilex.txt'
file = open(filename, 'r')

current = file.readlines()

graph = []
morph=[]
phone=[]


split_lines = [e.split(':') for e in current]
for i in range(len(split_lines)):
                graph.append(split_lines[i][0])
for i in range(len(split_lines)):
                morph.append(split_lines[i][4])
for i in range(len(split_lines)):
                phone.append(split_lines[i][3])

#print(morph[119355], ' ', graph[119355])
morph2graph = dict(zip(morph, graph))
graph2phone = dict(zip(graph, phone))

#print(graph2phone)

with open('g.txt','w') as g:
    for item in graph:
        g.write("%s\n" % item)

with open('m.txt','w') as m:
    for item in morph:
        m.write("%s\n" % item)

with open('p.txt','w') as p:
    for item in phone:
        p.write("%s\n" % item)

        
p.close()
m.close()
g.close()
file.close()
