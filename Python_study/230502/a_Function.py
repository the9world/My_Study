# 값에 의한 호출 (call by vaule)
# 함수에 인자를 넘길 때 값만 넘김
# 함수내에 인자 값 변경시에 호출자에게 영향을 주지 않음

# 참조에 의한 호출(call by reference)
# 함수에 인자를 넘길 때 메모리 주소를 넘김
# 함수 내에 인자 값 변경이 되면 호출자의 값도 변경됨.

# 객체 참조에 의한 호출
# (call by Object Reference)
# 객체의 주소가 함수로 전달됨.
# 전달된 객체를 참조하여 변경 시
# 호출자에게 영향을 주나, 새로운 객체를 만들 경우
# 호출자에게 영향을 주지 않음.

# a = [1,2,3,4,5]

# def swap_value(x, y):
#     temp= x
#     x=y
#     y=temp
# swap_value(a[1], a[2])
# print(a)

# a = [1,2,3,4,5]
# def swap_offset(offset_x, offset_y,) :
#     temp = a[offset_x]
#     a[offset_x] = a[offset_y]
#     a[offset_y] =temp
# swap_offset(1, 2)
# print(a)

# a = [1,2,3,4,5]
# def swap_reference(list, offset_x, offset_y):
#     temp = list[offset_x]
#     list[offset_x] = list[offset_y]
#     list[offset_y] = temp
# swap_reference(a, 1, 2)
# print(a)


'''함수를 만들어보자.
- 이 함수는 두 개의 숫자를 input으로 받으면 작은 수로  
큰수를 나눈 몫과 나머지를 반환하는 함수이다
- 반환 값은 튜플로 되어 있으며 몫, 나머지 순으로 되어있다.
단, 0으로 나누는 것은 불가하기 때문에 두 수 중에 작은 수가 0이라면
화면에 '0은 사용할 수 없습니다.' 를 출력하고 종료되어야 한다.'''

# def div3(a,b): # 강사님 풀이
# 	if a<b:
# 		big=b
# 		small=a
# 	elif b<=a:
# 		big=a
# 		small=b
# 	else:
# 		print("정수가 아닙니다.")
# 	if small==0:
# 		print('0은 사용할 수 없습니다.')
# 	elif abs(big)< 0 or abs(small)<0:
# 		print('정수를 입력하세요.')
# 	else:
# 		q = big // small
# 		r = big % small
# 		return(q,r)
# print(div3(1,0))

'''어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력하는 함수를 짜보자.
끊는 단위는 따로 정하지 않으면 2로 설정해보자.
hint : input을 string과 unit2=2 로 받고
while을 사용하고, 길이는 len 함수를 사용'''
# def func(string, unit=2):
#     i = 0
#     while i < len(string):
#         print(string[i:i+unit])
#         i += unit
# print(func("테스트를 위한 문장입니다"))

'''add_all 함수를 짜봅시다
add_all(1,2,3,4,5,6,7,8,9,10)
55
hint : *args를 input으로 받으세요.'''

# def add_all(*input): # 풀이 1
# 	s=0
# 	for i in range(len(input)):
# 		s+=input[i]
# 	return s
# print(add_all(1,2,3,4,5,6,7,8,9,10))

# def add_all3(*args): # *agrs 튜플이라 불가 킹치만 입력을 리스트로 하면 됨
#     s = 0
#     for i in args :
#         for j in i :
#             s += j
#         return s
# print(add_all3(1,2,3,4,5,6,7,8,9,10))

# def add_all4(*args):  # args 튜플을 리스트로 받는 법
#     temp = 0
#     for i in range(len(args)) :
#         if type(args[i]) == list:
#             for j in args[i] :
#                 temp += j
#         else :
#             temp += args[i]
#     return temp
# print(add_all4(1,2,3,4,5,6,7,8,9,10))

''' 팩토리얼(Factorial)을 구하시오. ( ex) 5! = 120)
1 부터 시작하여 어떤 범위에 있는 모든 정수를 곱하는 것.'''

# def fact(n): # 재귀적으로 하지 않은 것           ★안댄안댄다내다낻나ㅐㄷ
# 	f=1 # 곱을 계산할 변수의 초기값
# 	for i in range(1, n+1): # 1 부터 n 까지 반복
#         f = f*i # 곱셈연산
# 	return f

# def fact1(n): # 재귀적으로 하는 것
# 	if n<=1:  # n이 1이하이면 종료 조건
# 		return 1
# 	return n * fact1(n-1)
# print(fact1(5))

'''pop quiz! 문제를 먼저 풀어보자. 여기는 동네 유명한 빵집이다.
사람들에게 먼저 온 순서대로 번호표를 나누어주려고 한다.
번호표를 나누어주는 함수를 작성해보자.
- 함수는 사람이름으로 되어 있는 리스트를 받아서
"대기번호 x번: 사람이름"을 화면에 출력하고 (번호표, 사람이름)을
원소로 이루어진 리스트를 반환한다.
input : list
output : list
'''
# people = ['펭수','뽀로로','뚝딱이','텔레토비']

# def func1(line):
#     new_lines = []
#     i=1 #대기번호를 트래킹하는 변수 i
#     for x in line:
#         print('대기번호 %d번 : %s' %(i,x))
#         new_lines.append((i,x))
#         i +=1 #별도로 업데이트를 해줘야 함.
#     return new_lines
# func1(people)

# def func1(line): # enumerate
#     new_lines = []
#     for idx,val in enumerate(line):
#         print('대기번호 %d번 : %s' %(idx,val))
#         new_lines.append((idx+1,val))
#     return new_lines
# func1(people)

# enumerate (열거하다)
# 반복 가능한 객체의 인덱스와 원소에 함께 접근할 수 있는 함수.
# lst = ['a', 'b', 'c']
# for x in enumerate(lst):
#     print(x)

# lst1 = 'abcd'
# for x in enumerate(lst1):
#     print(x)

# zip()
# 반복 가능한 객체들을(2개 이상) 병렬적으로 묶어주는 함수.
# 각 원소들을 튜플의 형식으로 묶어줌.
# str_list = ['one','two','three','four']
# num_list = [1,2,3,4]

# for i in zip(num_list,str_list):
#     print(i)

# lambda/ 한 줄을 실행한 결과 값이 바로 반환값이 됨.
# lambda는 식 형태로 되어 있어서 lambda expression(람다 표현식)라고도 불림
# 람다는 익명 함수로서 함수를 간편하게 작성할 수 있게 해줌
# python3에서 사용이 권장되지는 않지만 머신러닝이나 데이터 분석시 많이 사용됨
#  1, 2번 같은 함수식
# def plus_two(num):
#     return num + 2
# a = 2
# b = plus_two(a)
# print(b) # 4

# lambda x : x +2
# func2 = lambda x : x + 2
# c = func2(2)
# print(c) # 4

# map()
# 리스트, 튜플 스트링 등 자료형 각각의 원소에 동일한 함수를 적용
# items = [1,2,3,4,5]
# squared = []
# for i in items :
#     squared.append(i*i)
# print(squared) 

# squared_map = list(map(lambda x : x**2, items))
# print(squared_map) # [1,4,9,16,25]

'''lambda와 map을 이용하여 items의 요소들을 string(문자)으로
바꾸는 것을 짜봅시다.'''
# items = [1, 24, 3, 6, 7]
# str_items = list(map(lambda x : str(x),items))
# print(str_items) # ['1', '24', '3', '6', '7']

# list comprehension
# 0 ~ 9까지를 순서대로 가지고 있는 리스트를 만드세요
# list_1 = [0,1,2,3,4,5,6,7,8,9]

# list_2 = []
# for x in range(10):
# 	list_2.append(x)
# print(list_2) # [0,1,2,3,4,5,6,7,8,9]

# lc_1 = [x for x in range(10)]
# print(lc_1) # [0,1,2,3,4,5,6,7,8,9]

'''for 문
quiz 1) 구구단 2단을 list comprehension을 이용하여 구현하고
리스트를 화면에 출력해보자

quiz 2) 다음의 문장을 분석해보자.
"코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다.
마스크를 끼고 손씻기를 생활화합시다" 라는 문장을
띄어쓰기별로 분석하려고 한다. 띄어쓰기별로 문장을 나눈 후
각 요소의 길이를 리스트에 저장하라.
(hint: 띄어쓰니느 split 함수 사용)'''

# a = 2
# for i in range(2,10):
#     print(a,"x",i,"=", a*i)
#     i+=i

# # 1) 구구단 2단
# tables = [2*x for x in range(1,10)]
# print(tables)

# # 2) 코로나 바이러스
# sentence = """코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다.  
# 마스크를 끼고 손씻기를 생활화합시다."""
# len_sent = [len(s) for s in sentence.split()]
# print(len_sent) 

# 10부터 20까지의 숫자들중에서 짝수만을 담은 리스트를 만들어보자
# list3=[]
# for x in range(10,21):
#     if x%2==0:
#         list3.append(x)
# print(list3) # [10, 12, 14, 16, 18, 20]

# lc_2 = [x for x in range(10,21) if x%2 ==0]
# print(lc_2) # [10, 12, 14, 16, 18, 20]

# for 문 + if 문
# quiz 1) 1부터 10의 제곱수 중, 50 이하인 수만 리스트에 저장하라.
# quiz 2) 다음의 문장을 분석해보자.
"""코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다.
외출 시에는 마스크를 끼고, 손씻기를 생활화합시다."""
# 라는 문장을 띄어쓰기별로 분석하려고 한다.
# 띄어쓰기별로 문장을 나눈 후 각 요소의 길이가 5미만인 것들만 리스트에 저장

# lc_3 = [x**2 for x in range(1,11) if x**2<50]
# print(lc_3) # [1, 4, 9, 16, 25, 36, 49]

# sentence = """코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다.
# 외출 시에는 마스크를 끼고, 손씻기를 생활화 합시다."""
# lc_4 = [s for s in sentence.split() if len(s) <5]
# print(lc_4)

"""for + if + else
1 부터 10까지의 숫자들 중 홀수이면 어떤 제곱수를
짝수이면 세제곱수를 담은 리스트를 만들어보자"""

# list_4 =[]
# for x in range(1,11):
#     if x%2==1:
#         list_4.append(x**2)
#     else :
#         list_4.append(x**3)
# print(list_4) # [1, 8, 9, 64, 25, 216, 49, 512, 81, 1000]

# print([x**2 if x%2==1 else x**3 for x in range(1,11)])
# [1, 8, 9, 64, 25, 216, 49, 512, 81, 1000]

# for 문 + for 문
# word1 = 'Hello'
# word2 = 'World'
# result = [i+j for i in word1 for j in word2]
# print(result)
""" ['HW', 'Ho', 'Hr', 'Hl', 'Hd', 'eW', 'eo', 'er', 'el', 'ed',
 'lW', 'lo', 'lr', 'll', 'ld', 'lW', 'lo', 'lr', 'll', 'ld',
 'oW', 'oo', 'or', 'ol', 'od'] """ # 출력

""" for 문 + if 문
quiz 1) 40 이하의 숫자는 5를 더하고,
40 초과의 숫자는 41로 바꾸어 리스트로 저장하고, 리스트를 출력하라.

quiz 2) 커트라인이 60점일 때, 사람이름과 통과여부를 리스트로 담아서 출력하라.
이름과 통과여부는 튜플로 묶여있는 자료이다. """
# list_5 = [12,67,32,48,19,57,29,49] # 1번
# lc_6 = [x+5 if x<=40 else 41 for x in list_5]
# lc_6

# students = {"보라돌이":61, "뚜비":35, "나나":78,"뽀":88} # 2번

# result = [(name,True) if score>60 else (name, False)for name,score in students.items()]
# print(result)

# 조건이 2개 이상이면 for 가 뒤로 간다
# 조건이 1개 이면 for 뒤에 조건을 쓴다.

# 선형대수학(linear Algebra)
# 선형성(linearity)
# 벡터(vector)
# 스칼라(Scalar) : 크기만 있고 방향이 없는 물리량, 즉 방향성을 가지지 않는 성분.
# 벡터 : 크기와 방향이 있는 물리량, 즉 크기에 방향성을 함께 고려하여야 설명이 가능한
# 물리량이다. 물리량 중 변위, 속도, 가속도, 힘, 운동량, 충격량, 전,자기장 등은 벡터량이다
# # An ordered list of numbers
# dx1 행/ 열   (트랜스포지 1xd)
# 벡터의 기본연산
# 두 벡터를 차례로 따라 이동한 벡터의 끝지점만 가리키는 벡터가 있다면
# 그 벡터가 벡터의 합
# 수치적으로 벡터의 합을 연산하라면, 각 차원(자리)의 값들을 더해주면 그 것이 결과 벡터

# 행렬
# -수 또는 변수 등의 일련의 개체들을 행(row)과 열(Column)에 맞추어 직사각형 모형으로
# 순서 있게 배열하여 괄호[]로 묶은 것.
# -괄호 안의 개체와 같이 행렬을 구성하는 요소 보통 문자 aij,bij, cij 등으로 나타냄
# (i행 j열의 원소)
# 행(Row) 행렬의 가로줄
# 열(Column) 행렬의 세로줄

# 행렬의 상등
# 두 행렬 A 와 B의 행의 개수와 열의 개수가 같을 때, 이 두 행렬은"같은꼴"

# 행렬의 곱셈
# 두 행렬 (m x k) 행렬 A와 (k x n) 행렬 B에 대하여 A행렬의 열의 수와 B행렬의 행의 수가 같을 때,
# A x B 와 B X A 는 교환법칙이 성립되지 않아 답이 다르다
# [12] 2x2    [56] 2x2
# [34]        [78]
# 1[1x5+2x7] 19 A
# 2[1x6+2x8] 22 B
# 3[3x5+4x7] 43 A
# 4[3x6+4x8] 66 B
# A
# 1x5+2x7
# 3x5+4x7 
# B
# 1x6+2x8
# 3x6+4x8