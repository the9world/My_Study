# dictionary(딕셔너리, 사전) 자료형  #이름표를 가지고 데이터를 찾아서 그와 관련된 값을 저장
# key-value 형태 #[대괄호]{중괄호}(괄호) 큰 괄호가 작은 괄호에 들어갈 수 없음
# key : value (ex "나이":18) 쌍<->세트 
# key 값으로 접근 #규칙에 따라 엮어 놓는
# 장점 정보 열람이 용이함,
# person={"이름":"한구긴",
#  "나이":18,
#  "점수": {"영어":80, "국어":90, "수학":100},
# "ㅎㅎ":1}
# print(person["나이"]) # 18 
# print(person["점수"]["수학"]) # 100

# dict_1={1: 'a'} # dictionary 형태 
# dict_1['b']=2  #'b':2 key-value 쌍 추가, list와 다르게 ?
# dict_1[1] = 'c'
# del dict_1[1] #del 해당 데이터를 삭제한다
# print(dict_1)

# dict_2 = {1: 'a', 2:'b', 3: 'c'} # key(앞) 1,2,3  # value(뒤?) a,b,c 

# # keys()
# # 딕셔너리에서 key 값만 리스트 형태로 돌려준다.
# dict_keys = dict_2.keys() # dict_keys([1, 2, 3])
# print(dict_keys)
# # vlues()
# # 딕셔너리에서 value 값만 리스트 형태로 돌려준다
# dict_values = dict_2.values() # dict_values(['a', 'b', 'c'])
# print(dict_values)
# # items()
# # 딕셔너리에서 key-value 쌍을 튜플(묶음?)로 묶은 값을 리스트 형태로 돌려준다.
# dict_items = dict_2.items() # dict_items([(1, 'a'), (2, 'b'), (3, 'c')])
# print(dict_items)

# get()
# key에 대응되는 value를 돌려준다.(출력?) # None 해당 데이터가 없다는 뜻 (0개 있다는 뜻)
# key값이 존재하지 않으면 None을 돌려준다.(출력?) # 없는 것 때문에 error 안나게 방지하는 함수
# dict_2={"나이" : 0}
# dict_2["나이"] # 얘는 error 출력
# print(dict_2.get("나이")) # 얘는 error 대신 None(없다, 0) 이라 출력
# print(dict_2.get("나이", "나이 불명")) # 나이가 있으면 키값 "나이"의 밸류값을 출력
# 없으면 None("나이 불명") 출력 

# clear()
# dictionary 안에 모든 것을 다 삭제하는 함수 # remove와 다르게 key+value 모두 삭제함
# dict_2.clear()
# print(dict_2)