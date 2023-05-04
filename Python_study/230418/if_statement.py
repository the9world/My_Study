#조건문(IF): 문법이 정해져 있다.
#Python 표준: 탭(1회) OR 스페이스(4회)
"""
if 조건:
    실행하려는 코드
    코드2줄
    코드3줄
코드4줄
if문은 조건이 True(참)일 때만 안쪽 코드 블럭을 실행

if 조건: 
    조건이 참일 때 실행하려는 코드
else:
    아닐 때 실행하려는 코드
else는 조건이 False(거짓)일 때 안쪽 코드 블럭을 실행

if 조건1:
    조건1이 True(참)일 때 실행
elif 조건2:
    조건1은 False, 조건2는 True일때 실행
else:
    조건 1 False 조건2 False일때 실행
"""
# 전공책 if항목 책 참조
# bool type
# # True(참), False(거짓)

# number1 = 5 #숫자형변수 / 정수
# number2 = 6

# #비교 연산자 ><, == 등 (조건식)
# if number1 > number2: #False는 출력 되지 않고 else로 내림
#     print(number1 > number2)
#     print("number1이 더 크다.")
# elif number1 == number2: #elif 같을 경우
#     print(number1==number2)
#     print("같다")
# else:
#     print(number1 > number2)
#     print("number2가 더 크다")
# 비교 연산자 (a, b는 변수) 
#     a>b    (a가 b보다 크다)
#     a>=b   (a가 b보다 크거나 같다) =이 앞에 오면 안됨.
#     a<b    (a가 b보다 작다)
#     a<=b   (a가 b보다 작거나 같다 )
#     a==b   (a와 b가 같다
#     a!=b   (a와 b가 같지 않다)

# print (2>3)  #False
# print (2>=3) #False
# print (2<3)  #True
# print (2<=3) #True
# print (2==3) #False
# print (2!=3) #True

# print ("a"<"b")         #True
# print ("CAT"<"DOG")     #True
# print ("COW" > "CAT")   #True
# print ("DOG" == "dog")  #False
# print ("DOG" > "dog")   #False

# 논리 연산자 [bool type 변수에 사용 (True, False)]
    # and   A and B (A, B 모두 True 일때만 True 아니면 False) 
    # or    A or B  (A, B 중 하나라도 True면 True, 둘 다 False면 False)
    # not   not A   (True ↔ False, False ↔ True 바꾼다.)

# print(True and True)    #True
# print(True and False)   #False
# print(False and True)   #False
# print(False and False)  #False

# print (True or True)    #True
# print (True or False)   #True
# print (False or True)   #True
# print (False or False)  #False

# print (not True)    #False
# print (not False)   #True
# 응용
# age = 17
# money = 10000
# if age >= 20 and money >= 10000:
#     print("성인이고 부자입니다")
# if age >= 20 or money >= 10000:
#     print("성인 또는 부자입니다")

# a = "하이"
# b = "빠이" 
# if a in "빠이":
    # print(a)
    # 문자열에 값이 있으면 True 없으면 False 

# if 0:
    # print(0)
    # 숫자 0은 False, 나머지는 True

