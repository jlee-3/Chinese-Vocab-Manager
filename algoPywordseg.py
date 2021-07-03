#!/Users/JLee/anaconda/envs/NLP/bin/python
#encoding=utf-8
FILE = "test.txt"

#import pywordseg
from pywordseg import *
#import pywordseg

# Prepare input
inputtxt = open(FILE, "r")
in_str = inputtxt.read()
in_list = [p for p in in_str.split('\n') if len(p) != 0] #input must be a list

# declare the segmentor.
seg = Wordseg(batch_size=64, device="cpu", embedding='elmo', elmo_use_cuda=False, mode="TW")

# input is a list of raw sentences.
#ws = seg.cut(["今天天氣真好啊!", "潮水退了就知道，誰沒穿褲子。"])
ws = seg.cut(in_list)

print([' | '.join(p) for p in ws])