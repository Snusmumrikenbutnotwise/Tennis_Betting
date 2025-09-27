#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:24:30 2024

@author: admin
"""

import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd
from datetime import datetime
import csv

file = open("atp_s_links.csv", "r")
Links = list(csv.reader(file, delimiter=","))
file.close()
def ListMaker(data):
    lst=list(data)[0:-1]
    for i in range(0,len(lst)):
        lst[i]=str(lst[i])
        lst[i]=lst[i].replace('class=','').replace('<td','').replace('tl','').replace('tr', '').replace('</td>','').replace('"">','')
    try:
        lst[0]=int(lst[0].replace('.', ''))
    except:
        lst[0]='none'
    try:
        lst[1]=datetime.strptime(lst[1].strip(), "%d. %m. %Y")
    except:
        lst[1]='none'
    try:
        lst[2]=float(lst[2].replace(" cm", ''))
    except:
        lst[2]='none'
    try:
        lst[3]=float(lst[3].replace(' kg', ''))
    except:
        lst[3]='none'
    try:
        lst[4]=lst[4].replace(' ','')
        if lst[4]=='right':
            lst[4]=1
        else:
            lst[4]=0 
    except:
        lst[4]='none'
    return lst

cookies = {
    '_sg_b_v': '1%3B46%3B1729874170',
    '_sg_b_n': '1729874190871',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Oct+25+2024+18%3A36%3A10+GMT%2B0200+(Central+European+Summer+Time)&version=202409.1.0&browserGpcFlag=0&isIABGlobal=false&consentId=c387c48a-ed2d-4739-9d90-560f79fa7446&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CV2STACK42%3A1&hosts=H194%3A1%2CH198%3A1%2CH203%3A1%2CH317%3A1%2CH16%3A1%2CH190%3A1%2CH21%3A1%2CH201%3A1%2CH99%3A1%2CH473%3A1%2CH281%3A1%2CH154%3A1&genVendors=V2%3A1%2C&intType=1&geolocation=PL%3B14&AwaitingReconsent=false',
    '_ga': 'GA1.1.1813358545.1729874034',
    '_ga_401YC6BRS1': 'GS1.1.1729874033.1.1.1729874170.58.0.0',
    'optimizelyEndUserId': 'oeu1729874170727r0.6370843414303046',
    '_sg_b_p': '%2Fresults%2F',
    'idx_last_game_tab': 'lstGame-1',
    'idx_mutual_tab': 'mutPlayer-1',
    'idx_profile_tab': 'plProfile-1',
    'OptanonAlertBoxClosed': '2024-10-25T16:36:08.308Z',
    'eupubconsent-v2': 'CQHC6HAQHC6HAAcABBENBMFsAP_gAAAAAChQKhtX_G__bWlr8X73aftkeY1P99h77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIAu3TBIQNlGJDURVCgaogVryDMaEyUgTNKJ6BkiFMRM2dYCF5vm4tj-QCY5vp991dx2B-t7dr83dzyy41Hn3a5_2a0WJCdA5-tDfv9bROb-9IOd_x8v4v8_F_pE2_eT1l_tWvp7B9-cts7_XW89_fff_9PFcQuB_-_3_uAAAAQJABAXmOgAgLzJQAQF5lIAIC8wAAA.f_wAAAAAAAAA',
    'my_cookie_hash_2': '171c92e355622e52a46033b96491e237',
    'my_cookie_id_2': '2363663217',
    'my_timezone': '%2B1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    # 'Cookie': '_sg_b_v=1%3B46%3B1729874170; _sg_b_n=1729874190871; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+25+2024+18%3A36%3A10+GMT%2B0200+(Central+European+Summer+Time)&version=202409.1.0&browserGpcFlag=0&isIABGlobal=false&consentId=c387c48a-ed2d-4739-9d90-560f79fa7446&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CV2STACK42%3A1&hosts=H194%3A1%2CH198%3A1%2CH203%3A1%2CH317%3A1%2CH16%3A1%2CH190%3A1%2CH21%3A1%2CH201%3A1%2CH99%3A1%2CH473%3A1%2CH281%3A1%2CH154%3A1&genVendors=V2%3A1%2C&intType=1&geolocation=PL%3B14&AwaitingReconsent=false; _ga=GA1.1.1813358545.1729874034; _ga_401YC6BRS1=GS1.1.1729874033.1.1.1729874170.58.0.0; optimizelyEndUserId=oeu1729874170727r0.6370843414303046; _sg_b_p=%2Fresults%2F; idx_last_game_tab=lstGame-1; idx_mutual_tab=mutPlayer-1; idx_profile_tab=plProfile-1; OptanonAlertBoxClosed=2024-10-25T16:36:08.308Z; eupubconsent-v2=CQHC6HAQHC6HAAcABBENBMFsAP_gAAAAAChQKhtX_G__bWlr8X73aftkeY1P99h77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIAu3TBIQNlGJDURVCgaogVryDMaEyUgTNKJ6BkiFMRM2dYCF5vm4tj-QCY5vp991dx2B-t7dr83dzyy41Hn3a5_2a0WJCdA5-tDfv9bROb-9IOd_x8v4v8_F_pE2_eT1l_tWvp7B9-cts7_XW89_fff_9PFcQuB_-_3_uAAAAQJABAXmOgAgLzJQAQF5lIAIC8wAAA.f_wAAAAAAAAA; my_cookie_hash_2=171c92e355622e52a46033b96491e237; my_cookie_id_2=2363663217; my_timezone=%2B1',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'navigate',
    'Host': 'www.tennisexplorer.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Connection': 'keep-alive',
}

#Links=['match-detail/?id=2525147']
AllData=[]
BlockedLinks=[]
for link in Links[38146:]:
    try:
        try:
            response = requests.get('https://www.tennisexplorer.com'+link[0], cookies=cookies, headers=headers, timeout=10)
        except:
            BlockedLinks.append(link)
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            L=ListMaker(soup.find_all('td', class_="tl")[0:6])
        except:
            print("L")
        try:
            R=ListMaker(soup.find_all('td',class_="tr")[0:6])
        except:
            print('R')
        try:
            date=soup.find_all('div', class_='box boxBasic lGray' )
        except:
            print('olabogakurkasroga')
        try:
            avgL=float(str(soup.find_all('tr', class_='average')[0])[79:83])
            avgR=float(str(soup.find_all('tr', class_='average')[0])[131:135])
        except:
            avgL='none'
            avgR='none'
        try:
            date=datetime.strptime(str(date[1])[52:62],'%d.%m.%Y')
        except:
            print("tu jest problem")
        L.append(avgL)
        R.append(avgR)
        try:
            LR=L+R
        except:
            print(L)
            print(R)
        LR.append(date)
        AllData.append(LR)
    except Exception as error:
        print(error)

with open('BIGTENNISENERGYATPSINGLES', 'w') as f:
    write=csv.writer(f)
    write.writerows(AllData)

with open('BlockedLinksAtpSingles', 'w') as f:
    write=csv.writer(f)
    write.writerows(BlockedLinks)



