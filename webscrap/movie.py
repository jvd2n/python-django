from bs4 import BeautifulSoup
from urllib.request import urlopen


class Movie(object):
    url = ''

    def __str__(self):
        return self.url

    def set_url(self):
        self.url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94'
        # self.url = input('url? ')

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_rank = 0
        print('< 현재 상영 영화 / 평점 >')
        for i, j in zip(soup.find_all("div", attrs=({'class': 'title _ellipsis'})),
                        soup.find_all("span", attrs=({'class': 'num'}))):
            n_rank += 1
            print(f'{n_rank}\' {i.find("a").text} ★{j.text}')

    @staticmethod
    def main():
        movie = Movie()
        while 1:
            menu = input('1 input 2 output 0 exit\n>> ')
            if menu == '1':
                movie.set_url()
            elif menu == '2':
                movie.scrap()
            elif menu == '0':
                break
            else:
                continue


Movie.main()
