import pandas as pd


class Conversion(object):

    # def __str__(self):
    #     return f'i = {self.i}\n' \
    #            f'f = {self.f}\n' \
    #            f's = {self.s}\n' \
    #            f'ls = {self.ls}\n' \
    #            f'dt = {self.dt}\n' \
    #            f'tp = {self.tp}'

    @staticmethod
    def create_tuple() -> ():   # -> () : 리턴 타입 명시
        return tuple(range(1, 11))

    @staticmethod
    def tp_to_ls(tp) -> []:
        return list(tp)

    @staticmethod
    def int_to_float(ls) -> []:
        return [float(i) for i in ls]

    @staticmethod
    def float_to_int(ls) -> []:
        return [int(i) for i in ls]

    @staticmethod
    def list_to_dict(ls) -> {}:
        # dt = {}
        # for i in range(10):
        #     dt[str(i)] = ls[i]
        return dict(zip([str(i) for i in ls], ls))

    @staticmethod
    def str_to_tuple() -> ():
        return tuple('hello')

    @staticmethod
    def dt_to_df(dt):
        # 1
        index_name = ['int']
        return pd.DataFrame.from_dict(dt, orient='index')

    @staticmethod
    def main():
        # i = 0
        # f = 0.0
        # s = ''
        ls = []
        dt = {}
        tp = ()
        # df = pd.DataFrame()
        c = Conversion()
        while 1:
            m = input('1-create tuple           2-convert list\n'
                      '3-int_to_float           4-convert int-list\n'
                      '5-list convert dict      6-str convert tuple\n'
                      '7-str tuple convert list 8-dict_convert_df\n'
                      '0-Exit\n'
                      '>> ')
            if m == '0':
                break
            elif m == '1':  # 1부터 10까지 요소를 가진 튜플을 생성
                tp = c.create_tuple()
                print(f'tp의 타입 : {type(tp)}')
                print(tp)
            elif m == '2':  # 1번 튜플을 리스트로 전환
                ls = c.tp_to_ls(tp)
                print(f'ls의 타입 : {type(ls)}')
                print(ls)
            elif m == '3':  # 2번 리스트를 실수(float) 리스트로 전환
                ls = c.int_to_float(ls)
                print(ls)
            elif m == '4':  # 3번 실수(float) 리스트를 정수 리스트로 전환
                ls = c.float_to_int(ls)
                print(ls)
            elif m == '5':  # 4번 리스트를 딕셔너리로 전환. 인덱스 키는 str로 전환
                dt = c.list_to_dict(ls)
                print(dt)
            elif m == '6':  # 'hello' 를 튜플로 전환
                tp = c.str_to_tuple()
                print(tp)
            elif m == '7':  # 6번 튜플을 리스트로 전환
                ls = c.tp_to_ls(tp)
                print(ls)
            elif m == '8':  # 5번 딕셔너리를 데이터프레임으로 전환
                tp = c.create_tuple()
                ls = c.tp_to_ls(tp)
                dt = c.list_to_dict(ls)
                # dt = {
                #     '1': [1,2,3],
                #     '2': [4,5,6],
                #     '3': [7,8,9]
                # }
                df = c.dt_to_df(dt)
                print(df)
            else:
                continue


Conversion.main()
