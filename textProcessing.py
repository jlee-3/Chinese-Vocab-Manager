#!/Users/JLee/anaconda/envs/NLP/bin/python
#encoding=utf-8

import re
import collections

def filterHanzi(w):
    if re.search(u'[\u4e00-\u9fff]+', w) != None:
        return True
    else:
        return False

def txtCleaner(wordList):
    cleanList = filter(filterHanzi, wordList)
    #return cleanList
    return [p for p in cleanList]

def listFreq(wordList):
    freqdict = collections.Counter(wordList)
    orderedfreq = dict(freqdict)
    return dict(sorted(orderedfreq.items(), key=lambda x: x[1], reverse=True))
    #return dict(freqdict)

def unknownWords(wordList, knownList):
    klSet = set(knownList) #convert list to set for search time = O(n)
    unknownList = filter(lambda w: w not in klSet, wordList)
    return [p for p in unknownList]