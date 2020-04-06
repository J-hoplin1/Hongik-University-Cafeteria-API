from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import html
import sys
import time
import unidecode
import re
import json
todayDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#Convert Dictionary to json
dirCode = os.getcwd()
def saveAsJSON(jsonStr):
    #save at same directory with code
    with open('HongikUnivSejongCampusCafeteria'+todayDate+'.json', 'w', encoding="utf-8") as make_file:
        json.dump(jsonStr, make_file, ensure_ascii=False, indent="\t") #indent -> Indentation parameter


makeTodayMealization = dict()

#URL
URL = "http://sj.hongik.ac.kr/site/food/food_menu.html"
n = time.localtime().tm_wday
html = urlopen(URL)
bs = BeautifulSoup(html,'html.parser')

Location = []
getCafeteriaLocation = bs.findAll('th')
for gc in getCafeteriaLocation:
    Location.append(gc.text)

Location = Location[8:]

menus = []
getAllmenuInfo = bs.findAll('td',{'class' : 'mon'})
for ga in getAllmenuInfo:
    menus.append(ga.text.replace('\n','').replace('\t','').split('\r'))

capsule = []
if n == 6:
    makeTodayMealization["Date"] = todayDate
    makeTodayMealization[Location[0]] = {
        Location[1]: ""
    }
    makeTodayMealization[Location[2]] = {
        Location[3]: "",
        Location[4]: "",
        Location[5]: "",
        Location[6] + "_1": "",
        Location[7] + "_2": "",
        Location[8] + "_1": "",
        Location[9] + "_2": "",
        Location[10]: ""
    }
    makeTodayMealization[Location[11]] = {
        Location[12]: "",
        Location[13]: "",
        Location[14]: ""
    }
    makeTodayMealization[Location[15]] = {
        Location[16]: "",
        Location[17]: ""
    }
    saveAsJSON(makeTodayMealization)
else:
    for r in range(0,len(menus)):
        if r % 6 == n:
            capsule.append(menus[r])
        else:
            pass
    makeTodayMealization["Date"] = todayDate
    makeTodayMealization[Location[0]] = {
        Location[1] : capsule[0]
    }
    makeTodayMealization[Location[2]] = {
        Location[3] : capsule[1],
        Location[4] : capsule[2],
        Location[5] : capsule[3],
        Location[6]+"_1" : capsule[4],
        Location[7]+"_2" : capsule[5],
        Location[8]+"_1" : capsule[6],
        Location[9]+"_2" : capsule[7],
        Location[10] : capsule[8],
    }
    makeTodayMealization[Location[11]] = {
        Location[12] : capsule[9],
        Location[13] :  capsule[10],
        Location[14] : capsule[11]
    }
    makeTodayMealization[Location[15]] = {
        Location[16] : capsule[12],
        Location[17] : capsule[13]
    }
    saveAsJSON(makeTodayMealization)
