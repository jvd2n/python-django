from titanic.views.controller import Controller


if __name__ == '__main__':

    ctrl = Controller()
    while 1:
        m = input('1 Pre-Process\n'
                  '0 Exit\n'
                  '>> ')
        if m == '0':
            break
        elif m == '1':
            ctrl.preprocess('train.csv')
        elif m == '2':
            pass
        else:
            continue
