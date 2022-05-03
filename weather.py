# coding: utf-8

import requests
from bs4 import BeautifulSoup

URL = "https://weather.yahoo.co.jp/weather/"

# HTMLの取得
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")

# タグの解析
data = soup.find("div", "mapJp").findAll("li", "point")

result = {}
for i, value in enumerate(data):
  name = value.find("dt").text
  weather = value.find("p", "icon").find("img")["alt"] # altをとりたい
  temp_high = value.find("p", "temp").find("em", "high").text
  temp_low = value.find("p", "temp").find("em", "low").text
  precip = value.find("p", "precip").text

  result[i] = {
      'name':       name,
      'weather':    weather,
      'temp_high':  temp_high,
      'temp_low':   temp_low,
      'precip':     precip
  }

# 表示
for i, num in enumerate(result):
  for num2, key in enumerate(result[i]):
    print (key, result[i][key])
