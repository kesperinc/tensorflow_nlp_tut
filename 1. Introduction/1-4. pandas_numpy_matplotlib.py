# -*- coding: utf-8 -*-
"""Pandas Numpy Matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/147HoS3GOKwDzFDNx2pF7z70XWuo06n9z

링크 : https://wikidocs.net/32829
"""

"""# 1. Pandas"""

"""## 1) Series"""

import pandas as pd

sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])
print(sr)

print(sr.values)

print(sr.index)

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)

print(df.index)  # 인덱스 출력

print(df.columns)  # 열 출력

print(df.values)  # 값 출력

"""## 2) 데이터프레임"""

# 리스트로 생성하기
data = [
    ['1000', 'Steve', 90.72],
    ['1001', 'James', 78.09],
    ['1002', 'Doyeon', 98.43],
    ['1003', 'Jane', 64.19],
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
print(df)

# 딕셔너리로 생성하기
data = {'학번': ['1000', '1001', '1002', '1003', '1004', '1005'],
        '이름': ['Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
        '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]}

df = pd.DataFrame(data)
print(df)

print(df.head(3))  # 앞 부분을 3개만 보기

print(df.tail(3))  # 뒷 부분을 3개만 보기

print(df['학번'])  # '학번'에 해당되는 열을 보기

# csv 파일을 사용하는 경우가 많습니다. csv 파일을 데이터프레임으로 로드 할 때는 다음과 같이 합니다.
# df = pd.read_csv('csv 파일의 경로')

"""# 2. Numpy"""

import numpy as np

a = np.array([1, 2, 3, 4, 5])  # 리스트를 가지고 1차원 배열 생성
print(type(a))
print(a)

b = np.array([[10, 20, 30], [60, 70, 80]])
print(b)  # 출력

print(b.ndim)  # 차원 출력
print(b.shape)  # 크기 출력

print(a.ndim)  # 차원 출력
print(a.shape)  # 크기 출력

a = np.zeros((2, 3))  # 모든값이 0인 2x3 배열 생성.
print(a)

a = np.ones((2, 3))  # 모든값이 1인 2x3 배열 생성.
print(a)

a = np.full((2, 2), 7)  # 모든 값이 특정 상수인 배열 생성. 이 경우에는 7.
print(a)

a = np.eye(3)  # 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성.
print(a)

a = np.random.random((2, 2))  # 임의의 값으로 채워진 배열 생성
print(a)

a = np.arange(10)  # 0부터 9까지
print(a)

a = np.arange(1, 10, 2)  # 1부터 9까지 +2씩 적용되는 범위
print(a)

a = np.array(np.arange(30)).reshape((5, 6))
print(a)

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

b = a[0:2, 0:2]
print(b)

b = a[0, :]  # 첫번째 행 출력
print(b)

b = a[:, 1]  # 두번째 열 출력
print(b)

a = np.array([[1, 2], [4, 5], [7, 8]])
b = a[[2, 1], [1, 0]]  # a[[row2, row1],[col1, col0]]을 의미함.
print(b)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

b = x + y  # 각 요소에 대해서 더함
# b = np.add(x, y)와 동일함
print(b)

b = x - y  # 각 요소에 대해서 빼기
# b = np.subtract(x, y)와 동일함
print(b)

b = b * x  # 각 요소에 대해서 곱셈
# b = np.multiply(b, x)와 동일함
print(b)

b = b / x  # 각 요소에 대해서 나눗셈
# b = np.divide(b, x)와 동일함
print(b)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.dot(a, b)
print(c)

"""# 3. Matplotlib"""

import matplotlib.pyplot as plt

plt.title('test')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.show()

plt.title('test')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.xlabel('hours')
plt.ylabel('score')
plt.show()

plt.title('students')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.plot([1.5, 2.5, 3.5, 4.5], [3, 5, 8, 10])  # 라인 새로 추가
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student'])  # 범례 삽입
plt.show()