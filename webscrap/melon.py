import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):
    url = ''

    def __str__(self):
        return self.url

    # https://www.melon.com/chart/day/index.htm

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            print('=' * 10 + ' MENU ' + '=' * 10)
            menu = input('1 INPUT_URL  2 RANK Top100 \n0 EXIT \n>> ')
            if menu == '1':
                # melon = melon(input('URL? '))
                melon.url = input('URL? ')
            elif menu == '2':
                n_rank = 0
                hdr = {'User-Agent': 'Mozilla/5.0'}
                req = urllib.request.Request(melon.url, headers=hdr)
                html = urllib.request.urlopen(req).read()
                soup = BeautifulSoup(html, 'html.parser')
                # soup = BeautifulSoup(urlopen(melon.url), 'lxml')

                lst50 = soup.select('.lst50,.lst100')
                print(f'Input URL is {melon}\n')
                print('-' * 40 + ' RANK TOP 100 ' + '-' * 40)
                for li1 in lst50:
                    n_rank += 1
                    print(f'{str(n_rank).rjust(3, "0")}\' '
                          f'{li1.select_one(".ellipsis.rank01").a.text} '
                          f'- {li1.select_one(".ellipsis.rank02").a.text}')
                    if n_rank % 10 == 0:
                        print('-' * 94)
            elif menu == '0':
                exit()
            else:
                print('Wrong Number')
                continue


Melon.main()
