from bs4 import BeautifulSoup


class BsDemo(object):
    html_doc = ''

    def __str__(self):
        return {self.html_doc}

    @staticmethod
    def main():
        bs = BsDemo()
        while 1:
            print('=' * 10 + ' MENU ' + '=' * 10)
            m = input('1 Input HTML  2 Prettify\n3 Print TITLE\n0 EXIT\n>> ')
            if m == '1':
                bs.html_doc = """<html><head><title>The Dormouse's story</title></head>
                <body>
                <p class="title"><b>The Dormouse's story</b></p>
                
                <p class="story">Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                and they lived at the bottom of a well.</p>
                
                <p class="story">...</p>
                """
            elif m == '2':
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.prettify())
            elif m == '3':
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.title.string)
                print('='*40)
                print(soup.a)
                print(soup.find(id="link2"))
                print(soup.find(id="link3"))
                print('='*40)
                print(soup.find_all('a'))
                print('='*40)
                for link in soup.find_all('a'):
                    print(link.get('href'))
                print('=' * 40)
                print(soup.get_text())
            elif m == '0':
                break


BsDemo.main()
