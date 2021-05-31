from titanic.views.controller import Controller
from titanic.templates.plot import Plot


if __name__ == '__main__':
    print('\'Hello!\'')
    while 1:
        m = input('[1] Data Visualization\n'
                  '[2] Modeling\n'
                  '[3] Machine Learning\n'
                  '[4] Machine Release\n'
                  '[0] Exit\n'
                  '>> ')
        if m == '0':
            print('\'Bye!\'')
            break
        elif m == '1':
            plot = Plot('train.csv')
            # plot.draw_survived_dead()
            # plot.draw_pclass()
            # plot.draw_sex()
            plot.draw_embarked()
        elif m == '2':
            ctrl = Controller()
            r = ctrl.modeling('train.csv', 'test.csv')
            # r = ctrl.preprocess('train.csv', 'test.csv')
            print(type(r.train))
            print(type(r.test))
            print(r.train)
        elif m == '3':
            pass
        elif m == '4':
            pass
        else:
            continue
