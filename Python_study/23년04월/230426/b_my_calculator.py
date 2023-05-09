# 어제 만든 칼큘을 클래스로 변경
# Mycalculator 클래스로 만들어보세요
# add, sub, mul, div 메소드
# while 문은 클래스 외부에서
# class MyCalculator :
#     def __init__(self,add,sub,mul,div) :
#         self.add=str(n1)+"+"+str(n2)+"="+str(n1+n2)
#         self.sub=str(n1)+"-"+str(n2)+"="+str(n1-n2)
#         self.mul=str(n1)+"*"+str(n2)+"="+str(n1*n2)
#         self.div=str(n1)+"/"+str(n2)+"="+str(n1/n2)
# my_calculator=MyCalculator()
# while True :
#     print("""
#     계산기
#     1: +
#     2: -
#     3: *
#     4: /
#     q: 종료
#     """)
#     operator = input("원하는 계산을 입력하세요:")
#     if operator == 'q' :
#         break
#     n1 = int(input("첫 번째 정수:"))
#     n2 = int(input("두 번째 정수:"))
#     if operator =="1":
#         my_calculator.add(n1, n2)
#     if operator =="2":
#         my_calculator.sub(n1, n2)
#     if operator =="3":
#         my_calculator.mul(n1, n2)
#     if operator =="4":
#         my_calculator.div(n1, n2)
#     break


class MyCalculator :
    def __init__(self):
        pass
    def add(self, n1, n2):
        print(f"{n1}+{n2}={n1+n2}")
    def sub(self, n1, n2):
        print(f"{n1}+{n2}={n1-n2}")
    def mul(self, n1, n2):
        print(f"{n1}*{n2}={n1*n2}")
    def div(self, n1, n2):
        print(f"{n1}/{n2}={n1/n2}")
    # def div(self, n1, n2):
    #     if n2 == 0 :
    #         print("0으로 나눌 수 없습니다.")
    #     else:
    #         print(f"{n1}/{n2}={n1/n2}")
if __name__=="__main__": # 이거 하면 딴데서 불러도 바로안함
    my_calculator= MyCalculator()
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
            if operator == 'q' :
                break
            n1 = int(input("첫 번째 정수:"))
            n2 = int(input("두 번째 정수:"))
            if operator =="1":
                my_calculator.add(n1, n2)
            if operator =="2":
                my_calculator.sub(n1, n2)
            if operator =="3":
                my_calculator.mul(n1, n2)
            if operator =="4":
                my_calculator.div(n1, n2)
else:
    print(__name__)

# class ZeroCalculator(MyCalculator):
    # def div(self, n1, n2):
    #     if n2 == 0 :
    #         print("0으로 나눌 수 없습니다.")
    #     else:
    #         print(f"{n1}/{n2}={n1/n2}")
# zero_calculator = ZeroCalculator()
# zero_calculator.div()