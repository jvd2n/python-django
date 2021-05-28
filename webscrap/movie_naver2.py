from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv


class NaverMovie(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = 'tit3'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    rank_dt = {}
    rank_df = None

    def scrap(self):
        drv = webdriver.Chrome(self.driver_path)
        # drv.implicitly_wait(3)
        drv.get(self.url)
        # ls = drv.find_elements_by_class_name('tit3')
        # print(type(ls))
        soup = BeautifulSoup(drv.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class': self.class_name})

        for i, j in enumerate(all_div):
            print(f'{i+1} - {j.find("a").text}')
        self.rank_dt = {str(i+1): j.find("a").text for i, j in enumerate(all_div)}
        # print(self.rank_dt)
        drv.close()

    def dict_to_dataframe(self):
        self.rank_df = pd.DataFrame.from_dict(self.rank_dt, orient='index')
        print(self.rank_df)

    def dataframe_to_csv(self):
        path = './data/movie_naver.csv'
        if not os.path.exists(path):
            self.rank_df.to_csv(path, sep=',', mode='w', encoding='utf-8-sig')
        else:
            self.rank_df.to_csv(path, sep=',', mode='a', encoding='utf-8-sig', header=False)


if __name__ == '__main__':
    naver = NaverMovie()
    # naver.class_name = input('class_name? >> ')
    # naver.scrap()

    # NaverMovie().scrap()
    # NaverMovie() -> dynamic Method 일 경우 ()를 붙여서 인스턴스화한다.

    naver.scrap()
    naver.dict_to_dataframe()
    naver.dataframe_to_csv()
