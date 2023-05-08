weather = input("비가 오나요?:") #weather 변수에 값 할당
# print("비가 오나요?", weather == "비") #비가 오나요? True 출력
if weather in "비" or "옴"  : #(조건문, 조건식) "비"와 같으면 조건식이 True이므로 안쪽 코드 출력 
    print("우산을 가져간다")
elif "맑" in weather:
    print("날씨가 좋다.") #여기서 수행이 끝나면 else는 수행하지 않음.
else: # 조건식이 False이면 실행
    print("우산을 가져가지 않는다.")