# li_3 = [1,2,[3,4,5,[5,6,[7,8,[9,10]]]]] #출력 결과가 [2,3]이 되도록 만드시오.
# print(len(li_3[3])) #len 사용법
# print(li_3)
# print(li_3[2][2][2][2][1])

# + 연산자
# 리스트를 연결 한다.
# extend(확장, (리스트)) + 함수와 같다
# li_1=[1,2,3]
# li_2=[4,5,6]
# print(li_1+li_2) #[1,2,3,4,5,6] # 리스트 결합

# li_1.extend(li_2)  # li_1과 2를 연결
# print(li_1) # [1,2,3,4,6] 
# print(li_2) #[4,5,6]

# * 연산자
# 리스트를 반복한다 
# li = [1,2,3]
# print(li*3) # [1,2,3,1,2,3,1,2,3]

# pop(인덱스)
# 리스트의 인덱스 위치의 요소(값)를 *꺼낸다 = 튀어나오다*
# 인덱스를 함수에 전달하지 않으면 제일 마지막 요소를 *꺼낸다 = 튀어나오다*
# 리스트 안의 값을 꺼내서 따로 저장 가능
# li = [1,2,3,4]
# a = li.pop()
# li.pop()
# print(li) # [1,2,3]
# print(a) # 4
# b=li.pop(1)
# print(li) # [1,3]
# print(b) #2

# append(ex.원소) #추가
# 리스트의 마지막에 원소를 추가
#li_4=[1,2,3]
#li_4.append(4)
#li_4.append("문자")
#li_4.append([1,2,3])
#print(li_4)

# a_1=[6,5,7,8]
# a_2=[9,11,10,[13,12,14]]
# a_1.sort()
# a_1.append(a_2)
# print(a_2) ★ 안댐★

# n_1={1: 'a'} # dictionary 형태 #★★★★★★★★★★★★★★★★★★★★★★★★★★★★
# n_1['b']=2  #'b':2 key-value 쌍 추가, list와 다르게 ?
# n_1[1] = 'c'
# del n_1[1] #del 해당 데이터를 삭제한다
# print(n_1)

# for i in (range(2, 21)) [: : -1] :
#     print(i)

# cnt = 10  
# while cnt >0: # while cnt >= 1 과 같음  
#     print(cnt)  
#     cnt -= 1 # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 위와 동일하게 
    

# list=(1,2,3,4,5,6,7,8,9)
# for i in range(1, 10) :
#     i+=1
#     print(i)

# a = float(input("영어 점수를 입력하세요(ex : 4.0, 4.5) : "))
# b = float(input("수학 점수를 입력하세요(ex : 4.0, 4.5) : "))
# c = float(input("국어 점수를 입력하세요(ex : 4.0, 4.5) : "))
# d = float(input("과학 점수를 입력하세요(ex : 4.0, 4.5) : "))
# e = float(input("체육 점수를 입력하세요(ex : 4.0, 4.5) : "))


# i =(a+b+c+d+e)/5
# a=int(i)

# if (i-a) <0.5 :
#     print(a)
# else :
#     print(a+1)

# i = int(a+b+c+d+e)/5

# print (round(i, 2))

## 모르겟다



# a= int(input("몇 단:")) # 원하는 구구단

# for i in range(1,10) :
#             if 10 >= a > 1 :
#                   print(a,"x",i*1,"=",a*i)
#                   i+=1
#             pass
# else
# print("2~9의 숫자 중 하나를 입력하세요")

#  이중for문 : 반복문 안에 반복문 넣기 9단까지
for i in range(2, 10) : # 2 ~ 9 # 한바퀴 돌고 j 값이 2가 됨  #앞 자리
    print(i, "단") # i 값이 바뀔 때 단을 출력하기 위해
    for j in range(1, 10): # 1 ~ 9  # 안 쪽 for문이 먼저  #뒷 자리
        print(i, "*", j, "=", i*j)
    print("----------") 
      
# a=2
# for i in range(1,10):
#       if i >= 1 :
#          print (a,"x",i,"=",a*i)
#          i+=1
#       if a >= 1 :
      
#             a+=1