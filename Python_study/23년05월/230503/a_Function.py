"""
선형대수학 : 행렬을 분해시킴
선형성, 벡터, 행렬, C구조,
[제로행렬:'주대각선'은 안바뀜]
a11 = 1행 1렬, a12= 1행 2열

"""
# import numpy as np # 버전 확인
# print(np.__version__)

import numpy as np
A = [1,2,3,4,]
a = np.array(A)
s = a[:2]
s = np.asarray(s)
print('A의 출력입니다.%a'%a)
print('S의 출력입니다.%s'%s)

# -Ndarray 타입을 검색하거나 슬라이싱은 참조만 할당하므로
# 변경을 방지하기 위해서는 새로운 ndarray로 만들어 사용 .copy 메소드가 필요

ss = a[:2].copy()
print(ss.size)
ss[0]=99
print(a)
print(s)
print(ss)

arr = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([100,200,300])
arr4 = np.array([[100],[200],[300]])
arr3 = np.array([100,200])
print(arr)
arr + arr[0]
arr / arr
# 브로드 캐스팅 다른 모양의 배열 간의 산술 연산을 수행할 수 있도록 해주는 numpy 기능
arr
10 - arr
arr * 3
arr/3
arr+arr4
arr+arr3
arr+arr2

""" reshape
- 이미 존재하는 배열을 내가 원하는대로 shape 조정을 함
- 내가 입력한 행렬로 만들어줌"""
