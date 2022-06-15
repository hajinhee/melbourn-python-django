from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from icecream import ic

from context.domains import Reader, File

'''
자연어 처리 4단계
1. Preprocessing(전처리) => 텍스트 마이닝
2. Tokenization(토큰화)
3. Token Embedding(토큰 임베딩)
4. Document Embedding(데이터 임베딩) ⇒ 벡터화[ ]
'''


class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './save/'
        self.movie_comments = pd.DataFrame()

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. 텍스트 마이닝(크롤링)')
            print('2. preprocess')

            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.crawling()
            if menu == '2':
                self.preprocess()
            elif menu == '0':
                break

    def preprocess(self):
        self.stereotype()
        ic(self.movie_comments.head(5))
        ic(self.movie_comments)

    def crawling(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        f = open(path, 'w', encoding='UTF-8')

        for no in range(1, 501):
            url = 'https://movie.naver.com/movie/point/af/list.naver?&page=%d' % no
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')

            reviews = soup.select('tbody > tr > td.title')
            for rev in reviews:
                title = rev.select_one('a.movie').text.strip()
                score = rev.select_one('div.list_netizen_score > em').text.strip()
                comment = rev.select_one('br').next_sibling.strip()

                # -- 긍정/부정 리뷰 레이블 설정
                if int(score) >= 8:
                    label = 1  # -- 긍정 리뷰 (8~10점)
                elif int(score) <= 4:
                    label = 0  # -- 부정 리뷰 (0~4점)
                else:
                    label = 2

                f.write(f'{title}\t{score}\t{comment}\t{label}\n')
        f.close()

    #
    #
    #     본인 환경에 맞게 설치 경로 변경할 것
    #
    #     df_data = pd.DataFrame(data)
    #
    #
    #     # 코멘트가 없는 리뷰 테이터(NaN) 삭제
    #     df_reviews = df_data.dropna()
    #     # 중복 리뷰 삭제
    #     df_reviews = df_reviews.drop_duplicates(['comment'])
    #
    #     df_reviews.info()
    #     print(df_reviews.head(10))
    #     return df_reviews
    #
    # def check_info(self):
    #     # 영화 리스트 확인
    #     print('-------------- 영화 리스트 확인 --------------')
    #     df_reviews = self.preprocess()
    #     movie_lst = df_reviews.title.unique()
    #     print('전체 영화 편수 =', len(movie_lst))
    #     print(movie_lst[:10])
    #
    #     # 각 영화 리뷰 수 계산
    #     print('-------------- 각 영화 리뷰 수 계산 --------------')
    #     cnt_movie = df_reviews.title.value_counts()
    #     print(cnt_movie[:20])
    #
    #     # 각 영화 평점 분석
    #     print('-------------- 각 영화 평점 분석 --------------')
    #     info_movie = df_reviews.groupby('title')['score'].describe()
    #     print(info_movie.sort_values(by=['count'], axis=0, ascending=False))
    #
    #     # 긍정, 부정 리뷰 수
    #     print('-------------- 긍정, 부정 리뷰 수 --------------')
    #     print(df_reviews.label.value_counts())
    #
    # def visualize_data(self):
    #     df_reviews = self.preprocess()
    #     top10 = df_reviews.title.value_counts().sort_values(ascending=False)[:10]
    #     top10_title = top10.index.tolist()
    #     top10_reviews = df_reviews[df_reviews['title'].isin(top10_title)]
    #     print(top10_title)
    #     print(top10_reviews.info())

    def stereotype(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        self.movie_comments = pd.read_csv(path, delimiter='\t',
                               names=['title', 'score', 'comment', 'label'])

    def tokenization(self):
        pass

    def embedding(self):
        pass


if __name__ == '__main__':
    Solution().hook()

