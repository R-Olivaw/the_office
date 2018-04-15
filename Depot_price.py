# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:50:23 2018

@author: Alex
"""

import requests
from bs4 import BeautifulSoup

def stock_price_checker():
    print("\nChecking stock prices...\n")
    url1 = 'https://www.msn.com/en-us/money/stockdetails?symbol=US:ODP'
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.text, 'html.parser')
        
    card1 = soup1.find(class_='precurrentvalue')
            
    price_ob1 = card1.find('span')
    price_num1 = price_ob1.contents
    price_int1 = float(price_num1[0])
    depot_price1 = str(price_num1[0])
            
    print("Office Depot:", '${:.2f}'.format(float(depot_price1)))
            
    url2 = 'https://www.msn.com/en-us/money/stockdetails/fi-126.1.GPS.NYS?symbol=GPS&form=PRFIHQ'
    page2 = requests.get(url2)
    soup2 = BeautifulSoup(page2.text, 'html.parser')
            
    card2 = soup2.find(class_='precurrentvalue')
            
    price_ob2 = card2.find('span')
    price_num2 = price_ob2.contents
    price_int2 = float(price_num2[0])
    scott_price2 = str(price_num2[0])
            
    print("Michael Scott Paper Company:", '${:.2f}'.format(float(scott_price2)))
            
    url3 = 'https://www.msn.com/en-us/money/stockdetails/fi-126.1.TGT.NYS?symbol=TGT&form=PRFIHQ'
    page3 = requests.get(url3)
    soup3= BeautifulSoup(page3.text, 'html.parser')
            
    card3 = soup3.find(class_='precurrentvalue')
            
    price_ob3 = card3.find('span')
    price_num3 = price_ob3.contents
    price_int3 = float(price_num3[0])
    dunder_price3 = str(price_num3[0])
            
    print("Dunder Mifflin:", '${:.2f}'.format(float(dunder_price3)))
    
    if price_int3 > price_int1 and price_int3 > price_int2:
        print("\nAnother great day to be a Dunder Mifflin employee!")
    else:
        print("\nWell, the economy goes up and down...")
        
stock_price_checker()
