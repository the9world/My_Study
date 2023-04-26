# 예외 처리 (오류 처리)
# 오류 발생을 잡아내서 처리하는 것
# li = [1,2,3,4,5]
# li[100]
# 100 / 0 
# f = open("없는 파일", "r")
# 에러 발생 시 프로그램 중단
# 에러 메시지를 출력한다.

# 예외 처리 구문
# try ~ except
# try 블록에는 오류가 발생할 수 있는 코드
# except 블록에는 오류가 발생했을 때 수행할 코드
# 오류가 발생하지 않으면 except 블록의 코드는 실행되지 않는다.
# try:
#     100 / 0
#     print("에러가 없습니다")
# except:
#     print("에러 발생")
# print("에러 발생 후")

# try:
#     100 / 0
# except Exception as e: # Exception 에러 메세지 출력
#     print(e)
# print("에러 발생 후")

# try:
#     100 / 0 #  # ZeroDivisionError 나누기 0 오류
#     # [1,2,3,4,5][100] # IndexError인덱스 초과 오류
# except ZeroDivisionError as e: # ZeroDivisionError 나누기 0 만 잡음
#     print(e, "0으로 나눌 수 없습니다.")
# except IndexError as e :
#     print(e, "인덱싱할 수 없습니다.")
# print("에러 발생 후")

# finally
# 예외 발생 여부와 상관 없이 항상 수행되는 코드
# try :
#     f = open("없는 파일", "r")
# except :
#     print("에러 발생")
# finally:
#     f.close()

# else
# 오류가 발생하지 않으면 실행
# try :
#     age= int(input("나이:"))
# except :
#     print(" 숫자를 입력하지 않았으므로 당신의 목숨은 ㅇ벗습니다")
# else: #if 의 else와 주의해서 구분
#     if age >= 20:
#         print("틀딱입니다.")
#     else:
#         print("잼민이 땅땅")

# class Bird: # ------------다시봅시다--------
#     def fly(self):
#         raise NotImplementedError # 구현 되지 않은 에러
# my_bird = Bird
# my_bird.fly()