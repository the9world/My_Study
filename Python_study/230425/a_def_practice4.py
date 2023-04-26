# 다음 함수를 정의하세요.
# 정수 n을 입력받고, n보다 작은 수 중
# 3의 배수와 5의 배수를 모두 더 한 합을
# 반환 하는 함수
"""
함수 이름 : sume_3_5
"""
# def sume_3_5(n): # -------풀이 1번-------
#     result=0
#     for i in range(n):
#         if i % 3 == 0 or i % 5 ==0: 
#             result+=i # ★★★★★★ 뭐지 이건 이해안댐
#     return result
# print(sume_3_5(4))

# def sume_3_5(n): # -------풀이 2번-------
#     result=0
#     for i in range(n):
#         if i % 3 == 0
#             result += i
#         elif i % 5 ==0: 
#             result += i
#     return result

# 정육면체 주사위 2개가 있다.
# 2개의 주사위를 던졌을 때 나올 수 있는
# 주사위 눈의 조합을 모두 print 하는 함수를 정의하세요.
"""
함수 이름: draw_dice
출력 예시
1, 2
6, 3
"""
# def draw_dice(): # -------풀이 1-------
#     for i in range(1,7) :
#         for j in range(1,7):
#            print([i,j])
# draw_dice()

# def draw_dice(): # -------풀이 2-------
#     i = 1
#     while i < 7 :
#         j = 1
#         while j < 7:
#             print ([i,j])
#             j +=1
#         i += 1
# draw_dice()

# 두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를
# 계산하고 반환하는 함수를 정의하세요
# "함수 이름 : get_diff"
# def get_diff(a,b) :
#     result = abs(a-b)
#     # if a> b:   # abs(a-b)와 같은 방법
#     #     result = a -b 
#     # else :
#     #     result = b =-a 
#     return result
# print(get_diff(100, 147))

# 가장 큰 수를 만드는 함수 (0~9, 중복 가능)
# 함수에 입력된 5개의 정수를 사용하여 만들 수 있는
# 가장 큰 수를 반환하는 함수를 정의하세요
"함수 이름 : get_biggest"

# def get_biggest(a,b,c,d,e):    # -------다시-------
#     result1 = a*b*c*d*e
#     result2 = a+b+c+d+e
#     ra = [a,b,c,d,e]
#     ra.sort(a,b,c,d,e)
#     ra.remove(0)
#     if result1> result2:
#         return result1
#     else :
#         return result2
# print (get_biggest(7,8,0,4,1))

# def get_biggest(a,b,c,d,e): # ★-------예시 1-------
#     numbers = [a,b,c,d,e] # 입력 받은 숫자
#     numbers.sort()
#     # numbers = [1,2,3,4,5] # 1,2,3,4,5 로 예시
#     result=0
#     for i in range(len(numbers)): #0~4
#         result += numbers[i] * (10**i)
#     return result
# print(get_biggest(5,4,3,2,1))
 
# def get_biggest(a,b,c,d,e): # -------예시2-------
#     numbers= [a,b,c,d,e]
#     numbers.sort(reverse=True)
#     result = ""
#     for i in numbers :
#         result += str(i)
#     return int(result)
# print(get_biggest(5,4,3,2,1))

# 별 찍기 2 : 정수를 함수에 입력하여
# 호출하면 해당 정수 줄의 별을 화면에 출력한다.
# 함수 이름 : print_stars2"
"""
출력 결과
n -> 1
n -> 4
   *
  **
 ***
****
"""
# def print_stars2(n): # ----- 풀이 ------ ???????????????
#     for i in range(1, n+1): # 1 ~ n
#         print(" " * (n-i) , "*" * i) # i= 별 갯수
# print_stars2(4)
