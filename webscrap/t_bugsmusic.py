from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    soup = BeautifulSoup()
    class_name = ['title', 'artist']
    title_ls = []
    artist_ls = []
    title_dict = {}

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text
        self.soup = BeautifulSoup(self.url, 'lxml')
        self.title_ls = self.soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        self.artist_ls = self.soup.find_all(name='p', attrs=({"class": self.class_name[1]}))

    def get_ranking(self):
        print('------- 제목 --------')
        for i in self.title_ls:
            print(f'{i.find("a").text}')
        print('------ 가수 --------')
        for i in self.artist_ls:
            print(f'{i.find("a").text}')

    def insert_title_dict(self):
        print('------- {\'제목\': \'가수\'} --------')
        for i, j in zip(self.title_ls, self.artist_ls):
            self.title_dict[i.find("a").text] = j.find("a").text
        print(self.title_dict)
        rank = 0
        for i in self.title_dict.keys():
            rank += 1
            print(f'{rank}\' {i} - {self.title_dict[i]}')

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time, 2-output 3-dict')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('상세정보 입력'))  # wl_ref=M_contents_03_01
            elif menu == '2':
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_title_dict()
            else:
                print('Wrong Number')
                continue


BugsMusic.main()
