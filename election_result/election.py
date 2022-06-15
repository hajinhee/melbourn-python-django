import pandas as pd

from context.domains import Reader, File
import folium
import numpy as np
from sklearn import preprocessing


class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. crime_in_seoul.csv, 구글맵 API 를 이용해서 서울시내 경찰서 주소목록파일을 작성하시오.')
            print('2. us-states.json, us_unemployment.csv 를 이용해서 미국 실업률 지도를 작성하시오.')
            print('3. cctv_in_seoul.csv, pop_in_seoul.csv 를 이용해서 서울시내 경찰서 주소목록파일(cctv_pop.csv)을 작성하시오.')
            print('4. police_pos.csv 를 이용해서 경찰서 범죄 검거율 정규화파일(police_norm.csv)을 작성하시오.')
            print('5. 서울시내 경찰서 범죄발생과 검거율 현황지도(polium)를 작성하시오.')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.save_police_pos()
            if menu == '2':
                self.folium_test()
            if menu == '3':
                self.save_cctv_pos()
            if menu == '4':
                self.save_police_norm()
            if menu == '5':
                self.draw_crime_map()
            elif menu == '0':
                break
