__author__ = 'Administrator'
import requests
import re

fr = open("IP.txt",'r')
fw = open("ipParse.txt",'w')

str = fr.readline()
URL = "http://ip.chinaz.com/ajaxsync.aspx?at=ip&callback=jQuery111307981394122348004_1463649579878"

while str:
    ip = {"ip":str}
    if str <> "":
        response = requests.post(URL,ip)
        r=re.compile(r'location:\'(.*)\'')
        addr = re.search(r,response.content)
        if addr <> None:
            line = str +","+addr.group(1)
            fw.write(line)
            print addr.group(1)
    str = fr.readline()

fr.close()
fw.close()