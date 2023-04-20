# +　더하기 연산자
# -　빼기 연산자
# *　곱하기 연산자
# /　나누기 연산자
# ** 제곱 연산자
# // 정수 나누기 (몫) 연산자
# %　나머지 연산자

# 이스케이프 문자 (\ 역슬래시 사용)
# \n 줄바꿈
# \r 리턴
# \t 탭
# \" 쌍따옴표
# \' 따옴표

#print ("안녕하세요"+10) error 문자+숫자 불가
#print("hello"[0])
#print("hello"[1])
#print("hello"[2])
#print("hello"[3])
#print("hello"[4])  # 문자열 데이터에서만 사용할 수 있다.
#print("hello"[-1]) # 음수(-)는 뒤에서 부터 인덱싱한다
#print("hello"[1:3]) #[0:]전체, [:5]전체, :앞 뒤 공백은 맨앞 뒤 인덱스
#print("hello"[2:4])
#print("hello"[:3])
#print("hello"[2:])
#print("hello"[100]) error(out of index)
#print(len("hello")) # Len 인덱스 길이 체크

#조건문(IF): 문법이 정해져 있다.
#Python 표준: 탭(1회) OR 스페이스(4회)
"""
if 조건:
    실행하려는 코드
    코드2줄
    코드3줄
코드4줄
if문은 조건이 True(참)일 때만 안쪽 코드 블럭을 실행

if 조건: 
    조건이 참일 때 실행하려는 코드
else:
    아닐 때 실행하려는 코드
else는 조건이 False(거짓)일 때 안쪽 코드 블럭을 실행

if 조건1:
    조건1이 True(참)일 때 실행
elif 조건2:
    조건1은 False, 조건2는 True일때 실행
else:
    조건 1 False 조건2 False일때 실행"""

# 논리 연산자 [bool type 변수에 사용 (True, False)]
    # and   A and B (A, B 모두 True 일때만 True 아니면 False) 
    # or    A or B  (A, B 중 하나라도 True면 True, 둘 다 False면 False)
    # not   not A   (True ↔ False, False ↔ True 바꾼다.)