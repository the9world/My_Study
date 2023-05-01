def add(a, b):
    return a + b
def sub(a, b):
    return a - b

if __name__ == "__main__" : # __name__ = 내가 실행한 파일 이름
# name == main 인 경우 밑에 내용이 수행 됨
# name != main 인 경우 __name__(해당 파일 이름) 이 출력 됨
    print (add(1, 2))
    print (sub(3, 4))
else:
    print(__name__)
# 실행을 한 곳(파일)이 __main__이 됨
# 실행을 당한 파일이 module(__name__)이 됨
