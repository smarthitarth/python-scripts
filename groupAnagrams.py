# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:43:32 2020

@author: hitar
"""
import collections
l = ["eat", "tea", "tan", "ate", "nat", "bat"]
#m = [3,2,1,2]
#c = collections.Counter(l)
cd = []
for i in l:
    cd.append("".join(sorted(i)))

lm = []
lm2 = []
m = 0
for i in range(len(cd)):
    print(cd[i])
    if cd[i] not in lm:
        lm.append(cd[i])
        lm2.append([l[i]])
        for j in range(i+1, len(cd)):
            if(cd[i] == cd[j]):
                lm2[m].append(l[j])
        m+=1