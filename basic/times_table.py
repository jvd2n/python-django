"""
구구단 프로그램
"""


class TimesTable(object):
    num = 0
    dict = {}

    def times(self):
        for i in range(1, 10):
            print(f'{self.num} * {i} = {self.num * i}')

    @staticmethod
    def every_times():
        for i in range(2, 10):
            print(f'{i}단 : ', end='')
            for j in range(1, 10):
                print(f'{str(i * j).rjust(2, "0")}  ', end='')
            print()

    def dict_times(self):
        d = self.dict
        for i in range(1, 10):
            # key = f'{self.num}*{i}'
            d[i] = self.num * i
        print('{ OUTPUT DICT }')
        print(d)
        for k in d.keys():
            print(f'{self.num} * {k} = {d.get(k)}')

    @staticmethod
    def main():
        tt = TimesTable()
        while 1:
            print('=' * 9 + ' TIMES TABLE ' + '=' * 9)
            menu = input('1 Select Num 2 Every Num (2-9)\n'
                         '3 Dict Num   0 Exit\n>> ')
            if menu == '1':
                tt.num = int(input('input num >> '))
                tt.times()
            elif menu == '2':
                tt.every_times()
            elif menu == '3':
                tt.num = int(input('input num >> '))
                tt.dict_times()
            elif menu == '0':
                break
            else:
                continue


TimesTable.main()
