"""
eng 변수, kor 변수, mat 변수를 만들고
각 변수는 과목의 시험 점수이다.
영어 점수는 80점
국어 점수는 60점
수학 점수는 50점
3과목 점수의 평균을 내고 
평균 점수에 따라 성적을 출력한다.
A : 91 ~ 100
B : 81 ~ 90
C : 71 ~ 80
D : 61 ~ 70
F : 60 이하
"""
        # 처음에 했던 수업 1번
# eng = input("영어 점수:") #80
# eng = int(eng) #위아래 동일 
# kor = int(input("국어 점수:")) #60
# math =int(input("수학 점수:")) #50

        # 이어서 두 번째 수업
"""scores = []
scores = list()
scores.append(int(input("영어 점수:"))) # input이 안되서?? 문자형 데이터라 int 정수로 바꿔준다
scores.append(int(input("국어 점수:")))
scores.append(int(input("수학 점수:")))"""


#avg= (scores[0]+scores[1]+scores[2])/3 # 두 번째 수업
# sum()
# 리스트의 요소를 모두 더한다. # 더하기는 숫자끼리만 된다.
# avg= sum(scores) /3 # 두 번째 수업

"""avg = (eng+kor+math) /3 # 첫 번째 수업 
if 91<= (eng+kor+math)/3:
     print("A")
elif 81<= (eng+kor+math)/3:
     print("B")
elif 71<= (eng+kor+math)/3:
     print("C")
elif 61<= (eng+kor+math)/3:
     print("D")
elif 60<= (eng+kor+math)/3:
     print("F") """ #첫 번째 수업

""" if avg>=91:
    print("A")
elif avg>=81:
    print("B")
elif avg>=71:
    print("C")
elif avg>=61:
    print("D")
elif avg<=60:
    print("F") """ # 첫 번째, 두 번째 수업

# input() 함수
# 정보를 입력받는 함수 (=변수에 할당하는 연산자)
# user_input = input() #사용자의 입력(input)을 받고 출력함
# print(user_input) #()가 우선

# 정수형 변환 함수
# int()
# 정수형, integer형, int형
# int(값)

# 나이와 가지고 있는 돈을 입력 받는다.
# 가지고 있는 돈으로 물건을 몇 개 살 수 있는지 와 잔 돈을 출력한다.
# 물건의 가격은 500 원 이다.
"""age=input("나이:")
money=int(input("돈:")) #int 정수로 바꾸기 위해 (실수(소수점) 나오면 이상해져서)
price=500
print(money//price) #//몫 연산자 사용
print(money%price)"""

"""money % 물건
print("최대 구매 수량", money//물건)
print("잔 돈", money%물건)""" # 이거 틀림

age=input("나이:")
money=int(input("돈:"))
price = [1000, 50, 120]
print("커피",money//price[0], money % price[0]) # []인덱싱, [:] 슬라이싱 
print("콜라",money//price[1], money % price[1])
print("물", money//price[2], money % price[2])

# 나이와 가지고 있는 돈을 입력 받는다.
# 가지고 있는 돈으로 물건 별로 각 각 몇 개 살 수 있는지 와 잔 돈을 출력한다.
# 물건의 가격은 1번 물건 1000 원 이다. 2번 물건 50원, 3번 물건은 120원이다.
