# li_1=["Hello", "World", "Python"]
# li_1의 원소를 사용하여
# hello World Python 이라고 출력 하세오.
# print(li_1[0], li_1[1], li_1[2])
# print(li_1[0] + " " + li_1[1] + " " + li_1[2]) #" "공백 넣어 준 것
# join(리스트)
# 리스트의 문자열을 합친다
# print(" ".join(li_1)) # ["Hello", "World", "Python"]

# li_1의 원소를 사용하여
# Help라고 출력 하세오. #append도 가능?
# print(li_1[0][0:3]+li_1[2][0]) # 앞 [0]은 헬로 뒤 [0:3]은 글자수
# print(li_1[0][0]+li_1[0][1]+li_1[0][3]+li_1[2][0])  # Help

# li_2=[1,2,3]
# # li_1과 li_2를 사용하여
# # ["Hello", "World", "Python", 1,2,3] 을 출력 하세요
# print(li_1+li_2)
# li_1.extend(li_2)
# print(li_1) # ["Hello", "World", "Python", 1,2,3]

# li_1과 li_2를 사용하여
# ["Hello", 1, "World", 2, "Python", 3] 을 출력 하세요
# print([li_1[0], li_2[0], li_1[1], li_2[1], li_1[2], li_2[2]])
# 마지막 일 댄 괜찮은데 중간에 끼면 이상해짐

# li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[1])
# li_1.insert(5, li_2[2])
# print(li_1)

# li_1 = ["Hello", "World", "Python"]
# li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[2])
# li_1.append(li_2[2])
# print(li_1) #["Hello", 1, "World", 2, "Python", 3]