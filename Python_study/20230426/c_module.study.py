# 모듈(module)
# 함수, 변수, 클래스 모아놓은 파이썬 파일
# 다른 파이썬 프로그램 파일에서 불러와서 사용
# import 명령어로 불러옴
"""
import 모듈이름
"""
# import my_module #모듈을 통해서 호출
# my_module.add(1,2)
# my_module.sub(1,2)
"""
from 모듈이름 import 모듈함수
from 모듈이름 import 모듈함수1, 모듈함수2
from 모듈이름 import *(전체, 모두)
"""
# from my_module import add, sub
# # 특정해서 꺼내옴, 함수 이름으로 바로 호출
# add(1, 2)
# sub(1, 2)

# from my_module import *
# add(1, 2)
# sub(1, 2)
# import my_module
# 실행을 한 곳(파일)이 __main__이 됨
# 실행을 당한 파일이 module(__name__)이 됨
from b_my_calculator import MyCalculator
# my_calculator = MyCalculator()
# my_calculator.div(10, 0) # error,  0 으로 나눌 수 없음
# 컨트롤+메소드(div)클릭하면 정의된 부분으로 이동
# 상속으로 0으로 나누지 못하게 하는 법
class ZeroCalculator(MyCalculator):
    def div(self,n1,n2) :
        if n2 > 0 : # n2가 0이면
            print("0으로 나눌 수 없습니다.") # error 0으로 나눌 수 없음
        else:
            print(f"{n1}/{n2}={n1/n2}")
zero_calculator = ZeroCalculator()
zero_calculator.div()

# https://wana.tistory.com/13