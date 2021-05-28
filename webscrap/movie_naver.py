from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd


class MovieRank(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date='
    cls = []
    driver = 'C:/Program Files/Google/Chrome/chromedriver'
    soup = None
    title_ls = []
    mv_dt = {}
    mv_df = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}').text
        self.soup = BeautifulSoup(self.url, 'lxml')
        ls = self.soup.find_all(name='div', attrs=({"class": "tit3"}))
        for i in ls:
            self.title_ls.append(i.find("a").text)

    def get_rank(self):
        print(self.title_ls)

    def list_to_dict(self):
        for i, j in enumerate(self.title_ls):
            self.mv_dt[i+1] = j
        print(self.mv_dt)

    def dict_to_dataframe(self):
        self.mv_df = pd.DataFrame.from_dict(self.mv_dt, orient='index')
        print(self.mv_df)

    @staticmethod
    def main():
        mr = MovieRank()
        while 1:
            m = input('1 input_Date  2 get_Rank\n'
                      '3 rank List to Dict\n'
                      '4 rank Dict to DataFrame'
                      '0 Exit\n>> ')
            if m == '0':
                break
            elif m == '1':
                detail = input('ex)20210527 >> ')
                mr.set_url(detail)
            elif m == '2':
                mr.get_rank()
            elif m == '3':
                mr.list_to_dict()
            elif m == '4':
                mr.dict_to_dataframe()
            else:
                continue


MovieRank.main()
