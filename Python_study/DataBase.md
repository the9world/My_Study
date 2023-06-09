# DATABASE
## RDBMS
- Oracle
- DB2  
- MySQL(MariaDB, 오픈소스, 가장 대중적)
1. 중요한 정보를 저장
2. 일처리 여러 단계 중에 잘못되면  
다시 초기상태로 돌아감(원상복구)
3. 데이터 저장공간이 정해져 있음

## NoSQL
- SNS 서비스 발달로 데이터양이 무제한인 것을 처리  
- 저장공간이 무한이고 분산처리
- 데이터 원상복구도 가능하지만,  
폭발적으로 늘어나는 데이터를 분산처리하는데 효율적  


### RDS 순서
1. AWS - 서비스 - 데이터베이스 - RDS - 서울 리젼 지정 - 
데이터베이스 생성: 
엔진옵션: 엔진유형
Aurora DB: 유료 회사에서 많이 사용
MySQL 프리티어 선택

엔진버전 : 자동 최신??
템플릿 : "프리티어"
가용성 및 내구성 : 배포옵션 : 프리티어는 불가
설정
DB 인스턴스 식별자 : 대문자를 입력해도 되지만
소문자로 저장됨
자격증명설정: 마스터사용자 이름: admin 두셈(토큰같은거 나중에 꼭 필요)
마스터 암호 : 8자 이상 ASCII문자

인스턴스구성
  컴터사양임 냅두셈 어차피 프리티어 못바꿈

스토리지
 스토리지 유형: ssd, 할당스토리지:20gb

연결
 컴퓨팅리소스 ec2연결하냐 안하냐, 일단 no

퍼블릭억세스
예: 이게 오픈임 이거 ㄱㄱ , 아니오:시크릿

추가구성
포트:3306:디폴트 우린 이거 ㄱ(회사에선 다 바꿈)

대충 생성

- MySQL WorkBench 설정
    1. Dwonload MySQL WorkBench
        - 자신의 OS 환경으로 Download
        - Login 없이 "No thanks, just start my download."  
    2. my sql bench 설치 64비트
설치후  
       - MySQL Connections "+" 클릭  
       - Connection Name: rds에서 만든이름: mydb  
       - Host네임: RDS-db인스턴스-db식별자이름클릭-  
        연결&보안- 엔드포인트복사  
       - Username : RDS에서 만든 토큰같은거 admin
       - Password : 어드민 만들때 만든 마스터암호
       - Test Click Suecces: OK 눌러서 connection 생성  
       - Test Erorr: RDS- 연결&보안- vpc 보안그룹-  
        인바운드 규칙- 인바운드규칙편집- 규칙추가-  
        유형mysql/aurora(사용자지정TCP해도 됨) 	 
        소스:애니웨어-규칙저장


워크벤치 설치 에러:https://musclebear.tistory.com/115  
교수님 설치 방법: https://docs.google.com/presentation/d/12Xm89yzn-Lk6eacTjSn59hXrB28Ip4waDyPfe29jXDE/edit#slide=id.p


DataFrame(데이터프레임)을 데이터베이스에선 Tables(테이블)    
테이블은 인덱스가 없음, 직접 컬럼으로 생성해야함.  
데이터베이스는 많은 테이블들로 이루어져 있음.  
관계형 데이터베이스:RDBMS

  - 테이블설계 : 테이블만든다  
    - 테이블 설계는 어렵지만, 커리는 쉽다?  

|**Data Types**|
|--|
|**Numeric Type**||
| - **int**, smallint, **tinyint**, mediumint, bigint, decimal, numeric, float, **double**, bit |
|**String Type**||
| - char, **varchar**, binary, varbinary, blob, tinyblob, |
|**Data Tyes**||
| - **timestemp**|

- 실제로 작업할 때 : 데이터베이스 : 스키마  
  - 프로젝트 단위로 만든다.

My_SQL 실행 :

mysql workbench 실행후
name: mydb
Charset/Collation : utf-8, utf8_unicode_ci

schemas mydb tables 
column name, datatype (100)100까지만  

텍스트에 - 하이픈하고 나오면 컬럼  
SQL file : ( "--","#" 주석)

- id 컬럼은 인덱스 같은 고유 입력
  - PK : Primary Key : 가장 중요한 키
  - NN : Not Null : 결측치가 될 수 없다.
  - UN : Unsigned : 음수가 없다. ( 1 ~ )
  - AI : Auto increment : 자동 증가  
    해당 컬럼 밸류가 자동증가
- 코드의 *의 의미는 이 테이블의 모든 컬럼!
PK - Primary key, 중복이나 빈값(NULL)이 들어올 수 없음

NN - Not Null(빈값) 못들어옴

UQ - Unique, 중복 값을 넣을 수 없음

B - 데이터를 이진 문자열로 저장함(010101 같은)

UN - Unsigned data type (- 범위 삭제)

INT, DOUBLE 등의 경우 UN을 사용해 주면 -값 +값 이던 범위가

- 값은 없어지고 +값만 2배로 늘어남

ZF - Zero Filled 컬럼 크기보다 작은 값을 넣었을 경우 0으로 채운 뒤 삽입시킴

AI - Insert 시마다 값 1씩 늘어남

G - 다른 열을 기반으로 한 수식으로 생성된 값

Default/Expression - 기본값, 기본값에 수식 설정



```SQL
-- cats 테이블에 데이터 넣기 ("--" 주석)

use.mydb -- 이 db를 main(?)으로 잡아줌

insert into mydb.cats -- inser info : 테이블에 넣음 : DB 저장에 됨,
( name, age) -- name하고 age 컬럼에 집어 넣어라.
values
( '냥이' , 7 ); -- 밸류값은 컬럼과 일치되어야함. 
-- 데이터 베이스에 데이터를 넣고 빼고 삭제할 수 있는
-- 테이블 작업하기전에, 데이터베이스를 알려주고 작업하는 방법
-- SQL 문은 항상 끝은 ;(세미콜론)
use mydb; -- 내가 작성하는 것들은 mydb로 가기때메 mydb.cats로 안해도 됨

insert into cats
( age, name )
values
( 3, 'victorya' ) ;
-- 참고만
create table cats3
( id int not null auto_increment, 
   name varchar(20), 
   breed varchar(20),
   age int,
   primary key (id)
);

insert into cats3
(name, breed, age)
values
('Ringo', 'Tabby', 4);


-- 한 번의 SQL 문으로, 데이터 여러개 인서트

insert into cats
(name, age)
values
('고양이', 10), ('캣츠', 6), ('Sadie', 4) ; -- 엔터치고 여러줄로 해도 됨.
```

```sql
insert into shirts (article, color, shirt_size, last_worn)
values ('polo shirt', 'Khaki', 'S', 96);

SELECT * FROM shirts_db.shirts;

-- shirts.sql 파일을 실행하여, 데이터를 insert
select * from shirts;
-- 모든 셔츠를 조회하되, aticle & color만
select article, color from shirts ;

-- M 사이즈의 셔츠에서 shirt_id만 빼고 전체 칼럼을 가져오시오
select article, color, shirt_size, last_worn from shirts where shirt_size = 'M';
 
-- polo 셔츠의 사이즈를 L로 바꾸세요
update shirts set shirt_size = 'L' where article = 'polo shirt';

-- last worn 이 15인 데이터를 0으로 바꾸세요
update shirts set last_worn = 0 where last_worn = 15;

-- blue 셔츠의 사이즈는 XS로 컬러는 off white로 변경하세요
update shirts set shirt_size = 'XS', color ='off white' where color = 'blue';

-- 입은지(last_worn) 200일이 지난 셔츠는 삭제하세요
delete from shirts where last_worn > 200;

-- 유행이 지난 tank top는 삭제합니다.
delete from shirts where article = 'tank top';

-- 셔츠 테이블의 모든 데이터를 삭제하세요
-- delete from shirts; 
```
- CRUD: Create, Read, Update, Delete
  - insert
  - select
  - update
  - delete

id를 지정한 숫자부터 시작하고 싶으면 table- option- auto increment 수정