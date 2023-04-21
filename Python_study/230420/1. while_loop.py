# while 반복문
"""
while 조건:
    반복할 코드
"""
# 조건이 True(참)인 경우에 코드를 계속 반복
# print(1) ~~ print(10) # 밑과 값은 동일하나 방법이 다름
# n = 1
# while n <= 10 : # 100으로 바꾸면 100까지 출력 
#     print(n)
    # n += 1    # n = n+1 # n 에다가 1을 더 한 연산자 
#     반복문 : 최초 값 1 출력후 다시 올라가서 +1이 되고 반복문 False이 될때까지 1씩 증가

# while 반복문을 활용하여 10부터 1까지 순서대로 출력하세요
# cnt = 10
# while cnt >= 0 : # while cnt >= 1 과 같음
#     print(cnt)
#     cnt -= 1 # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 위와 동일하게


# += 연산자
# 대입 연산자의 일종
# 더하기 연산 후 할당
# n += 1은 n = n+1이라는 의미
# 산술 연산자 모두 적용 가능 (-=, *=, /=, **=, //=, %=)

# s1 = "안녕"
# s1 += "하세요" # 대입 연산자는 이런 식으로 따로 사용도 가능하다.

# money = 10000
# price = 1000
# coffee = 5
# while money >= price : # 동일 : while money - pirce >= 0 :
#     print("커피를 구매했습니다.")
#     money -= price
#     coffee -= 1
#     print("남은커피:", coffee) # 커피 갯수 세는 것
#     if coffee == 0 :
#         break # if(특정조건)문과 함께 사용 @탭 넣음@
# break (반복문 안에서 사용)
# 반복문을 즉시 종료 (True 일 경우 반복이지만 빠져나감) 

# while 반복문을 활용하여
# 1부터 10까지 홀수만 출력한다
# a = 1
# while a <= 10 :
#     if a % 2 == 1:
#         print(a)
#     a += 1 # if 안으로 가면 안됨

# continue
# 반복문의 제일 처음으로 돌아감
# b = 1 # b=0
# while b < 10:
# # while b < 9 :
#     # b+= 1
#     if b % 2 == 0 : #continue # True면 다시 처음으로 돌아가서 출력이 안됨
#         b+=1
#         continue
#     print(b) # 1,3,5,7,9 (짝수)
#     b += 1
# while True (무한 반복문, 무한 루프)
# 조건식에 True를 입력해 항상 참이 되도록 하여 무한히 반복하게 한다
# while True : # 계산 할 필요가 없이 True 이므로 무한 반복
#     print("hi")
# while True :
#     user_input = input ("종료하려면 1을 입력해주세요.")
#     if user_input == "1" :
#         break # 1이 입력 될 경우 반복문을 나감

# 무한반복문으로 계산기 만들기
# +, -, *, / 계산
# 2개의 수를 계산 a+b
# while True : # """ 쓰면 여러줄 짜리 문자열
#     print("""
#     계산기
#     ======
#     1. 더하기(+)
#     2. 빼기(-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     5. 끝내기 
#     """) # 5. 끝내기는 임의 추가임 지우면 베이직
#     operator = input ("계산을 선택하세요 :") #operator 변수
#     if operator == "1" : #계산기에서 1(+)을 선택 할 경우 #""없으면 False 데이터 타입(문자or숫자)까지 같아야함
#         print("1+2=", 1+2)
#     if operator == "2" :
#         print("1-2=", 1-2)
#     if operator == "3" :
#         print("1*2=", 1*2)
#     if operator == "4" :
#         print("1/2=", 1/2)
#     if operator == "5" : # 끝내기는 버튼 응용 #  무한반복 나가는 버튼은 ctrl + C
#         break

# 코드를 수정하여 사용자가 입력한 숫자를 이용해 계산하도록 변경
# while True : # """ 쓰면 여러줄 짜리 문자열
#     print("""
#     계산기
#     ======
#     1. 더하기(+)
#     2. 빼기(-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     q. 끝내기 
#     """) # q. 끝내기는 임의 추가임 지우면 베이직
#     operator = input ("계산을 선택하세요 :") #operator 변수
#     if operator == "q" : # 끝내기는 버튼 응용 #  무한반복 나가는 버튼은 ctrl + C
#         #int(input) 보다 아래 있으면 숫자 입력 창이 또 뜸
#         break
#     a = int(input("숫자를 입력하세요"))
#     b = int(input("숫자를 입력하세요"))
#     if operator == "1" : #계산기에서 1(+)을 선택 할 경우 #""없으면 False 데이터 타입(문자or숫자)까지 같아야함
#         print(a, "+", b, "=", a+b)
#     elif operator == "2" : # elif : if에선 False elif에서 True일 경우 실행
#         print(a, "-", b, "=", a-b)
#     elif operator == "3" :
#         print(a, "*", b, "=", a*b)
#     elif operator == "4" :
#         print(a, "/", b, "=", a/b)

# 사용자가 가지고 있는 돈을 입력받는다.
# 구매할 수 있는 커피의 개수와 잔돈을 출력한다.
# 구매할 수 있는 음료수의 개수와 잔돈을 출력한다
# 구매할 수 있는 콜라의 개수와 잔돈을 출력한다.
# 커피는 500원 음료수는 700원 콜라는 930원
# 물품의 개수는 무한하다고 가정한다.
# while 반복문을 사용하여 작성한다.
# 반복문과 리스트를 사용
# idx = 0
# prices = [500, 700, 930]
# money = int(input("금액:"))
# while idx < len(prices) : # <- idx <=, idx < 3 :도 가능
#     price = prices[idx] # = 할당 []인덱싱
#     print("커피:",money//price)
#     print(money%price)
#     idx+=1

# # while 반복문을 사용해서 scores 리스트에 시험 점수 5개를 정수형으로 입력 받으세요.
# 영어 = int(input("영어점수:"))
# 수학 = int(input("수학점수:"))
# 국어 = int(input("국어점수:"))
# 사회 = int(input("사회점수:"))
# 체육 = int(input("체육점수:"))
# scores = [영어, 수학, 국어, 사회, 체육]

# while scores :
#     print("영어:",영어, "수학:", 수학, "국어:", 국어, "사회:", 사회, "체육:", 체육)
#     break               # 혼자 한거 비효율 노가다 ★★★★★★다시해봅시다★★★★★★

# scores = [] # 강사님이 알려주신 방법
# n = 0
# while n < 5 :
#     score = int(input("시험 점수:"))
#     scores.append(score)
#     n += 1
# print(scores) # 탭 위치(블럭,소속) 중요, while 안에 있으면 매번 나옴!! 들여쓰기 잘해야댄다

# while 반복문을 사용하여 구구단 2단을 출력하세요.

# n = 1
# while n < 10 :
#     print("2*", n, "=", 2*n)
#     n += 1            ########## 다시해봅시다
