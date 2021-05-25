class Wikipedia(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        while 1:
            menu = input('1.Input_URL 2.Print_URL 3 4 0.EXIT\n>> ')
            if menu == '1':
                wiki = Wikipedia(input('URL? '))
            elif menu == '2':
                print(f'URL : {wiki}')
            elif menu == '3':
                pass
            elif menu == '0':
                break
            else:
                'Wrong Number'


Wikipedia.main()
