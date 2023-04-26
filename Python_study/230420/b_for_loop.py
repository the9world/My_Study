# # for 문
# """
# for 변수 in iterable(순회 가능한) 값:
#     반복할 코드 (무한 반복X 1회? 순회)
# """
# li_1=["one", "two", "three"]
# for i in li_1: # i 안에(in) li_1를 대입(할당)해서 순회 iterable?
#     print(i) # 세로로 하나씩 one, two, three가 나옴 
# # 첫 번째 요소부터 마지막 요소까지 변수에 대입(할당?)하면서 반복
# s1 = "hello"
# for i in s1:
#     print(i) # 세로로 하나씩 h e l l o 가 나옴

# numbers=[1,2,3,4,5,6,7,8,9,10]
# for number in numbers :
#     print(number) # 1부터 10까지 나옴

# numbers.reverse()
# for number in numbers :
#     print(number) # reverse 라 10 부터 1까지 역순

# # range() *개체* 시작 정수부터 끝 정수까지 이터너블 한 값을 준다???
# range(끝 정수)   #0 ~ 끝 정수-1 까지
# for i in range(10) :
#     print(i) # 0 ~ 9
# range(시작, 끝)  # 시작 ~ 끝 -1 까지
# for i in range(1, 11) : 
#     print(i) # 1 ~ 11
# range(시작, 끝, 스탭)  # 시작 ~ 끝 -1까지인데 스탭(입력한 증감)만큼 차이나게
# for i in range (1, 21, 3) :
#     print(i) # 1부터 20까지 숫자 중에 3씩 + 값

# pass # 아무것도 하지 않고 넘어갈 때(밖으로 나감)
if 1 == 1 :
    pass
print("완료")
for i in range(5):
    pass
print("완료")


# # for문을 사용하여 2부터 30까지 출력해보세요
# for i in range(2, 31) :
#     print(i) # 2부터 차례대로 30까지 나옴

# for문을 사용하여 2부터 30까지 숫자 중 짝수만 출력 ★★★★홀수짝수 예제 다시 풀어라
# for i in range(2, 31, 2) : # 강사님이 알려줌 # 2~30이 들어있음
# #     print(i) # 2부터 30까지 차례대로 짝수만 나옴
#     #if i % 2 == 1: #홀수, 나머지가 1인 값
#     #if i % 2 == 0 : #짝수, 나머지가 0인 값 
#      #continue # 얘를 만나면 다시 위로
#       pass # 아무것도 안하고 그냥 넘어갈 때(밖으로 나감)
#     else : # 짝수
#             print(i)
# for i in range(2, 31) : 
#     if i % 2 == 0:   #짝수, 나머지가 0인값 ★다시 ★



# # for문을 사용하여 10부터 1까지 출력해보세요
# for i in range(10, 0, -1) :
#     print(i) # 10부터 1까지 -1씩 역순으로 나옴 # 내가한거
    #열림,닫힘 범위 0<(포함안함) ≤10(포함)

# 강사님 ex.
# for i in reversed(range(1,11)) :
#     print(i)
# for i in range(1, 11)[::-1]: # <-슬라이싱 [시작인덱스:끝인덱스:방향]
#     print(i)

# i = list(range(6)) # 혼자 걍 연습, 리스트로 변환도 가능함
# i.reverse()  # reversed 리버스와 비슷  // # reverse는 리스트형에서만 사용가능
# print(i) # [5,4,3,2,1]

money = 10000
price = 1000
coffee = 5

# for i in range(coffee) : # coffee = 0~4, 변수의 값 (5니까 0포함 5개) # 반복을 원하는 횟수
#     # print("커피를 구매했습니다") # i에 0넣어서 1번, 1넣어서 1번, 2넣어서 1번 반복 총 5회
#     money -= price # money = money - price 와 같음
# #    print("남은 커피:", coffee-1-i) # 4~0 # i에 0넣고 1번 빼서 4남고 ~~반복~~ 4넣고 5번 빼서 0남음
# #          ★★★★★★★★이거 다시★★★★★★★★★ i는 왜?

# for i in range(1, coffee + 1):
#     print("커피를 구매했습니다")
#     print("남은 커피:", coffee - i )

# for i in range(coffee) :
#     coffee -= 1
#     print("남은 커피:", coffee)

# 두 번째 연습
# for i in range(coffee) : # coffee = 0~4, 변수의 값 (5니까 0포함 5개) # 반복을 원하는 횟수
#     # print("커피를 구매했습니다") # i에 0넣어서 1번, 1넣어서 1번, 2넣어서 1번 반복 총 5회
#     money -= price # money = money - price 와 같음
#     print("남은 커피:", coffee - 1 - i) # 4~0 # i에 0넣고 1번 빼서 4남고 ~~반복~~ 4넣고 5번 빼서 0남음
#     if money < price :
#         break

# for 문은 횟수가 정해져 있는 반복을 할 때 효율적이다.
# while 문은 특정 조건,시점을 만족 시킬 때 까지 반복 할 때 효율적이다.

# prices = [500, 700, 930] #index 기준 0, 1, 2
# money = int(input("돈:")) # 입력되는걸 숫자값으로 인식하게?
# for i in range(len(prices)): # 무조건 괄호 안 부터 # index 기준 0, 1, 2
#     price=prices[i] # ★★요거 왜 넣지 잘 모르겟음★★ 대충 알겟는데 복잡스
#     print(money//price)
#     print(money%price)

# for price in prices : # pirces list의 변수[값]를 바로 꺼내서 pirce에 모두 대입해 사용(각각?)  #for문의 특징
#     print(money//price)
#     print(money%price)

# scores=[]
# for i in range(5) :
#     score = int(input("시험 점수:"))
#     scores.append(score)
#     print(i)

# # for 문으로 구구단 2단 2x1 ~ 2x9
# for i in range(1, 10) : # 1 ~ 9
#     print("2x", i, "=", 2*i) #순차대로 횟수

#  이중for문 : 반복문 안에 반복문 넣기 9단까지
# for i in range(2, 10) : # 2 ~ 9 # 한바퀴 돌고 j 값이 2가 됨  #앞 자리
#     print(i, "단") # i 값이 바뀔 때 단을 출력하기 위해
#     for j in range(1, 10): # 1 ~ 9  # 안 쪽 for문이 먼저  #뒷 자리
#         print(i, "*", j, "=", i*j)
#     print("----------") # 각 단 끝날때 마다 i 값이 바뀌기 전에 들어가게 하기 위해(탭)

