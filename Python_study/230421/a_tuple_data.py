# tuple(튜플)형
# element의 값이 한 번 정해지면 값을 수정 할 수 없다.
# mutable (수정 가능한) list, dict
# immutable (수정 불가한) int(정수), float(소수), str(문자), tuple
# +,* 사용 가능 (연결, 반복 출력)
# ex. a= 10, a+=10 = 20 해당 값 위치로 연결함, 수정이랑 다름
# my_list = [1,2,3]
# my_list[0]=5
# print(my_list) # [5,2,3]
# my_tuple = (1,2,3)
# my_tuple[0]= 5 # error
# print(my_tuple) # 바뀌면 안 되는 값에 주로 사용

tuple_1 = ("Hello","world","python")
t2 = (1,2,3,4,5)
t3 = (1,2,"Hello")
t4 = 1,2,3
t5 = (1,2,(3,4,5))
t6 = tuple_1+ t2
t7 = t3 * 3
t8 = (5,3,1,4,2)
print(t3[2]) # Hello __ 인덱싱은 앞 자리만 작성해도 가능
print(t3[0:2]) # 1,2 __ 슬라이싱은 뒷 자리까지 작성
# 슬라이싱은 할당되어 있는 타입(튜플)으로 가져옴
print(len(t3))
print(t5[2][1]) # 4 __ [2]는 첫 번째 인덱싱, [1]은 두 번째 인덱싱
# 정렬, 추가 및 대부분의 함수는 값 수정이라 사용 불가

for i in t8 :
    print(i) # for문 : 인덱스 순서대로 for 문에 들어감

