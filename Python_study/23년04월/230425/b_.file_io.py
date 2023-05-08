# 파일 입·출력
# Python에서 파일 생성 및 수정

# open("파일 이름", 파일 열기 모드) 
# Python 내장 함수
# 파일을 열고, 파일 객체를 리턴 한다.
# 1. 절대 경로: C:/, D:/ 처럼 최상단 경로부터 나타낸 경로
# 2. 상대 경로: 현재 작업 위치부터 나타낸 경로

# f = open("C:/Users/5/My_Study/Python_study/새파일.txt", 'w')
# f.close()  
# a = open(r"C:\Users\5\My_Study\Python_study\새파일1.txt", 'w')
# a.close()
# \ 사용 하려면 맨 앞에 r을 붙여 준다. (r"C:/")

# 파일 열기 모드
# r : 읽기 모드, 파일을 읽기만 할 때 (read)
# w : 쓰기 모드, 파일에 내용을 쓸 때 & 덮어쓰기 (write)
# a : 추가 모드, 파일 마지막에 내용을 추가 할 때 (append)
# w, a 는 파일이 없으면 새로 생성한다

# f = open("Python_study/새파일.txt", 'w', encoding="UTF-8")
# for i in range(1,11):
#     print(i, "번째 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()

# f = open("Python_study/새파일.txt", 'a', encoding="UTF-8")
# for i in range(11, 21) :
#     print(i, "번째 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()

# f = open("C:/Users/5/My_Study/Python_study/230425/2.new_file/새파일.txt", 'r', encoding="utf-8")
# #readline() 함수
# # 첫 번째 줄 부터 1줄 읽어 온다.
# # 커서가 이동하는 것처럼 읽어옴

# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# f.close()

# while True : #전부 읽기
#     line = f.readline()
#     if line == "": #문자가 더이상 없을 때
#         break  # 탈출
#     print(line)
# f.close()

# readlines() 함수
# 파일의 모든 줄을 읽어서 리스트로 변환 (한 줄 단위)
# f = open("C:/Users/5/My_Study/Python_study/230425/2.new_file/새파일.txt", 'r', encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line)

# read() 함수
# 파일 내용 전체를 문자열로 리턴한다. (문자열 한 덩어리)
# f = open("C:/Users/5/My_Study/Python_study/230425/2.new_file/새파일.txt", 'r', encoding="utf-8")
# data = f.read()
# print(data)
# f.close()

# for 문으로 읽기
# f = open("C:/Users/5/My_Study/Python_study/230425/2.new_file/새파일.txt", 'r', encoding="utf-8")
# for line in f:
#     print(line)
# f.close()

# with문
# open - close를 자동으로 해준다.
# with open("C:/Users/5/My_Study/Python_study/230425/2.new_file/새파일.txt", 'r', encoding="utf-8") as f:
#     f.write("end of file") # 파일 마지막에 드감
#     f.write("1")
#     f.write("2")
#     f.write("3")
#     f.write("4\n")

# csv(comma separated values)
# ,로 구분되는 값들을 모아놓은 파일
# 이름,입실시간,퇴실시간 (띄어쓰기 안 함/ 콤마 대신 탭 사용 가능)
# 김정은,10:30,12:30
# 황덕우,09:00,18:11
# with open("Python_study/data.csv", "w", encoding="utf-8")as f:
#     f.write("날짜, 날씨, 기온\n")
#     f.write("20230424, 맑음, 10도\n")
#     f.write("20230425, 비, 5도\n")
#  ----★ 엑셀에서 한글로 보려면 ansi 파일 이어야함
# with open("Python_study/data.csv", "r", encoding="utf-8")as f:
#     data=f.readlines()
#     print(data)

# 계산 결과 저장 함수
# 정수 2개를 입력받고 두 수를 더 한 결과를
# add_result.txt 파일에 저장하는 함수를 정의하세요
"함수 이름 : add_write"
# def add_write(a,b):
#     c = a+b
#     with open("Python_study/230425/new_file/add_result.txt", "w", encoding="utf-8")as f:
#         f.write(str(c))
# add_write(3,7)

# with open("Python_study/230425/new_file/add_result.txt", "r", encoding="utf-8")as f:
#     add_result=f.readlines()
#     print(add_result)

# 텍스트 파일에 적힌 정수 2개를
# 읽어와서 정수 2개를 더한 결과를 print 하세요.
""" 텍스트 파일 이름 : add_number.txt
# 경로 : Python_study/add_number.txt
# 함수 이름 : read_add_print """
# def read_add_print():
#     with open("Python_study/add_number.txt", "r", encoding="utf-8")as f:
#         data= f.read()
#         a= int(data[0]) ; b=int(data[2]) ; c=int(data[4])
#         print(a+b+c)
# read_add_print()

# def read_add_print(): # 파일 안에 4,5,6,4,4
#     with open("Python_study/123.txt", "r", encoding="utf-8")as f:
#         data= f.read()
#         count=data.count("4")
#         a= int(data[0]) ; b=int(data[2]) ; c=int(data[4])
#         print(a+b+c, count)
# read_add_print() # 15, 3

