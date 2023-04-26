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

def add(a,b):
    result = str(a)+"+"+str(b)+"="+str(a+b)
    print(result)
    with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
        f.write(result)
def sub(a,b):
    result = str(a)+"-"+str(b)+"="+str(a-b)
    print(result)
    with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
        f.write(result)
def mul(a,b):
    result = str(a)+"*"+str(b)+"="+str(a*b)
    print(result)
    with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
        f.write(result)
def div(a,b):
    result = str(a)+"/"+str(b)+"="+str(a/b)
    print(result)
    with open("Python_study/230425/2.new_file/calculator.txt", "a", encoding="utf-8")as f:
        f.write(result)
while True :
    print("""
         계산기
         1: +
         2: -
         3: *
         4: /
         q: 종료
        """)
    operator = input("원하는 계산을 입력하세요:")
    if operator == 'q':
        break
    a = int(input("정수 1: "))
    b = int(input("정수 2: "))
    if operator == "1" :
        add(a,b)   
    elif operator == "2" :
        sub(a,b)
    elif operator == "3" :
        mul(a,b)
    elif operator == "4" :
        div(a,b)
    break