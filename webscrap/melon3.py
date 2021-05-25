import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon3(object):
    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0'}

    class_name = []

    def set_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_ranking(self):
        req = urllib.request.Request(self.url, headers=self.hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')

        ls = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        for i in ls:
            print(f'{i.find("a").text}')

    @staticmethod
    def main():
        b = Melon3()
        while 1:
            menu = input('1 Input 2 Output 0 EXIT')
            if menu == '1':
                b.set_url(input('url? '))
            elif menu == '2':
                pass
            elif menu == '0':
                break


Melon3.main()
