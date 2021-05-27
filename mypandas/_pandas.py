import pandas as pd

data = {
    'age': [20, 23, 48],
    'height': [183, 192, 175],
    'weight': [77, 83, 65]
}
index_name = ['수퍼맨', '스파이더맨', '배트맨']

frame = pd.DataFrame(data, index=index_name)
# 특정 열 조회
# print(frame.age)
# 특정 열의 특정 값 조회
print(frame.age[1])

# 특정 행 조회
# print(frame.loc['수퍼맨'])   # 인덱스 네임
# print(frame.iloc[0])  # 인덱스 시퀀스





