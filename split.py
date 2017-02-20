# -*- coding: utf-8 -*-  
import io
import re, collections
import jieba
import json

# 过滤空格
def trimSpace(segList):
    trimStr = []
    for str in segList:
        if str.strip() != "":
            trimStr.append(str.strip())
    return trimStr

# 过滤其他字符，只保留两位长度的中文
def filterWords(str):
    if re.match(u'([\u4e00-\u9fff]+)', str) and len(str)==2:
         return True
    return False

if __name__ == "__main__":
    fd = open("happiness_seg.txt",'r')
    content = fd.read().decode('utf8')
    #这里需要使用分词工具分词，直接使用" "分割会因为回车换行符没法分割而造成漏词
    segList = jieba.lcut(content, cut_all=False)

    # 过滤空格
    segList = trimSpace(segList)

    #判断是否二元词组
    wordList = []
    for i in range(0, len(segList)-1):
        if filterWords(segList[i]) and filterWords(segList[i+1]):
            wordList.append(segList[i]+""+segList[i+1])

    #输出频率最高的前 10 个「二元词组」
    print(json.dumps(collections.Counter(wordList).most_common(10)).decode("unicode-escape"))
