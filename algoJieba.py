#!/Users/JLee/anaconda/envs/NLP/bin/python
#encoding=utf-8
# PATH = "/Users/JLee/Google Drive/Data Science/Projects/Chinese Vocab Manager/"
# FILE = "test.txt"
# OUTPUTFILE = "test output_t1.txt"

import jieba
import re

def runJieba(in_str):
    jieba.set_dictionary('data/dict.txt.big.txt')
    #inputtxt = open(PATH + FILE, "r")
    #in_str = inputtxt.read()
    #print(in_str)
    result = jieba.tokenize(in_str, mode='search') #tokenize search: number one accuracy so far
    # outstr = ""
    # for tk in result:
    #     #print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
    #     if re.search(u'[\u4e00-\u9fff]+', tk[0]) != None:
    #         print(tk[0])
    #         #outstr = outstr + tk[0].encode('utf-8') + "\n"
    #         outstr = outstr + tk[0] + "\n"
    # return outstr
    outList = []
    for tk in result:
        outList.append(tk[0])
    return outList


# seg_cutall = jieba.lcut(in_str, cut_all=True)
# seg_conserve = jieba.lcut(in_str, cut_all=False)
# seg_cutall = jieba.lcut("被圍困在", cut_all=True)
# seg_conserve = jieba.lcut("被圍困在", cut_all=False)

#seg_cutall = jieba.lcut("我来到北京清華大學", cut_all=True)
#print seg_cutall
#print("Full Mode: " + "/ ".join(seg_cutall))  # 全模式
#seg_conserve = jieba.lcut("我来到北京清華大學", cut_all=False)
#print("Default Mode: " + "/ ".join(seg_conserve))  # 默认模式

# TEST ALGOS HERE
#seg_all = seg_cutall + seg_conserve
#seg_all = jieba.cut_for_search(in_str,HMM=True)
#seg_all = jieba.lcut(in_str, cut_all=True)
#result = jieba.tokenize(unicode(in_str,'utf-8'), mode='search') #tokenize search: number one accuracy so far
# result = jieba.tokenize(in_str, mode='search') #tokenize search: number one accuracy so far
# outstr = ""
# for tk in result:
#     #print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
#     if re.search(u'[\u4e00-\u9fff]+', tk[0]) != None:
#         print(tk[0])
#         #outstr = outstr + tk[0].encode('utf-8') + "\n"
#         outstr = outstr + tk[0] + "\n"

#print seg_all
# seg_uniq = list(set(seg_all))
# seg_uniq = map(lambda x: re.sub("\s", "", x), seg_uniq)

# outstr = "\n".join(seg_uniq).encode('utf-8').strip()
# print(outstr)
# outfile = open(OUTPUTFILE, "w")
# outfile.write(outstr.strip())
# outfile.close()
