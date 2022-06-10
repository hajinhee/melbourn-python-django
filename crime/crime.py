from context.domains import Reader, File
import folium

class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']

    def save_police_pos(self):
        self.file.fname = 'crime_in_seoul'
        crime = self.csv(self.file)
        station_names = []
        for name in crime['관서명']:
            station_names.append(f'서울{str(name[:-1])}경찰서')
        # print(f'station_names range: {len(station_names)}')
        # for i, name in enumerate(station_names):
        #     print(f'name {i} = {name}')
        gmaps = self.gmaps()
        '''
        [{'address_components': 
            [{'long_name': '１７０', 'short_name': '１７０', 'types': ['premise']}, 
            {'long_name': '보문로', 'short_name': '보문로', 'types': ['political', 'sublocality', 'sublocality_level_4']}, 
            {'long_name': '삼선동', 'short_name': '삼선동', 'types': ['political', 'sublocality', 'sublocality_level_2']}, 
            {'long_name': '성북구', 'short_name': '성북구', 'types': ['political', 'sublocality', 'sublocality_level_1']}, 
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']}, 
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']}, 
            {'long_name': '136-045', 'short_name': '136-045', 'types': ['postal_code']}], 
            'formatted_address': '대한민국 서울특별시 성북구 삼선동 보문로 170', 
            'geometry': {'location': 
                {'lat': 37.58977830000001, 'lng': 127.016589}, 
                'location_type': 'ROOFTOP', 
                'viewport': {'northeast': {'lat': 37.59112728029151, 'lng': 127.0179379802915}, 
                'southwest': {'lat': 37.58842931970851, 'lng': 127.0152400197085}}}, 
                'partial_match': True, 'place_id': 'ChIJCzgT1Me8fDURiSAT03pwJPg', 
                'plus_code': {'compound_code': 'H2Q8+WJ 대한민국 서울특별시', 'global_code': '8Q99H2Q8+WJ'}, 
                'types': ['establishment', 'point_of_interest', 'police']}]
        '''
        station_addrs = []
        station_lats = []
        station_lngs = []
        print(station_names[21])
        print('*'*20)
        for i, name in enumerate(station_names):
            if name != '서울종암경찰서':
                temp = gmaps.geocode(name, language='ko')
            else:
                temp = [{'address_components':
            [{'long_name': '１７０', 'short_name': '１７０', 'types': ['premise']},
            {'long_name': '보문로', 'short_name': '보문로', 'types': ['political', 'sublocality', 'sublocality_level_4']},
            {'long_name': '삼선동', 'short_name': '삼선동', 'types': ['political', 'sublocality', 'sublocality_level_2']},
            {'long_name': '성북구', 'short_name': '성북구', 'types': ['political', 'sublocality', 'sublocality_level_1']},
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']},
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']},
            {'long_name': '136-045', 'short_name': '136-045', 'types': ['postal_code']}],
            'formatted_address': '대한민국 서울특별시 성북구 화랑로7길 32',
            'geometry': {'location':
                {'lat': 37.60388169879458, 'lng': 127.04001571848704},
                'location_type': 'ROOFTOP',
                'viewport': {'northeast': {'lat': 37.60388169879458, 'lng': 127.04001571848704},
                'southwest': {'lat': 37.60388169879458, 'lng': 127.04001571848704}}},
                'partial_match': True, 'place_id': 'ChIJCzgT1Me8fDURiSAT03pwJPg',
                'plus_code': {'compound_code': 'H2Q8+WJ 대한민국 서울특별시', 'global_code': '8Q99H2Q8+WJ'},
                'types': ['establishment', 'point_of_interest', 'police']}]
            print(f'name {i} = {temp[0].get("formatted_address")}')

    def save_cctv_pos(self):
        file = self.file
        file.fname = 'cctv_in_seoul'
        cctv = self.csv(file)
        print(cctv)
        file.fname = 'pop_in_seoul'
        pop = self.xls(file, header=2, cols='B, D, G, J, N')
        print(pop)
        # self.csv(self.file).to_csv('../crime/save/.csv', sep=',', na_rep='NaN')

    def save_police_norm(self):
        pass

    def folium_tset(self):
        file = self.file
        file.fname = 'us-states.json'
        states = self.new_file(file)
        file.fname = 'us_unemployment'
        unemployment = self.csv(file)
        bins = list(unemployment["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))
        m = folium.Map(location=[48, -102], zoom_start=3)
        folium.Choropleth(
            geo_data=states, # dataframe 이 아님
            name="choropleth",
            data=unemployment, # 지도 위에 얹을 데이터
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name="Unemployment Rate (%)",
            bins=bins,
            reset=True
        ).add_to(m)
        m.save("./save/folium_test.html")


    def draw_crime_map(self):
        self.file.fname = 'geo_simple'
        a = self.csv(self.file)
        print(a)


if __name__ == '__main__':
    Solution().folium_tset()