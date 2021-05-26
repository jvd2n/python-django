class VectorTest(object):
    ls = ['abc', 786, 2.23, 'john', 70.2]
    tp = ('def', 786, 2.23, 'paul', 70.2)
    dict = {'abcd': 786, 'john': 70.2}

    def add_list(self, value):
        self.ls.append(value)
        self.read_list()

    def read_list(self):
        print(f'\n{self.ls}\n')

    def merge_list(self, ls):
        self.ls.extend(ls)
        self.read_list()

    def delete_list(self, value):
        self.ls.remove(value)
        self.read_list()

    def add_tuple(self, value):
        self.tp += value
        print(f'\n{self.tp}\n')

    def read_tuple(self):
        print(f'\n{self.tp}\n')

    def merge_tuple(self, value):
        print(f'\n{self.tp + value}\n')

    def delete_tuple(self, value):
        print('Impossible Logic')

    def add_dict(self, value):
        # self.dict['tom'] = 100
        a = list(value.keys())
        b = list(value.values())
        self.dict[a[0]] = b[0]
        self.read_dict()

    def read_dict(self):
        print(f'\n{self.dict}\n')

    def merge_dict(self, value):
        self.dict.update(value)
        self.read_dict()

    def delete_dict(self, value):
        del self.dict[value]
        self.read_dict()

    @staticmethod
    def main():
        v = VectorTest()
        tinyls = [123, 'john']
        tinytp = (123, 'john')
        tinydt = {'홍': '30세'}

        while 1:
            print('=' * 10 + ' DATA TYPE EXAMPLE ' + '=' * 10 + '\n'
                  'LIST  [ 1 ADD  2 READ  3 MERGE  4 DEL ]\n'
                  'TUPLE ( 5 ADD  6 READ  7 MERGE  8 DEL )\n'
                  'DICT  { 9 ADD 10 READ 11 MERGE 12 DEL }')
            menu = input('0 EXIT >> ')
            if menu == '1':
                # v.add_list(input('value? '))
                v.add_list(100)
            elif menu == '2':
                v.read_list()
            elif menu == '3':
                v.merge_list(tinyls)
            elif menu == '4':
                value = 786
                v.delete_list(value)
            elif menu == '5':
                v.add_tuple((100,))
            elif menu == '6':
                v.read_tuple()
            elif menu == '7':
                v.merge_tuple(tinytp)
            elif menu == '8':
                pass
            elif menu == '9':
                v.add_dict({'tom': 100})
            elif menu == '10':
                v.read_dict()
            elif menu == '11':
                v.merge_dict(tinydt)
            elif menu == '12':
                v.delete_dict('abcd')
            elif menu == '0':
                break
            else:
                print('Wrong Number')
                continue


VectorTest.main()
