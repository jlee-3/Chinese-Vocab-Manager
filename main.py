#!/Users/JLee/anaconda/envs/NLP/bin/python
#encoding=utf-8

from algoJieba import *
from textProcessing import *
from postgresTools import *

IMPORT_PATH = "/Users/JLee/Google Drive/Data Science/Projects/Chinese Vocab Manager/import text/"
OUTPUT_PATH = "/Users/JLee/Google Drive/Data Science/Projects/Chinese Vocab Manager/outputs/"
FILE = "test.txt"
OUTPUTFILE = "test output_t1.txt"

inputtxt = open(IMPORT_PATH + FILE, "r")
in_str = inputtxt.read()
print(in_str)
outList = runJieba(in_str)
print(outList)
#print([' | '.join(p) for p in outList])
outList = txtCleaner(outList)
inputWords = outList
#print(outList)
#print([p for p in outList])
#outList = [p for p in outList]
#print(outList)
#knownList = ['的','在','是','一個','藝文']
#knownList = ['是','一個','藝文']
knownList = getTableAsList(connectServer(), 'knownwords', 'word')
outList = unknownWords(outList, knownList)
wordfreq = listFreq(outList)
print(wordfreq)
knownratio = (len(inputWords) - len(wordfreq))/ len(inputWords)
print("Percentage of words known: ", knownratio)

#tocflList = getTableAsList(connectServer(), 'tocfl_list', 'tocfl_word')