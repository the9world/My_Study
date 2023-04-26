# 객체지향(oop, object oriented programming)
# 객체와 객체 사이의 상호작용으로 프로그램을
# 구성하는 프로그래밍 패러다임

# 객체지향의 특징
# 1.추상화(Abstration) # rpg 게임 직업 전사 등등
#  공통된 속성이나 기능 도출(주요한 특징만 남김)
# 2.캡슐화(Encapsulation) # rpg 게임 작동, 이동 공격 등등
#  데이터의 구조와 연산을 결합(연산 등 캡슐 하나에 합침)
# 3.상속(Class Inheritance) # 전사 베이스로 업/ 다운그레이드
#  상위 개념의 특징이 하위 개념에 전달됨(추가, 변경 가능)
# 4.다형성(polymorphism) # 몰라 
#  유사 객체의 사용성을 그대로 유지(유지하면서 변경 가능)
# 객체는 추상화와 캡슐화의 결과
# 객체는 데이터 필드와 메소드를 가진다
# 프로그램상의 구현 된 어떤 것(데이터, 값, 물건 등)

# 클래스는 객체를 정의한 것(객체의 설계도) 붕어빵 틀?
# 데이터 필드(멤버 변수, 속성): 객체가 가지고 있는 변수
# 메소드: 객체가 가지고 있는 함수
"""
class 클래스 이름 :
    클래스 멤버 변수
    메소드
"""
# 클래스 이름 규칙도 변수 이름 규칙과 같다
# 클래스 이름 컨벤션(관용)
# 첫 글자 대문자
# 언더스코어(_) 안 쓰기
# 단어 구분될 때 대문자
# class Car : # 여기를 호출해야 아래를 실행
# # class 내부에 있는 것들이 메소드, 멤버함수
#     def move(self):
#         print('move')

# class SportsCar:
#     pass

# 인스턴스
# 클래스를 통해 생성된 객체
# class Car에 의해서 만들어 진 값 인스턴스, 객체
# class Car안에 있는 것이 메소드, 멤버함수
# my_car = Car() # 호출
# my_car.move()
# # . : 객체 멤버 접근 연산자
# li = [1,2,3,4,5] # 객체 멤버 접근연산자 (예시)
# li.append(6)
# li1=(1,2,3,4,5) # 튜플
# li2={5,5,5,5} # set #순서가 없고 중복 안됨
# print (li2) # 중복은 안되므로 5 하나만 나옴
# # Python에서는 모든 것이 다 객체다.
# # 내장함수 Type()
# print(type(li))
# print(type("하이"))
# print(type(1))
# print(type(1.1))
# print(type(li1))
# print(type(li2))

# str(문자열) 메소드
# 파이썬에서 스트링 객체는 임뮤터블(수정 불가능)
# upper(): 모두 대문자로 변경
# lower(): 모두 소문자로 변경
# strip(): 문자열 양쪽 끝의 특정 문자를 제거 [lstrip(왼), rstrip(오)]
# s = "  Hello  "
# print(s.upper())  # "  HELLO  "
# print(s.lower())  # "  hello  "
# print(s.strip())  # "Hello"
# print(s.lstrip()) # "Hello  "
# print(s.rstrip()) # "  Hello"

# # split(): 구분자로 분할하여 리스트로 변환
# # replace(): 문자열의 특정 부분을 대체
# s2 = "Hello,World,Python"
# print(s2.split(',')) # ['Hello', 'World', 'Python']
# print(s2.replace(',',' ')) # Hello World Python
# # s2 = s2.replace(',',' ') ; print(s2) # 위와 같은 방식

# s3 = "Hello" # H 를 소문자로 바꾸기
# # s3[0] = 'h' # 불가
# s3.lower() # 수정은 아니라서 추후 따로는 적용 안됨 print 해야함
# s4 = s3.replace('H','h')
# print(s4)

# slef 매개변수: 모든 메소드의 첫 번째 매개변수
# 메소드의 정의에는 사용되지만, 호출에는 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의 된 멤버에 접근할 때 사용
# class person:
#     def say(self):
#         self.name = "허순자"
#         print("Hello")
#     def move(self):
#         print(f"{self.name}님이 도망갔습니다.")
#     def eat(self, food):
#         # self.sleep() # 이거 왜 넣는거지?
#         print(f"{self.name}님이 {food}를 먹었습니다.")
#     def sleep(self):
#         print(f"{self.name}님께서 운명하셨습니다.")
# person1=person() #변수에 적용
# person1.say() # Hello
# person1.move() # 허순자님이 도망갔습니다
# person1.eat("밥") # 허순자님이 밥을 먹었습니다.
# person1.sleep() # 허순자님께서 운명하셨습니다.

# initializer: 초기자: 이니셜라이저, 
# initialize: 초기화: 이니셜라이즈, 만든다, 생성, 시작한다와 유사
# init은 class 에서 멤버 변수들 초기 값을 입력 받을 때 주로 사용
# class person:
#     def __init__(self, name, age, gender, phone) :#매개변수
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         print("initialize")
#     def say_name(self):
#         print(f"""반갑다. 내 이름은{self.name} 나이는 만렙이야 {self.age}
# 성별은 아마 {self.gender}했을듯.. 날 발견하면 {self.phone} """ )
#         # print(self.name, self.age, self.gender, self.phone)
# print("before")
# person2 = person(" 허순자", 99, "퇴화", "국번없이 112")
# print("after")
# person2.say_name()

# #person 클래스에 introduce 메소드를 추가
# # 이름, 나이, 성별을 print 하는 메소드
# class person1:
#     def __init__(self, name, age, job):
#         self.name= name
#         self.age= age
#         self.job = job
#     def say_name(self):
#         print(self.name)
#     def introduce(self):
#         print(f"안녕하세요. 제 이름은 {self.name}.")
#         print(f"{self.job} 이죠.. 나이는 {self.age}살 일지도.. ")
#         # print(self.name, self.age, self.job)
# person3 = person1("코난", 12, "탐정")
# person3.introduce()

# 상속 inheritance
class Animal: # ---------- __init__ 모르겟다
    def __init__(self,name):
        self.name=name # 위 name과 다르지만 값은 같은 객체
        print(f"{self.name}가(이) 생성되었습니다.")
    def say(self) :
        print("")

class Dog(Animal) : # 상속 받은 class 것을 갖다 쓴다.
# 메소드 재정의 : method overriding : 메소드 덮어쓰기
    def say(self):
        print("멍멍")
my_dog= Dog("백구")
my_dog.say()

class Cat(Animal):
    def say(self):
        print("야옹")
my_cat= Cat("나비")
my_cat.say()

# class Student:
#     def __init__(self, name, age, school, grade, gilt):
# # 이름, 나이, 학교, 학년을 멤버 변수로 저장하는 메소드를 만드시오.
#         self.name = name
#         self.age = age
#         self.school = school
#         self.grade = grade
#         self.gilt = gilt
#     def info(self) :
#         print(f"""안녕하십니까? 이번에 {self.school} 에서
# {self.grade}번방으로 이감 온 {self.name} 입니다.
# {self.age}살이고 죄명은 {self.gilt}입니다 """)

# a1=Student("허순자", "29", "청송교도소", "62", "자해공갈")
# a1.info()

# class Student:
#     def __init__(self, name, age, school, grade):
# # 이름, 나이, 학교, 학년을 멤버 변수로 저장하는 메소드를 만드시오.
#         self.name = name
#         self.age = age
#         self.school = school
#         self.grade = grade
#     def introduce(self) :
#         print(f"이름:{self.name} 나이:{self.age} 학교:{self.school} 학년:{self.grade}")

# stu1=Student("허순자",29, "청송교도소", "자해공갈")
# stu2=Student("손흥민",22, "서울대학교", 3)
# stu3=Student("류현진",21, "연세대학교", 4)
# stu_list=[stu1, stu2, stu3]
# for stu in stu_list :
#    stu.introduce()

