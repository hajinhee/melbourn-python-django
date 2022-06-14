from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from icecream import ic

from context.domains import File, Reader
'''
https://blog.diyaml.com/teampost/%EC%9E%90%EC%97%B0%EC%96%B4-%EC%B2%98%EB%A6%AC%EC%9D%98-4%EA%B0%80%EC%A7%80-%EB%8B%A8%EA%B3%84/
1. Preprocessing
2. Tokenization
3. Token Embedding
4. Document Embedding
'''

class Solution(Reader):
    def __init__(self):
        self.okt = Okt()
        self.file = File()
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. kr-Report_2018.txt.txt 를 읽는다.')
            print('2. Tokenization')
            print('3. Token Embedding')
            print('4. Document Embedding')
            print('5. 2018년 삼성사업계획서를 분석해서 워드클라우드를 작성하시오.')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.read_file()
            if menu == '2':
                self.tokenization()
            if menu == '3':
                self.token_embedding()
            if menu == '4':
                self.document_embedding()
            if menu == '5':
                pass
            elif menu == '0':
                break

    def read_file(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        file = self.file
        file.fname = 'kr-Report_2018.txt'
        path = self.new_file(file)
        with open(path, 'r', encoding='utf-8') as f:
            texts = f.read()
        print(texts)
        return texts

    def tokenization(self):
        pass

    def token_embedding(self):
        pass

    def document_embedding(self):
        pass


if __name__ == '__main__':
    Solution().hook()
