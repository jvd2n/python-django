import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Melon(object):
    url = ''

    def __str__(self):
        return self.url

    def scrap(self):
        n_rank = 0
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(self.url, headers=hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        # soup = BeautifulSoup(urlopen(melon.url), 'lxml')

        # lst50 = soup.select('.lst50,.lst100')
        print(f'Input URL is {self.url}\n')
        print('-' * 40 + ' RANK TOP 100 ' + '-' * 40)
        for i, j in zip(soup.find_all('div', attrs={"class": "ellipsis rank01"}),
                        soup.find_all('div', attrs={"class": "ellipsis rank02"})):
            n_rank += 1
            print(f'{str(n_rank).rjust(3, "0")}\' '
                  f'{i.find("a").text} - {j.find("a").text}')

        # for i in lst50:
        #     n_rank += 1
        #     print(f'{str(n_rank).rjust(3, "0")}\' '
        #           f'{i.select_one(".ellipsis.rank01").a.text} '
        #           f'- {i.select_one(".ellipsis.rank02").a.text}')
        #     if n_rank % 10 == 0:
        #         print('-' * 94)

    # https://www.melon.com/chart/day/index.htm

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            print('=' * 10 + ' MENU ' + '=' * 10)
            menu = input('1 INPUT_URL  2 RANK Top100 \n0 EXIT \n>> ')
            if menu == '1':
                # melon = melon(input('URL? '))
                # melon.url = input('URL? ')
                melon.url = 'https://www.melon.com/chart/day/index.htm'
            elif menu == '2':
                melon.scrap()
            elif menu == '0':
                exit()
            else:
                print('Wrong Number')
                continue


Melon.main()
