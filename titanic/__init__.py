import django
from titanic.views.controller import Controller
from titanic.templates.plot import Plot
print(f'Django ver : {django.VERSION}')

if __name__ == '__main__':
    print('\'Hello!\'')
    ctrl = Controller()
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
            df = ctrl.modeling('train.csv', 'test.csv')
        elif m == '3':
            ctrl.learning('train.csv', 'test.csv')
        elif m == '4':
            ctrl.submit('train.csv', 'test.csv')
        else:
            continue
