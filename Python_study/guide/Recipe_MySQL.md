## 가상환경 생성 (1) Python( VS CODE )
- 가상환경 만들기 (recipe-server)
  - 서버의 환경과 동일하게  
        AWS Lambda를 이용한다. Python 3.10 version  
        (base는 중요X base에서 안함)
  - $conda create -n lambda_app(가상환경이름) python==3.10
  - $conda activate lambda_app(가상환경이름)
  - 인터프리터(interpreter) 우측하단 : lambda_app 선택
  - $pip install flask flask-restful : FrameWalk "flask" 설치  
    - 프레임워크(framewallk)란 연결 통로?몰루
---


## 가상환경 생성 (2) MySQL(WorkBench)
```sql
use mysql; -- 우리가 만든 DB 말고 MySQL의 DB?

create user 'recipe_db_user'@'%' identified by '3885';  -- recipe에만 접속?
grant ALL privileges on recipe_db.* to 'recipe_db_user'@'%';
-- grant ALL privileges on: 모든 권한 부여, 

-- 테스트 실행. => MySQL WorkBench
```
- MySQL WorkBench home으로 가서 Connections 생성(+)  
  1. Connection NAME : recipe_DB (위 코드와 같음)  
  2. Host_Name: AWS rds 주소 입력  
      또는 my_db Connection 의 Host_name 복사  
  3. UserName은 코드에서 입력한 "recipe_db_user"
  4. Test 실행 - Password는 identified by '3885'에서 입력한 '3885'
---

 ## Restful API (Representational State Transfer)
- 통신을 위한 REST 구성
  - 자원(Resource): http://service.com/users 라는 형태의 URI
      - URI= 식별자, URL=식별자+위치
      - URI(URL) 구성 명칭  
```
http://opentutorials.org:3000/main?id=HTML&page=12  
protocol://host(domain):port/path?query string  
```

  - 행위(verb): HTTP Method
    - HTTP Methods 와 Message Format

|HTTP Moethods|설명|
|--|--|
|GET|Create: 데이터 생성: 가져온다.|
|POST|Read: 데이터 조회: 집어넣음|
|PUT|Update: 데이터 수정: 업데이트|
|DELETE|Delete: 데이터 삭제|
---

## API 명세서 : PostMan
- PostMan은 API 를 만들고 Test할 수 있는 앱
- PostMan download(64bit) & install
- 레시피 등록 API
  - POST: http://127.0.0.1:5000/recipes
- Request 요청
  - name, description, num_of_servings, cook_time directions, is_publish
- Response 응답
 result: success / fail
- Body- Raw- Text- JSON : dictionary, **"쌍따옴표"** 만 사용한다.
- 클라이언트(PostMan)에게 요청 받고  
요청 받은 URL이 '내 /path'가 맞다면  
/path 경로로 넘어와서 앞에 RecipeListResource 실행
---

- 저장된 레시피 리스트 가져오는 API
    - GET http://127.0.0.1:5000/recipes
      - 요청 데이터 없음.
    - 응답 데이터
```JSON
{"result": "Success"
 "count": 3,
 "itmes": [ {id: 1, name:.. , des...}, {}, {} ] }
```

## Python에서 MySQL 연동
- $pip install mysql-connector-python (import mysql.connector)
- 최상단 경로에 config.py 생성
- 프라이빗: .gitignoer- config.py : 이 파일은 빼고 올려라

### 특정 레시피 1개 데이터 가져오는 API
- GET http://127.0.0.1:5000/recipe/2 (2= recipe ID)  
- **GET 메소드는 Body에 절대로 데이터를 보내지 않는다.**
- **POST 메소드가 Body에 데이터를 보낸다.**
- 응답 : 1개의 레시피 데이터 (JSON?)

- 없는 아이디를 넣으면 에러뜬다 조건문으로 바꿔준다

JSON을 TEXT로 반환하는 프로그램
JSON editor Online