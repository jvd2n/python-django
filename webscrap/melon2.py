class Melon(object):
    url = ''

    def set_url(self, url):
        self.url = url

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('1 2 0 EXIT\n>> ')
