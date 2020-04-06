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

#Convert Dictionary to json
dirCode = os.getcwd()
def saveAsJSON(jsonStr):
    #save at same directory with code
    with open('HongikUnivSeoulCampusCafeteria.json', 'w', encoding="utf-8") as make_file:
        json.dump(jsonStr, make_file, ensure_ascii=False, indent="\t") #indent -> Indentation parameter


# URL
seoul_campus = "http://apps.hongik.ac.kr/food/food.php"
# return index of date. Mon -> 0 ~ Sun -> 6
n = time.localtime().tm_wday

html = urlopen(seoul_campus)
bs = BeautifulSoup(html, 'html.parser')



collect_sub_titles = bs.findAll('tr', {"class": "subtitle"})

subtitleList = []
for sl in collect_sub_titles:
    subtitleList.append(re.sub('\n','',sl.text).split('[')[0].strip())
collect_price = bs.findAll('th')

priceList = []
for pl in collect_price:
    priceList.append(pl.text)
priceList = priceList[7:]#앞의 불필요한 값들은 제외
collect_menuInformation = bs.findAll('div',{'class' : 'daily-menu'})

menuList = []
for cm in collect_menuInformation:
    menuList.append(re.sub('\n','',cm.text).split('\r'))
makeTodaySchoolMealization = dict()

capsule = []

todayDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
makeTodaySchoolMealization["Date"] = todayDate
if n == 6: #요일이 일요일인 경우에는 scrape할 값이없다.
    makeTodaySchoolMealization[subtitleList[0]] = {
        priceList[0]: [],
        priceList[1]: []
    }
    makeTodaySchoolMealization[subtitleList[1]] = {
        priceList[2]: [],
        priceList[3]: []
    }
    # 점심(11:30~14:30) 값이 두번있어서 키 중복 방지를 위해 "_"를 붙여준것이다.
    makeTodaySchoolMealization[subtitleList[2]] = {
        priceList[4]: [],
        priceList[5]: [],
        priceList[6] + "_": [],
        priceList[7]: []
    }
    saveAsJSON(makeTodaySchoolMealization)
else:
    for t in range(0, len(menuList)):
        if t % 6 == n:
            capsule.append(menuList[t])
        else:
            pass
    makeTodaySchoolMealization[subtitleList[0]] = {
        priceList[0] : capsule[0],
        priceList[1]: capsule[1]
    }
    makeTodaySchoolMealization[subtitleList[1]] = {
        priceList[2]: capsule[2],
        priceList[3]: capsule[3]
    }
    # 점심(11:30~14:30) 값이 두번있어서 키 중복 방지를 위해 "_"를 붙여준것이다.
    makeTodaySchoolMealization[subtitleList[2]] = {
        priceList[4]: capsule[4],
        priceList[5]: capsule[5],
        priceList[6] + "_": capsule[6],
        priceList[7]: capsule[7]
    }
    saveAsJSON(makeTodaySchoolMealization)

#makeTodaySchoolMealization 변수가 최종적으로 오늘의 학식 정보를 가진 딕셔너리 변수이다.
#json형태
'''
{
    "Date": "2020-04-06",
    '학생회관식당': {
                        '점심(4,200원)': ['쌀밥', '참치김치찌개', '간장불고기', '양배추/쌈장', '콩나물무침', '김치', '야채샐러드', '드레싱'], 
                        '저녁(4,200원)': ['쌀밥', '배추된장국', '오징어당면볶음', '돈육동그랑땡조림', '부추겉절이', '김치', '야채샐러드', '드레싱']
                    }, 
    '교직원식당': {
                    '점심 (6,000원)': ['흑미밥', '오징어뭇국', '제육볶음', '고구마맛탕', '참나물겉절이', '콩나물무침', '김치/매실차/조미김', '샐러드/드레싱'], 
                    '저녁 (6,000원)': ['1월 20일(월)부터 ~ 4월 10일(금)까지', '석식 운영하지 않습니다^^']
                   }, 
    '제2기숙사 식당': {
                        '아침(8:00~9:00)': [''], 
                        '점심(11:30~14:30)': ['쌀밥', '김치어묵국', '닭도리탕', '비엔나야채볶음', '명엽채조림', '유채무침', '포기김치', '야채샐러드'], 
                        '점심(11:30~14:30)_': ['쌀밥', '김치어묵국', '순살돈까스', '토마토스파게티', '콩나물냉채', '유채생채', '포기김치', '야채샐러드'], 
                        '저녁(17:30~18:50)': ['쌀밥', '미역국', '제육볶음', '또띠아피자', '고구마맛탕', '얼갈이겉절이', '포기김치', '야채샐러드']
                     }
}

'''