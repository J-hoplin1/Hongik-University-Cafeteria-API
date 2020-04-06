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

def seoulCampus():
    # URL
    seoul_campus = "http://apps.hongik.ac.kr/food/food.php"
    # return index of date. Mon -> 0 ~ Sun -> 6
    n = time.localtime().tm_wday

    html = urlopen(seoul_campus)
    bs = BeautifulSoup(html, 'html.parser')

    collect_sub_titles = bs.findAll('tr', {"class": "subtitle"})

    subtitleList = []
    for sl in collect_sub_titles:
        subtitleList.append(re.sub('\n', '', sl.text).split('[')[0].strip())
    collect_price = bs.findAll('th')

    priceList = []
    for pl in collect_price:
        priceList.append(pl.text)
    priceList = priceList[7:]  # 앞의 불필요한 값들은 제외
    collect_menuInformation = bs.findAll('div', {'class': 'daily-menu'})

    menuList = []
    for cm in collect_menuInformation:
        menuList.append(re.sub('\n', '', cm.text).split('\r'))
    makeTodaySchoolMealization = dict()

    capsule = []

    makeTodaySchoolMealization["Date"] = todayDate
    if n == 6:  # 요일이 일요일인 경우에는 scrape할 값이없다.
        makeTodaySchoolMealization[subtitleList[0]] = {
            priceList[0]: "",
            priceList[1]: ""
        }
        makeTodaySchoolMealization[subtitleList[1]] = {
            priceList[2]: "",
            priceList[3]: ""
        }
        # 점심(11:30~14:30) 값이 두번있어서 키 중복 방지를 위해 "_"를 붙여준것이다.
        makeTodaySchoolMealization[subtitleList[2]] = {
            priceList[4]: "",
            priceList[5] + "_1": "",
            priceList[6] + "_2": "",
            priceList[7]: ""
        }
        final_json = json.dumps(makeTodaySchoolMealization)
        return final_json
    else:
        for t in range(0, len(menuList)):
            if t % 6 == n:
                capsule.append(menuList[t])
            else:
                pass
        makeTodaySchoolMealization[subtitleList[0]] = {
            priceList[0]: capsule[0],
            priceList[1]: capsule[1]
        }
        makeTodaySchoolMealization[subtitleList[1]] = {
            priceList[2]: capsule[2],
            priceList[3]: capsule[3]
        }
        # 점심(11:30~14:30) 값이 두번있어서 키 중복 방지를 위해 "_"를 붙여준것이다.
        makeTodaySchoolMealization[subtitleList[2]] = {
            priceList[4]: capsule[4],
            priceList[5] + "_1": capsule[5],
            priceList[6] + "_2": capsule[6],
            priceList[7]: capsule[7]
        }
        final_json = json.dumps(makeTodaySchoolMealization)
        return final_json