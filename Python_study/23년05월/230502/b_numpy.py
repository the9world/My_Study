# 주피터 명령어 https://planharry.tistory.com/22
# *args, **kwargs https://brunch.co.kr/@princox/180
# 리스트 표현식 https://dojang.io/mod/page/view.php?id=2285
# numpy 1 http://bigdata.dongguk.ac.kr/lectures/Python/_book/numpy.html 
# numpy 2 https://laboputer.github.io/machine-learning/2020/04/25/numpy-quickstart/

# numpy란?
# Numerical Python의 약자로 산술계산용 라이브러리
# ndarray(다차원 배열객체) > 빠르고 효율적인 메모리 사용,
# 유연한 브로드스팅

# ndarray란? 
# numpy에서 제공하는 자료구조, N차원의 배열 객체
# 대규모의 데이터 집합을 담을 수 있는 자료구조

# ndarray vs. list
# 연속된 메모리 블록에 데이터를 저장
# 같은 종류의 데이터를 담음
# import random(모듈)
# import pandas (pd)

# import numpy as np

# n=1000000
# numpy_arr = np.arange(n)
# python_list = list(range(n))

# import time
# start = time.time() #시작시간 저장
# python_list = [x**3+10 for x in python_list]
# print('time:', time.time() - start) #현재시각-시작시간 = 실행시간

# """%%time # 안됨
# numpy_arr = numpy_arr**3+10"""

# A = [1,2,3,4]

# a = np.array(A)
# print(type(a))
# print(a)

# # - 벡터화
# #     - 배열은 for문을 작성하지 않고 데이터를 일괄처리 하는 것.

# arr = np.array([[1,2,3],[4,5,6]])
# arr
# arr+arr
# arr/arr

# # - 브로드캐스팅
# #     - 다른 모양의 배열 간의 산술 연산을 수행할 수 있도록 해주는 numpy의 기능.

# arr
# 10 - arr
# arr*3
# arr/3
# arr2 = np.array([100,200,300])
# arr4 = np.array([[100],[200]])
# arr4

# arr+arr4
# arr3 = np.array([100,200])
# arr+arr3
# arr+arr2
# list_1 = [1,2,3]
# list_1+list_1
# arr_1 = np.array([1,2,3])
# arr_1+arr_1

# # ndim
# # - 배열의 차원의 갯수

# arr.ndim
# arr.shape



# 0차원 (상수)
import numpy as np
a = np.array(10)
print(a)
print(a.ndim)

# 1차원
a = np.array([1,2,3])
print(a)
print(a.ndim)

# 3차원
a = np.array([[[[1,2],[3,4]]]])
print(a)
print(a.ndim)
print(a.shape)

# range 함수를 이용
arr1 = np.array(range(20))
print(arr1)
arr2 = np.arange(20)
print(arr2)

# zeros 
np.zeros(5) ; print(np.zeros(5)) # 0 이 할당 된 것
# ones
np.ones((3,3)) ; print(np.ones((3,3)))
np.full((4),(5)) ; print(np.full((4),(5)))
np.empty((2,3), dtype=np.float32) ; print(np.empty((2,3), dtype=np.float32))
np.arange(-3,3) ; print(np.arange(-3,3))
np.arange(3,50,3) ; print(np.arange(3,50,3))
np.linspace(0,1,6) ; print(np.linspace(0,1,6))

"""배열 결합 함수.  
 - hstack, concatenate(axis=0) 0 = 행을 인식
 - 두 배열을 왼쪽에서 오른쪽으로 붙이기. """
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.hstack([a,b]))
print(np.concatenate([a,b],axis=0))
print(np.stack([a,b]))
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack([a,b]))
# np.concatenate((a,b), axis=1) # 10 vector는 안됨
c = np.array([[0,1,2],[4,5,6]])
d = np.array([[6,7,8],[9,10,11]])
print(np.concatenate((c,d),axis=1))

# 두 배열을 위 아래로 붙이기
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a,b)
print(np.column_stack([a,b]))


import random
import numpy as np
print(random.random()) # 0<= 리턴 값 <=1

data=[1,2,3,4,5,6,7]
print(np.random.choice(data,3))

data= ['apple', 'banana', 'grape', 'orange']
print(random.choice(data))

"""로또 번호 생성기를 만드세요.
 로또 번호를 몇개 생성할까요? > 4
 1. 로또번호 : [13 16 20 22 27 43]
 2. 로또번호 : [21 27 31 36 37 45]
 3. 로또번호 : [ 4 15 16 26 30 39]
 4. 로또번호 : [ 7 15 26 29 40 41]"""

import numpy as np
def make_lotto(count):
    for i in range(count):
        lotto_num = [] #로또 번호가 담길 리스트형 변수
        for j in range(6): #6번 반복
            lotto_num = np.random.choice(range(1,46),6,replace=False)
            # replace=False 중복 추출 막기
            lotto_num.sort() #값 정렬
        print('{}.로또번호:{}'.format(i+1,lotto_num))
count = int(input('로또 번호를 몇개 생성할까요?'))
make_lotto(count)
# replace