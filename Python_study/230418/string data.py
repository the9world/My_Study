# print ("안녕하세요."+"반갑습니다.")
# print ("안녕하세요"*5)
# 문자열(String) "", ''로 감싸서 사용
#     1개 이상의 문자가 나열 된 상태
#     HELLO WORLD (공백도 문자)
#     +연결, *반복 (숫자 연산자와 다른 의미 →추상화)
 
# 연산자
#    (ex. 1+2= 1,2 피연산자, + 연산자 OR 산술연산자)
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
print("hello"[-4])

print("가나다라마바사"[0:4])