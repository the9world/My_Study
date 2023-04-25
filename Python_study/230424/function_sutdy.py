# function 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서 특정 작업(처리)을 수행하고
# output(출력)을 반환한다.

# 내장 함수 (built-in)
# Python이 기본적으로 제공하는 함수
# 절댓값을 구하거나 원소의 개수를 세는 것과 같은 함수가 내장 함수에 해당
# print(), len(), zip(), int(), float(), str(), list(), range()

# abs()  absolute의 약자
# 입력한 숫자형 데이터의 절댓값을 반환한다.
# 절댓값 = 부호를 제외한 숫자 그대로
# print (abs(100)); print (abs(-100)) # 둘 다 100
# print (abs(3.15)); print (abs(-3.15)) # 둘 다 3.15

# sun(리스트)
# 리스트 안의 숫자를 모두 더한 값을 반환한다.
# print (sum([1,2,3,4,5])) # 15  // sum(리스트명)

# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환한다. 가장 큰 수
# print (max([1,2,3,4,5])) # 5

# min(리스트)
# 리스트에서 최솟값을 찾아 반환한다.
# print (min([1,2,3,4,5])) # 1

# chr() 정수 1개를 입력 받고, 해당하는 유니코드 문자를 반환한다.  
# print(chr(65)) # A
# ord() 문자 1개를 입력 받고, 해당하는 정수를 반환한다.
# print(ord("A")) # 65

# round(값) 반올림 함수 # round(1,) 비우면 0
# ronud(값, 소수 자릿수), 오사오입 원칙 : 홀수에선 올리고 짝수에선 버림
# print (round(1.234)) # 1
# print (round(1.234, 2)) # 1.23
# print (round(1.369, 1)) # 1.4

# 함수 정의 (define) 함수 만드는 것
# 함수 이름 , 함수 입력 값(parameter), 함수 결괏 값(return value)
"""
def 함수 이름 (함수 입력 값) :
    함수 기능코드
    return 함수 결괏값
""" # while, for, if
# def 함수를 정의하는 명령어
# 함수 이름도 변수 이름처럼 규칙을 지켜야 한다.
# 영어, 숫자, _만 사용, (첫 글자가 숫자면 X, 띄어쓰기 X, 키워드 X)
# 기존에 이미 정의 된 함수 이름도 피하는 것이 좋음
# def print_names(): # "print_names"= 함수 이름, "()" = 입력 값
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인") # 여기까지는 output이 없는 상태
# # print_names() # 호출(출력)

# def get_name() :
#     return "내 이름" # reurn 된 값을 변수에 담는다?

# def print_my_name() :
#     print(get_name())
# print_my_name()

# a = print_names() # 리턴이 없음
# b = get_name() # 리턴이 있음
# print(a)
# print(b)
# return 호출한 곳으로 돌려주는 값, 차이는 return이 없으면 나오는 값이 없다 
# 출력만 하고 종료 return이 있으면 반환하는 값이 있다.

# def add (a, b) : #(a, b) # a, b= parameter, 매개변수. 함수 입력 값, argument
#     return a + b # print 함수가 없음 # 
# def print_add(a, b) :
#     print(a + b) ★★★★★★★★★★★★★★★★★★★★

# result = add (1,2) # 호출(이름 부르면)하면 add로 감
# print(result)

# a= print_add(1,2) # 1+2 하고 반환
# print (a) # 3

# print_add (1,2) # return이 없어서 함수를 호출 하고 끝
# result = print_add(1,2) # print(a+b) 함수가 회출되어 일단 3이 출력되고 result는 return이 없어서 None
# print(result) # None, 리턴 값이 없어서 종료 
# print_add("안녕", 1) # error : str+ int 
# print_add(1,2) # 3
# print_add("안녕", "하세요") # 안녕하세요
# print_add("하세요", "안녕") # 순서대로 입력되므로 확인
# print_add(b='하세요', a='안녕') # 지정해서 사용 가능

# def swap_number(a, b):
#     temp = a
#     a = b
#     b = temp
#     print(a , b)
#     return a, b # 이게 없으면 1, 2
# a = 1
# b = 2 
# print("함수 호출 전", a, b) # 1, 2
# a, b = swap_number(a,b) # 함수 안에서 2, 1
# print("함수 호출 후", a, b) # 1, 2,  # def 안에 return이 있으면 2, 1

# 함수 밖에서 쓰는 a, b와,  함수 안에서 쓰는 a, b는 이름만 같고 서로 다른 변수
# 함수 밖에서 쓰는 변수 전역 변수(Global Variable)
# 함수 안에서 쓰는 변수 지역 변수(Local Variable)

# 다음 함수를 정의하세요.
# 함수 이름 : ml
# 함수 입력 값 : 정수 2개
# 함수 출력 값 : 정수 2개의 곱
# def mul(a, b) :
#     return a * b # 수식은 return 뒤에만 넣을 수 있다?
# print(mul(3,6))
# result = mul (3,6)  # 위와 같음
# print (result)

# a=1 ; b=2 ; c=3
# a, b, c = 1, 2, 3
# d, e, f = [4, 5 ,6]
# g, h, i = (7, 8, 9)

# def mul(n1, n2 = 1):
# # n2 = 1 : 기본 값 매개변수, default value parameter
# # 함수 호출 시 n2에 입력 된 값이 없으면 기본 값 사용  
#     return n1 * n2
# mul(1,2) #2
# mul(1) #1 n2에 입력 된 값이 없으므로 기본 값(n2=1)이 호출 됨

# def test_func(x, test=[]):
# # [](리스트)를 사용하면 안에 값들이 누적됨 됨,  [] 기본 값 사용 금지
#     test.append(x)
#     print(x, test)
# test_func(1) # 1 [1]
# test_func(2) # 2 [1,2]

# def test_func1(x, test=5):
#     test=test
#     print(x, test)
# test_func1(1) # 1 5
# test_func1(2) # 2 5

# def test_func2(x, test=None):
#     if test == None:
#         test = []
#     test.append(x)
    # print(x, test)

# def sub (n1, n3, n2=0):
# n1, n2=0, n3 -> n1, n3, n2=0
# 위와 같이 기본 값이 있는 매개 변수는 기본 값이 없는 매개변수보다 뒤에 위치해야 함
    # print(n1 - n2 - n3)

# def add(): # add: 숫자 2개를 더 하는 함수
# 1 ~ 10까지 더 한다.
# https://legitcode267.tistory.com/13
# * 를 사용한 매개변수
# ex: *args 입력 값이 몇개가 될지 모를 때나 안 정했을 때 사용한다.
# 일반 매개변수와 같이 사용 가능하다.
# def add_many(*args) : # argument 줄임말
# # 튜플(tuple)처럼 사용
# # 인덱싱, 슬라이싱, for문 사용 가능
#     result =  0
#     for i in args :
#         result +=i #args 값 들을 하나 씩 꺼내어 result에 더 함
    # return result

# add_many(1,2) -->3
# add_many(1,2,3,4,5) --> 15
# add_many(1,2,3,4,5,6,7,8,9,10) -> 55

# result1 = add_many(1,2,3,4,5) 
# print(result1) # 15
# result2 = add_many(3,2,5,9,1)
# print(result2) # 20
# result3 = add_many(1,2)
# print(result3) # 3

# def calc_many(n1, *arge) :
#     result=    n1
#     for i in arge :
#         result +=i
#     return n1

# 키워드 매개 변수, **kwargs (keyword arguments)
# 딕셔너리로 사용
# def print_kwargs(**kwargs): # 들어오는 값들이 유동적일 때 주로 사용
#     print (kwargs)

# print_kwargs(a=1,b=2)
# print_kwargs(name="이름", age="10")

# 함수의 반환, return 반환 값
# return을 만나면 반환 값을 반환 하는 동시에 함수가 종료된다.
# def test_func5():
#   print(1)
#   print(2)
#   return None # 리턴을 만나는 동시에 반환 후 끝나서 밑은 수행 하지 않음
#   print(3)
#   print(4)
#   print(5)

# 함수의 반환 값은 무조건 1개 이다.
# def test_func6(a,b):
#     return a + b, a * b  # return (a+b, a*b) 과 같음
# # print(test_func6(1,2)) # 반환 값이 1개여야 해서
# result=test_func6(1,2)
# res_add, res_mul = test_func6(1,2)  # res_add, res_mul = (a+b, a*b)과 같음
# print(result) #(3,2)
# print(res_add, res_mul) # 3 2

# 홀수 판별 함수
# 정수 1개 입력 받고 홀수인지 판별하는 함수
"""
함수 이름 : is_odd_number
파라미터 : n
반환 값 : 홀수면 True, 짝수면 False
"""
# def is_odd_number(n=int(input("홀짝 :"))): ## 내가 한거
#     if  n%2==1: 
#         print("홀수")
#     elif n%2==0: 
#         print("짝수")
# is_odd_number() 

# def is_odd_number(n): # 강사님 풀이 1번
#     if n%2 ==1:
#         return True
#     else:
#         return False
# is_odd_number(5) # 홀수라 return True

# def is_odd_number(n): # 강사님 풀이 2번
#     if n%2 ==1:
#         return True
#     return False # 짝수는 트루가 아니니까 바로 여기로옴
# is_odd_number(4) # 짝수라 바로 return  False

# def is_odd_number(n): # 강사님 3풀이 3번
#         return n% 2 == 0
# print(is_odd_number(4)) # 짝수라 바로 False

# 테두리를 출력하는 함수
# 문자열을 입력 받고 print함수를 이용해 테두리와 함께 문자를 출력한다
"""
함수 이름 : get_bordered_str
파라미터 : message
반환 값 : None : 조건이 없으면 return 불 필요 : 호출 받은 곳으로 보낼 값은 없는 것.
"""
#print 예시
"""
*****
hello
*****
"""
# def get_bordered_str(message): # 내가 한 것
#     print("*"*len(message))
#     print(message)
#    print("*"*len(message))
# get_bordered_str("안녕하세요")

# def get_bordered_str(message): # 풀이
#     # message = str(message) # 이걸 넣어도 가능
#     n=len(str(message)) #연결형 데이터 :인덱싱, 슬라이싱 가능한 데이터
#     print("*"*n) 
#     print(message)
#     print("*"*n)
# get_bordered_str("반갑다")
# get_bordered_str(13579)

# 속도를 변환하는 함수
# m/s  단위의 속도가 입력 되면
# km/h 단위의 속도로 변환 한다.
"""
함수 이름 : convert_velocity
파라미터  : velocity
반환 값   : km/h로 변환 된 속도
"""
# def convert_velocity(velocity): # 풀이
#     # 1초 1m = 1m/s로 1시간을 가면 1m/s * 3600 = 3600m/h / 1000 = 3.6km/h
#     # 1m/s * 3600 / 1000 ==> 3.6km/h
#     result=velocity * 3.6 #초속 * 시속 
#     return print(result)
# convert_velocity(10) # return과 print 헷갈리지 말 것
# velocity = convert_velocity ; print(velocity) # 위와 같은 print 하는 법

# 별 찍기 함수
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다.
"""
함수 이름 : print_stars
파라미터 : n
반환 값 : None

출력 결과 n->1 = *, ~~ n -> 4 = ****
*
**
***
****
"""
# def print_stars(n): # 실습
    # for i in range(1, n+1) :
    # for i in range(0, n+1) :
    # for i in range(n) :
        # print("*"*i)
        # print("*"*i)   
        # print("*"(i+1)) ★★ 이거 다시
# print_stars(4)

# i = 0  # 풀이 2번
# while i < n:
#     j = 0
#     while j < i+1:
#         print("*", end="")
#         j+=1
#     print()
#     i+=1

# def print_stars(n): # 풀이 3번 # range n이라 하면 0부터 n 까지 (range 기본 값은 최대?)
#     for i in range(n) : # 0 ~ n-1
#         for j in range(i+1): # 0 ~ i   range 때문에 -1
#             print("*", end="") # end 줄 바꿈
#         print()
# print_stars(4) # 호출