# *****************
# *** Data Type ***
# *****************

"""
Python has Five standard types
Scalar
    Numbers : int, float, complex
    String : str
Vector
    Collection : List, Tuple, Dictionary, Set
"""

hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])
"""
Python List
"""
ls = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

# Create : ls에 '100'을 추가 Create
ls.append(100)

# Read : ls의 목록을 출력
print(ls)

# Update : ls와 tinyls의 결합
print(ls + tinylist)
ls.extend(tinylist)

# Delete : ls에서 786을 제거
del ls[ls.index(786)]
print(ls)


# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create
tplist = list(tp)
tplist.append(100)
tp = tuple(tplist)
# Read: tp 의 목록을 출력
print(tp)
# Update: tp와 tinytp 의 결합
print(tp+tinytp)
tpl = list(tp)
ttpl = list(tinytp)
tpl.extend(ttpl)
tp = tuple(tpl)
print(tp)
# Delete: tp 에서 786을 제거
tpl = list(tp)
del tpl[tpl.index(786)]
tp = tuple(tpl)
print(tp)


# dictionary CRUD Example
dt = {'abcd': 786, 'john': 70.2}
tinydt = {'홍': '30세'}
# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt['tom'] = 100
# Read: dt 의 목록을 출력
print(dt)
# Update: dt와 tinydt 의 결합
# dt.update(tinydt)
# print(dt)
merged = {**dt, **tinydt}
print(merged)
# Delete: dt 에서 'abcd' 제거
del dt['abcd']
print(dt)
