# -*- coding: utf-8 -*-
"""전기차프로젝트.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D_H_6A4f3AHhuXhAy8Ys5R2Hd1p8rznm

# 1. 설치 현황, 전기차 충전소 정보

**패키지 설치 및 로드하기**
"""

import csv
import pandas as pd
import folium

"""**데이터 프레임변환**"""

df_isnull = pd.read_csv('/content/전기자동차_위도경도.csv',  encoding = 'cp949') 
df = df_isnull.dropna(how='any', axis = 0)

"""**데이터 검토하기**"""

print(df)

"""**지도 생성**"""

smap = folium.Map(location=[36.437795 , 127.423688],titles="Stamen Terrian", zoom_start=8)

"""**생성된 지도에 마크표시**"""

for name, lat, lng in zip(df.충전소명, df.위도, df.경도) :
  folium.Marker([lat, lng], popup=name).add_to(smap)
smap

"""#2. 지역별 전기자동차 현황

**패키지 설치 및 로드하기**
"""

import pandas as pd
import folium

"""**데이터 프레임 변환**"""

df=pd.read_csv('/content/서울전기차대수.csv', encoding='cp949')#utf8 , cp949

"""**데이터 출력**"""

print(df)

"""**패키지 설치 및 로드하기**"""

import requests
import json
import re

"""**서울 행정 구역 json**"""

s_geo='https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'

"""**지도 불러오기**"""

s_map = folium.Map(location=[37.559984,126.9753071],
                   tiles='Stamen Terrain', zoom_start=11)

"""**지도**"""

folium.Choropleth(geo_data=s_geo, data=df, columns=['시군구명', '전기차수'], 
                  fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3, 
                  threshold_scale=[0, 250, 500, 1000, 1500, 2000, 3000, 40000], 
                  key_on='feature.properties.name').add_to(s_map)

s_map

"""#3. 지역별 전기자동차 증가

**폰트설치**
"""

!apt-get update -qq
!apt-get install fonts-nanum* -qq

"""**한글 폰트 설치**"""

import matplotlib.font_manager as fm
fm._rebuild()

import matplotlib.pyplot as plt
plt.rc('font',family="NanumGothic")

"""**CSV 파일 업로드**"""

from google.colab import files
import pandas as pd
import seaborn as sns
loaded = files.upload()
df=pd.read_csv('지역별충전소정보.csv',encoding='949')
print(df)

"""**index_col을 연도별로 설정**"""

df=pd.read_csv('지역별충전소정보.csv',encoding='949',index_col='연도')
print(df)

"""**연도별 증가 그래프**"""

car_plot = df.plot(grid=True, style = ['','g:*','','','','','','','b:*','','','r:*','','','','','']
)
car_plot.set_xticks([2017,2018,2019,2020,2021])
car_plot.set_xlabel('연도')
car_plot.set_ylabel('충전소설치')
car_plot.set_title('충전소정보')

plt.show()

"""**연도별 전기차량 증가**"""

from google.colab import files
import pandas as pd
loaded = files.upload()
df=pd.read_csv('연도별전기차증가.csv',encoding='949')
print(df)

"""**index_col을 기준일로 설정**"""

df=pd.read_csv('연도별전기차증가.csv',encoding='949',index_col='기준일')
print(df)

"""**연도별 전기차 증가 그래프**"""

car_plot = df.plot(grid=True, style = ['','','','','','','','','','','','','','','','','','r:*'])

car_plot.set_xticks([2019,2020,2021,2022])
car_plot.set_xlabel('기준일')
car_plot.set_ylabel('차량 수')
car_plot.set_title('연도별 전기차 증가')

plt.show()