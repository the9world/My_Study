# for 문 예시
# test_list = ['one', 'two', 'three'] 
# for i in test_list: 
#     print(i)

# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#      print(first + last)

# add = 0 #### 0, 1 = 1 / 1, 2 = 3/ 3, 3 = 6 / 6 + 4 = 10 / 10 + 5 = 15
# for i in range(1, 6): 
#     add= add + i
#     print(add)

# for i in range(4, 8):
#     print(i)

# num = int(input('정수를 하나 입력해주세요:'))
# for i in range(num) :
#     print (num) # 3 3 3 , 3을 3번

# def add(a,b):
#     result = str(a)+"+"+str(b)+"="+str(a+b)
#     print(result)
#     with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
#         f.write(result)
# def sub(a,b):
#     result = str(a)+"-"+str(b)+"="+str(a-b)
#     print(result)
#     with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
#         f.write(result)
# def mul(a,b):
#     result = str(a)+"*"+str(b)+"="+str(a*b)
#     print(result)
#     with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
#         f.write(result)
# def div(a,b):
#     result = str(a)+"/"+str(b)+"="+str(a/b)
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

# def solution(a, b): ★ 검토
#     answer = 0
#     if a%2 == 1 and 1 == b%2 : 
#         return a**2 + b**2
#     elif a%2== 1 or 1 == b%2 :
#         return 2*(a+b)
#     else:
#         return abs(a-b)
#     return answer

# a = [i for i in range(10)]        # 0부터 9까지 숫자를 생성하여 리스트 생성
# print(a) # range 값을 한번씩 i에 넣은후 i가 받은 값을 맨 앞 i 에게 전달?
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)

# list_a = []
# for i in range(2):
#     for j in range(4):
#         list_a.append(j)
# print(list_a)

# list_a = [ j for i in range(2) for j in range(4)]
# print(list_a) 

# list_a = list(range(10))
# list_b = []
# for i in list_a:
#     if i >= 5:
#         list_b.append(i)
# print(list_b)

# list_b = [i for i in list_a if i >= 5] 
# print(list_b) # 조건이 1개 일때만 맨 앞 i 빼고 그 뒤론 위에서 아래로 쓰듯

list_a = list(range(10))
# list_b = [i if i >= 5 else "under" for i in list_a]  
# print(list_b)# 조건이 2개 이상일땐 맨 앞 i 그리고 for 문이 맨 뒤 그외엔 정순

# --------------------
# list_b = [j for j in range(5) if j > 1 for i in range(3) if i == 2]
# print(list_b) # 2번

# list_b= []
# for i in range(3):
#     if i == 2:
#         for j in range(5) :
#             if j > 1:
#                 list_b.append(j)
# print(list_b) # 2번

# --------------------------------
# list_b = [i if i > 3 else "same" if i == 2 else "under" for i in list_a ]
# print(list_b)

# li_b=[]
# for i in range(10):
#     if i>3:
#         li_b.append(i)
#     if i==2:
#         b="same"
#         li_b.append(b)
#     else:
#         c="under"
#         li_b.append(c)
# print(li_b) # --------------다시

# ----------------------------------
# result = [x*y for x in range(2,3) for y in range(1,5)]
# print(result) # 뒤 포문이 위로

# result1 = [] 
# for c in range(1,5):
#     for d in range(2,3):
#         result1=[c*d]
#     print(result1)
# -------------------- 다시