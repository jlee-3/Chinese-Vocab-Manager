#!/Users/JLee/anaconda/envs/NLP/bin/python
#encoding=utf-8
FILE = "test.txt"

import ckip_transformers
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker
# Initialize drivers

ws_driver = CkipWordSegmenter(level=3, device=-1)
#pos_driver = CkipPosTagger(level=3, device=-1)
#ner_driver = CkipNerChunker(level=3, device=-1)
# Prepare input
inputtxt = open(FILE, "r")
in_str = inputtxt.read()
# text = [
#    "傅達仁今將執行安樂死，卻突然爆出自己20年前遭緯來體育台封殺，他不懂自己哪裡得罪到電視台。",
#    "美國參議院針對今天總統布什所提名的勞工部長趙小蘭展開認可聽證會，預料她將會很順利通過參議院支持，成為該國有史以來第一位的華裔女性內閣成員。",
#    "空白 也是可以的～",
# ]
in_str = [p for p in in_str.split('\n') if len(p) != 0]
# Run pipeline
ws  = ws_driver(in_str, use_delim=True)
#ws  = ws_driver(text, use_delim=True)
#pos = pos_driver(ws)
#ner = ner_driver(in_str)

print([' | '.join(p) for p in ws])
#print('\n\n'.join([' | '.join(p) for p in ws]))
