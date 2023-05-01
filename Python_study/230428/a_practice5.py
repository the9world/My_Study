# 거꾸로 배열해도 같은 단어 또는 문장이 되는
# 회문(palindrome)인지 판별하는 함수를 정의하세요
# 함수 이름 : is_palindrome
# 반환 값 : True 또는 False
# 앞뒤로 같은

# def is_palindrome(input_string) : # 1 번
#     input_string = input_string.replace(" ","") # 문자열 중간에 있는 공백 제거
#     length = len(input_string) # 소주 만병만 주소
#     for i in range(length//2) : # 반씩 검사
#         length-1
#         if input_string[i] != input_string[length -1 - i]: 
#             return False #if 문에 length-1(마지막 index-1)
#     return True
# a = is_palindrome("소주 만병만 주소")
# print(a)


# def is_palindrome(input_string) : # 2 번
#     input_string = input_string.replace(" ","")
#     return input_string == input_string [::-1]
# a= is_palindrome("다시 합창합시다")
# print(a)

# li1 = [1,2,3,4,5]
# li1.reverse() # 리턴이 없는 함수
# print(li1)
# reversed([li1]) # 원본은 그대로 리턴
# print(li1)

# string1 = "안녕하세요"
# string2 = reversed(string1)
# for i in string2 :
#     print(i)
# string3= "".join(string2)
# print(string3)

# 데이터 수집 단계
"""데이터 수집 -> 데이터 분석/처리->
인공지능 모델 학습 -> 인공지능 모델 평가 -> 사용
"""
# http (HyperText Transfer Protocol)
# request(요청) - response(응답,출력)
# client(web browser) - server
# html (HyperText Markup Language)
# 웹사이트를 표현하기 위한 언어
# <html> </html>
# html 파싱

# import requests
# url = "https://www.naver.com/"
# response = requests.get(url) # get 요청 방식, 리퀘스트 보낸 후 응답 받겟다는 뜻
# status = response.status_code # 상태 코드
# html = response.text
# print (status) # 200 (상태 코드)
# print (html) # 구성 코드

# http 상태 코드
# 200 : OK / 요청 성공
# 302 : 리다이렉트 / 페이지로 바로 연결
# 400 : Bad Request / 요청이 잘못 됨
# 401 : Unauthorized / 비인증
# 402 : 이 요청은 결제가 필요함
# 403 : forbidden / 접근 권한 없음
# 404 : not Found / 요청 받은 내용이 없음
# 405 : Method Not Allowed / 접근 방법이 잘못됨
# 500 : Internal Server Error / 서버에러
# 501 : Not Implemented /수행 기능을 서버가 지원안함
# 502 : Bad Gateway / 잘못된 응답

# url 구조 
# 프로토콜://주소:포트번호/경로?쿼리~
# http://naver.com/?~~~~
# 검색어를 쿼리에 넣어서 다시 요청
# 쿼리
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B9%98%ED%82%A8
# 프로토콜 /호스트주소:포트번호/경로 /? 쿼리~ /query = 검색어
# 쿼리 이름 = 값 & 쿼리이름 = 값 & 쿼리이름 값 = 값
# import requests
# keyword ="맥주"
# search_url="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+keyword
# response=requests.get(search_url)
# # print(response.text)
# print(type(response.text))

# BeautifulSoup  ((find 명령어 찾아보기))
# html 파싱(parsing)
# html을 객체 구조화해서 사용
# # html 태그 : <태그이름 속성=속성값>내용</태그이름> / <html> </html>
# # <html><head></head><body></body></html> : html.head : html.body
# from bs4 import BeautifulSoup # html을 객체로 사용할 수 있게 해줌
# html = "<html><body>Hello</body></html>"
# soup = BeautifulSoup(html, "html.parser") # 값을 꼭 넣어야함
# print(soup.body.text) # 파싱 된 상태임 #Hello
# print(soup.html.text)  # html 사이에 있는 것들 뜸
# print(type(soup.body.text)) #class bs4.BeautifulSoup 정의 한 이름

# import requests
# from bs4 import BeautifulSoup
# search_url="https://www.google.com/search?tbm=isch&q="
# keyword = "맥주" # 위와 해당 라인은 검색 요청
# url = search_url + keyword
# response=requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# imgs = soup.find_all('img') 
# import os
# folder_name = "imgs"
# if not os.path.exists(folder_name) :
#     os.mkdir(folder_name)
# for idx, img in enumerate(imgs[1:]) : # 이미지 하나씩 다 주소 열기
#     # print(img['src']) # 주소만 따오기
#     file_name = f"맥주_{idx}.jpg"
#     print(idx, "번째 이미지 저장")
#     file_path = os.path.join(folder_name, file_name)
#     img_response = requests.get(img['src'])
#     img_data = img_response.content
#     with open(file_path, "wb") as f: # wb = bit로 사용
#         f.write(img_data) # 맥주_0.jpg ~ 맥주_idx.jpg 까지 생성

# print(soup.find_all('div')[4])
# imgs = soup.find_all('img', attrs ={'class':'_image _listimage'})
# print(imgs)

# enumerate(번호를 붙인다) /(이터러블 사용) 자동적으로 인덱스하고 포문 돌려서 
# li1 = ["김연아", "류현진", "손흥민"]
# for name in enumerate(li1):
# # for name 사이에 idx 하면 index 따로 나열 가능
#     print(name) # (0, '김연아) (1, '류현진') (2. '손흥민')

# 네이버 IT/과학 뉴스 크롤링
# import requests
# from bs4 import BeautifulSoup
# # html 글자라서 편하게 다룰려고 파싱해주는 것을 사용한다
# url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# # ↙주소에 들어가면 나오는 정보 받아오는 방법
# # headers={"User-Agent": "Mozilla/5.0"} : 크롤링 방지 회피
# response= requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# html = response.text
# soup = BeautifulSoup(html, "html.parser") # 객체화
# div = soup.body.find('div', attrs={'class':'list_body'})
# # attrs={'class':'cluster_text_headline'} # 빈공간 지운거
# headlines = div.find_all('a', attrs={'class':'cluster_text_headline'})
# import os
# folder_name = "crawling_result"
# if not os.path.exists(folder_name) : # 없을 때만 만드는거
#     os.mkdir(folder_name)
# for headline in headlines:
#     print(headline.text.strip())
#     # 과제 : crawling_result 폴더의
#     # headlines.txt 파일에 저장하기
#     with open("crawling_result/headlines.txt", "a", encoding="utf-8") as f:
#         f.write(headline.text.strip())
#         f.write("\n") # error 이유 폴더 못만듬
#     article_response =requests.get(headline['href'])
#     article_soup = BeautifulSoup(article_response.text, "html.parser")
#     article = article_soup.find('div', attrs={"id":"dic_area"})
#     print(article.text)

# for idx, i in enumerate(headline[1:]): #뭔가 error
#     file_name = f"headline_{idx}.txt"
