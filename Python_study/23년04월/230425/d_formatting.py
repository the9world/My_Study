# 문자열 포맷팅(formatting)
# 포맷 코드
# %s 문자열 (string)
# %d 정수 (int)
# %f 실수 (float)
# %o 8진수
# %x 16진수
# \%% % 글자 자체 (백슬래쉬는 아님)  

# result = "%d + %d = %d " % (3, 2, 5)
# print(result)
a, b = 1, 2
result= "%d + %d = %d" %(a, b, a+b)
print(result)
result1 = "이름 : {} ".format('황덕우') # 직접 대입
age=100 ; result2 = "\nage: {}".format(age) # 변수 대입
result3 = "\n출신지 : {ad} \n성별 : {gen}".format(ad="한국", gen="트랜스")
result= result1+result2+result3
print(result)

# string1 = "Hello"
# int1 = 3
# float1 = 1.2345
# print("%s %d %f"%(string1, int1, float1)) # Hello 3 1.2345

# f - string
# Python 3.6 이후 버전부터 지원
# 변수 자체를 문자열로 바꿔 주는 것
string1 = "Hello"
int1 = 3
float1 = 1.2345
result= f"string {string1} {int1} {float1}"
print(result) # Hello 3 1.2345
result= f"{string1,int1,float1}" # ('Hello', 3, 1.2345)
print(result)


# # 포맷팅 변환 해보셈
# def add(a,b):
#     result = "%d + %d = %d" % (a,b, a+b)
#     print(result)
#     with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
#         f.write(result)
# def sub(a,b):
#     result = "%d - %d = %d" % (a,b, a-b)
#     print(result)
#     with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
#         f.write(result)
# def mul(a,b):
#     result = "%d * %d = %d" % (a,b, a*b)
#     print(result)
#     with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
#         f.write(result)
# def div(a,b):
#     result = "%d / %d = %d" % (a,b, a/b)
#     print(result)
#     with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
#         f.write(result)
# while True :
#     print("""
#          계산기
#          1: +
#          2: -
#          3: *
#          4: /
#          q: 종료
#         """)
#     operator = input("원하는 계산을 입력하세요:")
#     if operator == 'q':
#         break
#     a = int(input("정수 1: "))
#     b = int(input("정수 2: "))
#     if operator == "1" :
#         add(a,b)   
#     elif operator == "2" :
#         sub(a,b)
#     elif operator == "3" :
#         mul(a,b)
#     elif operator == "4" :
#         div(a,b)
#     break

