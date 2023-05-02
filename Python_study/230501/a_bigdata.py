# 가변공간 파이썬
# 비교연산자
# id 함수
# colab 런타임 연결

'''3 & 4 # & : 논리연산자가 X -> 비트연산자'''
# 0011 & 011 -> 0000
# 3 and 4 : 4
# 3 or 4 : 3

# 같은 복사 , 깊은 복사
# a= [5,4,3,2,1]
# b=a[:] 
# print(id(a), id(b))
# b # 54321
# a.sort() 
# a # 12345
# b # 54321

# a = [5,4,3,2,1] 
# b = a.copy() # 원본에 영향을 줌
# print(id(a), id(b))
# a. sort()
# a # 12345
# b # 54321
# a # 12345

# import copy
# a = [5,4,3,2,1]
# b=copy.deepcopy(a) # 원본에 영향을 주지 않음 (아예 새로 생성)
# print(id(a), id(b))
# a.sort()
# a
# b
# a

# is 연산자 
# is 는 int로 따지면 -5~256 까지의 작은 숫자는 파이썬 내부적으로 캐시돼있어서
# 다른 변수에 같은 값을 넣어도 같은 메모리 주소를 참조합니다.
# 하지만 257이상의 숫자는 다른변수에 정의하면 값이 같아도 다른 주소에 할당됩니다.
# String도 ‘teemo’같이 짧은건 같은 주소에 할당되지만,
# ‘teemo is the cutest champion in league of legends’와 같이 긴건 다른 주소에 할당됩니다.


# b 로 a 를 나눈 나머지가 3 초과면 실패, 3이면 무승부, 3 미만이면 성공이 출력되도록 만들어보자
# a = 34
# b = 4
# if  a % b > 3 : 
#   print ("실패")
# elif a % b == 3:
#   print ("무승부")
# else :
#   print("성공")

# 무슨 학교 다니세요?  
# 태어난 연도를 계산하여 학교 종류를 맞추는 프로그램
# 당신이 태어난 연도를 입력하세요
# 2000
# 당신은 학생이 아닙니다
# 나이는 현재년도- 태어난 년도 +1 로 계산
# 26세 이하 20세 이상이면 "대학생", 20세 미만 17세 이상이면 "고등학생",
# 17세 미만 14세 이상이면 "중학생", 14세 미만 8세 이상이면 "초등학생",
# 그 외의 경우는 "학생이 아닙니다" 출력

# birth_year = int(input('당신의 태어난 년도를 입력해주세요.'))

# age = 2023 - birth_year+1

# message = ""
# if 20<=age and age<=26:
#     message="대학생"
# elif 17<=age and age<20:
#     message="고등학생"
# elif 14<=age and age<17:
#     message="중학생"
# elif 8<=age and age<14:
#     message="초등학생"
# else:
#     print('학생이 아닙니다.')
# print(message)

# 양의 정수 하나를 입력 받아 이 정수가 2의 배수인지 3의 배수인지 작성하시오
# a = int(input("양수를 입력하세요"))

# num = int(input('정수를 하나 입력하세요.'))

# if num %2==0:
#     if num%3==0:
#         print('2와 3으로 나누어 집니다.')
#     else : 
#         print('2로 나누어집니다.')
# elif num %3==0:
#     print('3으로 나누어 집니다.')
# else:
#     print('어느 것으로도 나누어지지 않습니다.')

# set() : 집합 : 중복이 없다. 순서가 없다.
# add() : 집합에 요소를 추가합니다.
# set1 = set([1, 2, 3]) # {1, 2, 3} 출력
# set1.add(4) # {1, 2, 3, 4} 출력
# # update() : 해당 집합에 다른 집합을 추가합니다.
# # 직접 집합을 작성하여 추가하거나 다른 집합을 추가 할 수 있습니다.
# set1 = set([1, 2, 3]) 
# set1.update([4, 5, 6]) # {1, 2, 3, 4, 5, 6} 출력
# set2 = {7, 8, 9}
# set1.update(set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9} 출력
# # remove() : 집합에 해당 요소를 제거합니다.
# set1 = set([1, 2, 3])
# set1.remove(3) # {1, 2} 출력
# # clear() : 집합 내에 모든 요소를 제거합니다.
# set1 = set([1, 2, 3])
# set1.clear() # set() 출력(빈 집합)
# #union() : 집합들의 합집합을 구합니다. 또한 | 연산자를 사용할 수 있습니다.
# set1 = set([1, 2, 3])
# set2 = set([3, 4, 5])
# set3 = set1.union(set2) # {1, 2, 3, 4, 5} 출력, set1 | set2 과 같음
# # intersection() : 집합들의 교집합을 구합니다.
# # 또한 & 연산자를 사용할 수 있습니다.
# set1 = set([1, 2, 3])
# set2 = set([2, 3, 4])
# set3 = set([1, 2, 5])
# set4 = set1.intersection(set2).intersection(set3) # {2} 출력, set1 & set2 & set3 과 같음
# # difference() : 집합들의 차집합을 구합니다.
# # 또한 - 연산자를 사용할 수 있습니다.
# set1 = set([1, 2, 3])
# set2 = set([2, 3, 4])
# set3 = set1.difference(set2) # {1} 출력, set1 - set2와 같음

# break 나감 pass 지나감 continue 다시
# i = 1
# while i <= 10 :
#   if i % 2 == 0:
#     print(i)
#   i += 1 

# for count in range(5, -1, -1):
#     print(count) # 5 4 3 2 1 

# 1. 계단형, n을 입력받아, n 만큼 줄을 만들고 계단 형태로 별 찍기
# 2. 삼각형, 왼쪽 아래가 직각인 n만큼의 높이를 가지는 직각삼각형
# 2-1. 오른쪽 아래가 직각인 n만큼의 높이를 가지는 직각삼각형
# 3. 역삼각형, 왼쪽 위가 직각인 n 만큼의 높이를 가지는 직각삼각형
# 3-1. 오른쪽 위의 직각인 n만큼의 높이를 가지는 직각삼각형
# 4. 피라미드, n 만큼의 높이를 가지는 홀수개의 별 피라미드

## 1 번 (계단형)   i = 별갯수
# n = int(input('n:'))
# for i in range(n):
#    print(' '*i,end=' ') # end의 역할을 sep과 비슷한 기능(구분자 사용)
#    print('*'*n)

## 2 번 (삼각형)
# n = int(input('n:'))
# for i in range(1,n+1):
#   print('*'*i)

## 2 번 
# def stars(n): #  2번
#     for i in range(1, n+1):
#         print("*"*i)
# stars(5)

# 2 - 1 번 
# n = int(input('n:'))
# for i in range(1, n+1):
#   print(' '*(n-i), end='')
#   print('*'*i)

# 2 - 1 번
# def stars2(n): # 3번
#     for i in range(1, n+1):
#         print(" " * (n-i) , "*" * i)
# stars2(5)

# 3번 (역삼각형)
# n = int(input('n:'))
# for i in range(n):
#   print('*'*(n-i))

# 3-1 번
# n = int(input('n:'))
# for i in range(n):
#   print(' '*i, end='')
#   print('*'*(n-i))

# 4 번 (피라미드)
# n = int(input('n:'))
# for i in range(1,n+1):
#   print(' '*(n-i), end='')
#   print('*'*(2*i-1))

# (1) x = [3, 6, 9, 20, -7, 5] 의 값의 모든 요소에 10을 곱한뒤 출력하세요.
# 심화 : 출력과 리스트 x 의 값에도 모두 10을 곱해주세요.
# (2) y = {"math":70, "science":80, "english": 20} 의 값의
#   모든 요소에 10을 더한 뒤 출력하세요.
# 심화 : 출력과 딕셔너리 y의 값에도 모두 10을 더해주세요.
# (3) 숫자를 입력받고 입력받은 정수의 구구단을 출력하세요.

# # 1번
# x = [3,6,9,20,-7,5]
# for i in x:
#     print (i*10)
# # 1번 심화
# for i in range(0, len(x)):
#     x[i] = x[i]*10
# print(x)
# 2번
y = {"math":70, "science":80, "english": 20}
# for key in y:
#     val = y[key]
#     y[key] = y[key]+10
#     print('%s : %d' %(key,val+10))
# # 2번 심화
# y = {"math":70, "science":80, "english": 20}
# for key in y:
#     val = y[key]
#     y[key] = y[key]+10
#     print('%s : %d' %(key,val+10))
# 3번

# import random # ------- 다시 
# true_value = random.randint(1,100)
# answer= int(input("숫자:")) # 임의의 값 할당
# while True :
#     if answer != true_value :
#         answer=int(input("숫자:"))
#         print("입력한 숫자가 큽니다")
#         continue
#     elif answer < true_value :
#         print("입력한 숫자가 작습니다")

# import random
# true_value = random.randint(1,100)
# input_value= 9999 # 임의의 값 할당
# print('숫자')
# while true_value != input_value :
#     input_value = int(input())
#     if input_value>true_value: # 사용자의 입력값이 true_value 클때
#         print('숫자가 큽니다')
#     else :
#         print('숫자가 작습니다') # 사용자의 입력값이 true_value보다 작을 때
# print(f"정답입니다. 입력한 숫자는 {true_value}입니다.")

'''(1) word = ["school", "game", "piano", "science", "hotel", "mountain"]
중 글자수가 6글자 이상인 문자를 모아 새로운 리스트를 생성하세요'''
# word = ["school", "game", "piano", "science", "hotel", "mountain"]
# b= list() # 새로운 리스트 생성
# for i in range(len(word)):
#     if len(word[i]) >= 6:
#         b.append(word[i])
# print(b)

"""
1부터 100까지 숫자중
3과 5의 공배수일 경우 "3과 5의 공배수"
나머지 숫자중 3의 배수일 경우 "3의 공배수"
나머지 숫자중 5의 배수일 경우 "5의 배수"
모두 해당되지 않는 경우 그냥 숫자를 출력하세요
"""
# answer = int(input('숫자:'))    ####retry
# for a in range(1,101):
#     if answer % 3==0 and answer % 5==0:
#         print("3과 5의 공배수")
#     elif answer % 3==0 :
#         print("3의 공배수")
#     elif answer % 5==0 :
#         print("5의 배수")
#     else:
#         print(answer)

# 심화 문제 (1-입력한 숫자까지의 숫자중)
# b = int(input('정수를 입력하세요.')) #### 해답
# if b<=0:
#     print('음수는 정의하지 않음.')
# else:    
#     for a in range(1,b+1):
#         if a%3==0 and a%5==0: 
#             print('3과 5의 공배수')
#         elif a%3==0:
#             print('3의 배수')
#         elif a%5==0:
#             print('5의 배수')
#         elif 1<=a<=100:
#             print(a)
#         else:
#             print('1과 100사이 숫자가 아닙니다.')

"""사용자로부터 숫자를 계속 입력받다가
s or S 를 입력하면 합계 출력
"""
# a = int(input("숫자")) ###### -----retry
# while True :
#     if not input("s") or input("S"):
#         a += int(input())
#     else:
#         break
# print(a)

# c = 0
# d = 1
# while (d==1):
#     a = input()
#     if a=='s' or a=='S':
#         d=0
#     else:
#         a = int(a)
#         c+=a
# print(c)

'''사람 별 평균을 구하라.'''
# kor_score = [39,69,29,100,80]
# math_score = [32,59,85,30,90]
# eng_score = [49,70,48,60,100]

# mideterm_score = [kor_score, math_score,eng_score]

# student_score = [0,0,0,0,0]
# i=0
# for subject in mideterm_score: #kor,math,eng 과목 선택
#     for score in subject: #과목 선택후
#         student_score[i]+=score #각 학생마다 개별로 교과 점수를 저장
#         # print(subject,score,'i:',i,student_score) #kor->math->eng 
#         i+=1 #학생 index 구분
#     i=0 # 과목이 바뀔 때 학생 인덱스
# else:
#     a,b,c,d,e = student_score  #학생별 점수를 unpacking
#     student_average = [a/3,b/3,c/3,d/3,e/3]
#     print(student_average)


# 포맷팅 플루팅 에러
# 16까진 가능 17자리부터 에러
# print('나눗셈. {:.17}'.format(1/3))

# https://github.com/Youngpyoryu/Lecture_Note/tree/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC