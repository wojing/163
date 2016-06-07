__author__ = 'Administrator'
#-*-coding:utf8;-*-
import requests
import re
import json
import ast
from bs4 import BeautifulSoup
import time

url = "http://1.163.com/results.html"
r = requests.get(url)

s = BeautifulSoup(r.text,"html.parser")
##l = s.find_all({'class':'w-goods-price'})
l = s.find_all(class_='w-goods-price')
print "old len: "+str(l.__len__())

pageSize = 15
totalCnt = 14797
showAll = 'true'
token = '4bfc9dbe-af97-461d-8230-e2ac8c0d5570'
timestamp  = int(time.time())
pageNum = 16

param = { 'pageNum':pageNum,'pageSize':pageSize, 'totalCnt':totalCnt, 'showAll':'true', 'token':token,'t':timestamp}
res = requests.get('http://1.163.com/goods/revealList.do',params=param)

url = "http://1.163.com/results.html"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
##l = s.find_all({'class':'w-goods-price'})
l = s.find_all(class_='w-goods-price')
print "new len :"+str(l.__len__())

# rule = re.compile(r'\d+')
# a = 0
# for i in l:
#  u
def convertL2str(dictl):
    strlist = ""
    for i in dictl.keys():
        if i != "owner" and  i != "goods":
            strlist += (str(dictl[i]))+","

    goodlist = ""
    for i in dictl["goods"].keys():

        goodlist += (str(dictl["goods"][i]))+","

    ownerlist = ""
    if "owner" in dictl.keys():
        for i in dictl["owner"].keys():
            ownerlist += (str(dictl["owner"][i]))+","



    return strlist+goodlist+ownerlist;


def countR(pageNum):
    pageSize = 15
    totalCnt = 14797
    showAll = 'true'
    token = '4bfc9dbe-af97-461d-8230-e2ac8c0d5570'
    timestamp  = int(time.time())

    param = { 'pageNum':pageNum,
              'pageSize':pageSize,
              'totalCnt':totalCnt,
              'showAll':'true',
              'token':token,
              't':timestamp
              }

    res = requests.get('http://1.163.com/goods/revealList.do',params=param)
    str1 = res.content

    j = json.loads(res.content)
    s = json.dumps(j)
    s2=s.replace("null","None")
    s3= s2.replace("true","\"true\"")
    j = eval(s3)

    l = j["result"]["list"]
    stringL = ""
    for i in l:

        stringL += convertL2str(i)+"\n"

    return stringL

# i = 1
# e = []
# ResultStr = ""
# while i<3:
#     print "start"
#     ResultStr = countR(i)
#     i = i+1
#
# # for k in e:
# #     try:
# #         countR(k)
# #     except:
# #         print "Page "+str(k)+" is Error"
# #     finally:
# #         time.sleep(0.5)
# print "ResultStr: "  + ResultStr

