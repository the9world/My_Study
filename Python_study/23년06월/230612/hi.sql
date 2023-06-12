데이터 중복 제거 distinct

정렬하기 위한 order by

페이징(paging)에 사용 되는 limit 와 offset

문자열 검색에 유용한 like 사용법

count, sum, avg, max min 함수 사용법

group by, having 사용법

Sub Query 사용법

MySQL 에서 날짜 데이터를 저장하는 데이터 타입

DATE, TIME, DATETIME, TIMESTAMP
SELECT * FROM mydb.books;

        -- ★ 2023년 06월 09일 ★
        -- 문자열 데이터 다루기
        -- concat 함수를 사용, 문자열 합치는 함수
    -- fname 과 lname 이 분리되어 있는데
    -- 합해서 full_name으로 가져오고 싶다.
select concat(author_fname, author_lname )  as 'full_name' -- as full_name : 합친 칼럼명 지정
from books;  -- concat()Default: 칼럼명+칼럼명
select concat(author_fname," ",author_lname )  as 'full_name' -- ," ", 으로 합친 값 사이에 띄어쓰기 가능
from books; 

    -- '책 제목 : 작가 풀네임'으로 나오도록 concat 사용
select concat(title, ' : ' ,author_fname, ' ' ,author_lname)
from books;

select concat_ws(' ', author_fname, author_lname, title) -- ws는 문자열 사이를 '입력' 으로 연결
from books;

        -- 문자열 데이터의 일부분만 가져오는 함수,
        -- substring 함수
    -- 책 제목을 10글자만 보여주려 한다. 제목 칼럼은 short title로 명명
select substring(title, 1, 10) as 'short title' -- title의 글자수 1부터 10까지 
from books; 

    -- 제목 칼럼의 맨 뒤에서 7번째 글자부터 끝까지 가져오시오
select substr(title, -7)
from books;

        -- ★ 2023년 06월 12일 ★

-- CONCAT 함수는 하나 이상의 문자열을 연결하여 새로운 문자열을 생성합니다.
    -- 주어진 문자열을 순서대로 연결하며, 각 문자열 사이에는 공백이나 구분 문자가 없습니다
-- CONCAT_WS 함수의 WS는 'With Separator'를 의미.
    -- 구분자를 지정할 수 있음, concat_ws('입력! ', 문자1, 문자2, 문자3) : 문자1입력! 문자2입력! 문자3
-- SUBSTRING 함수는 문자열의 일부분을 추출합니다.
    -- 주어진 문자열에서 시작 위치(index)와 길이를 지정하여 추출할 부분을 선택할 수 있습니다.

        -- 문자열의 내용을 바꾸는 replace 함수
    -- 책 제목에 The가 있으면, 제거하고 싶다.
select replace(title, 'The', ''), pages, author_fname
from books;

        -- 문자열의 순서를 역순으로 바꿔주는 reverse 함수
    -- 작가 author_lname을 역순으로 가져오시오.
select reverse(author_lname)
from books;

    -- 책 제목을 맨 앞부터 10글자만 가져오고,
    -- 뒷부분은 ...을 붙여서 가져오시오.
select concat( substring(title, 1, 10), '...' )
from books;

    -- 문자열의 갯수(길이)를 구하는 char_length 함수
    -- 책 제목의 길이를 구하시오.
select char_length(title)
from books;

    -- 원래의 테이블에 책 제목의 길이를 구한 칼럼까지 함께 보여달라
select * , char_length(title) as length
from books;
    -- 대소문자를 처리하는 함수 upper(), lower()
    -- 작가 이름 author_fname 을, 대문자로 바꾸시오.
select upper(athor_fname)
from books;

    -- 작가 이름 author_fname을 대문자와 소문자 둘 다 보여주세요.
select upper(author_fname) as uppuer, lower(author_fname) as lower
from books;

        -- ★ ★ 실습1 ★ ★
    -- 타이틀의 공백을 "->"으로 바꿔서 나오도록 조회
select replace(title, ' ', '->')as 'title'
from books;

    -- index 문제
select author_lname as 'forwards',
        reverse(author_lname) 'backwards'
from books;

    -- 다음처럼 이름을 합치되, 대문자로 합쳐서 조회
select upper(concat(author_fname, ' ', author_lname)) 'full name in caps'
from books;

    -- 다음처럼 타이틀 칼럼과 연도 칼럼을 합치되,
    -- was released in이 들어가도록 합쳐서 조회하시오.
select concat (title,' was released in ', released_year) as 'blurd'
-- select concat_ws(' ', title, 'was released in', released_year) as blurd
from books;

    -- 다음처럼 타이틀과, 타이틀에 적힌 글자의 개수가 나오도록 조회
select title, concat(char_length(title)) as 'character count'
from books;

    -- 숏타이틀은 앞에서 10글자까지만 나오고, 뒤에 "..." 이 나오도록 만들고,
    -- author는 이름 두 개 칼럼을 합치고, quantity는 원래 숫자에 in stock이 붙도록 조회
select concat(substring(title, 1,10), '...') as 'short title',
concat(author_lname,',', author_fname) 'author',
concat_ws('   ', stock_quantity, 'in stock') as 'quantity'
from books;

            -- SQL 폴더의 Inser_into_book2.SQL 실행
            -- books 테이블에 19개의 데이터가 있다.
        -- 데이터를 유니크하게 가져오는 키워드(함수X) distinct(디스팅트)
        -- author_lname은 카테고리 컬 데이터다(중복 데이터가 있음)
    -- 이 칼럼의 데이터를 유니크하게 가져오자.
select distinct author_lname
from books; 

    -- full name 으로 중복을 제거하여 유니크하게 이름 확인해 보자.
select distinct concat_ws('  ', author_fname, author_lname) as 'FullName Unique'
from books;

        -- 데이터를 정렬하는 방법 : order by keyword(오더 바이 키워드)
        -- order by keyword의 ★위치★ !!! ★위치★가 중요하다..!
    -- author_lname으로 정렬
select *
from books
order by author_lname;

    -- full name으로 내림차순 정렬
select *, concat(author_fname, ' ', author_lname) as 'full_name_sort'
from books
order by full_name_sort asc;
    -- full name으로 오름차순 정렬
select *, concat(author_fname, ' ', author_lname) as 'full name sort'
from books
order by `full name sort` desc;
        -- 공백이 있는 칼럼 명은 ("")따옴표(double quotes?) 대신
        -- (``)백틱(backtick)을 사용, (~)물결은 틸트(tilde)
SELECT *
FROM (
  SELECT *, CONCAT(author_fname, ' ', author_lname) AS 'full name sort'
  FROM books
) AS subquery
ORDER BY subquery.`full name sort` DESC;

    -- 출간년도 내림차순으로 정렬하여, 책 제목, 출간 연도, 페이지 수를 가져오시오.
select title, released_year, pages
from books
order by released_year desc;

    -- author_lname으로 오름차순 정렬하되, lname이 같으면, (bas jon, cas jon)
    -- author_fname 내림차순으로 정렬  (cas jon, bas jon)
select *
from books
order by author_lname asc , author_fname desc;

    -- 데이터를 끊어서 가져오는 방법 limit 키워드와 (offset)
    -- books 테이블의 데이터를, 5개만 가져오시오.
select *
from books
limit 5; -- 5; = 0,5;    
-- 첫 번째 적는 숫자: 오프셋(offset) = 어디서부터 가져올까? 위치 : 인덱스
-- 두 번째 적는 숫자: 개수 : 몇 개 가져올까?
select *
from books
limit 5, 5; -- 6부터 5개(6~10), 5 포함 5개 보려면 4, 5(5~9)
select *
from books
limit 10, 5; -- 11부터 5개(11~15), 10 포함 5개를 보려면 9, 5(10~14)

    -- 출간 연도 내림차순으로 정렬하여,
    -- 처음부터 7개의 데이터를 가져오시오.
select *
from books
order by released_year desc
limit 0, 7;

        -- 문자열 안에 원하는 문자열이 들어 있는지 검색 : like keyword
    -- 책 제목에 the가 들어있는 데이터를 가져오시오.
select *
from books
where title like '%the%'; -- %문자% 이렇게 안 하면 "where=" 랑 다를 게 없음
    -- the로 끝나는 데이터를 가져오시오
select *
from books
where title like '%the';
-- %the% 앞 %는 앞에 뭐가오든 the로 끝나는 것, 뒤 %는 뒤에 뭐가오든 the로 시작하는 것 
-- %the%는 앞뒤 뭐든 포함

    --  stock_quantity 의 숫자가 두 자리인 데이터를 가져오시오.
select *
from books
where stock_quantity like '__'; -- _ 1개=1자리, 2개=2자리인 것들 가져오기


        -- ★ ★ 실습2 ★ ★
    -- 제목에 stires가 포함된 데이터를 제목만 조회
select title
from books
where title like "%stories%";
    -- 페이지 수가 가장 긴 책을 찾아서, 제목과 페이지 수를 조회
select title, pages
from books
order by pages desc
limit 1;
    -- 가장 최근에 발간된 책 3권을 찾아서 책의 제목과 발간 연도를 조회하되
    -- 다음처럼 (-)하이픈을 붙여서 조회 (칼럼 명은 summary)
select concat_ws(' - ', title, released_year) as 'summary'
from books
order by released_year desc
limit 3;
    -- author_lname에 ("")공백이 들어있는 사람의 책 제목과 author_lname을 조회
select title, author_lname
from books
where author_lname like "% %";
    -- 가장 stock_quantity가 적은 책 3권의 title, year, stock_quantity를 조회
select title, released_year, stock_quantity
from books
order by stock_quantity asc, released_year desc
limit 3;
    -- author_lname과 title로 정렬 후, title과 author_lname을 조회
select title, author_lname
from books
order by author_lname, title;
    -- author_lname으로 정렬하되, "My favorite author is"를 붙여서 조회
select upper(concat('My favorite author is ',author_fname,' ',author_lname, "!" )) as yell
from books
order by author_lname asc;

        -- 개수를 세는 함수 count 함수
        -- books 테이블의 데이터 개수는??
select count(*)
from books;

    -- author_lname은 중복데이터가 있다.
    -- 중복을 제거한 유니크한 데이터의 개수는?
select count(distinct author_lname)
from books;

    -- 책 제목에 the 가 들어간 책은 몇 권입니까?
select count(*)
from books
where title like '%the%';

    -- 집계하는 방법 : ~별로 묶어서... group by keyword
    -- author_lname 별로, 몇 권의 책을 썼는지,
    -- author_lname과 책의 권 수를 보여주세요.
select concat(author_lname,' ',author_fname) "full_name", count(*) 'count'
from books
group by author_lname;

select author_fname 'full_name', count(*) 'count'
from books
group by author_fname;

    -- 연도별로 각각 몇 권의 책이 출간되었는지
    -- 연도와 출간 수를 보여주세요.
select released_year '출간연도', count(*) 'count'
from books
group by released_year
order by released_year desc;

    -- 최댓값을 구하는 함수 max()
    -- 페이지 수가 가장 많은 책은 몇 페이지입니까?
select max(pages)
from books;    

    -- 최솟값을 구하는 함수 min()
    -- 출간 연도가 가장 빠른 책은 몇 년도인가?
select min(released_year)
from books;

    -- 페이지 수의 최대 값과 최소 값을 가져오시오.
select min(pages), max(pages)
from books;

     -- 페이지 수가 가장 긴 책의 제목과 페이지 수를 보여주세요.
select title,pages -- 잘못된 SQL 문
from books
where pages = max(pages); 
-- 방법1 : 정렬 후 limit
select title, pages
from books
order by pages desc
limit 1;
-- 방법2 : max 값 구해서, SubQuery(서브쿼리) 하는 방법
select max(pages)
from books;

select title, pages
from books
where pages = ( select max(pages) from books); -- subquery(서브쿼리)

    -- stock_quantity가 가장 적은 책의
    -- 책 이름과 작가명을 보여주세요
select min(stock_quantity)
from books;

select title, author_fname, author_lname
from books
where stock_quantity = (select min(stock_quantity) from books);

    -- 각 작가의 full name 별로 해당 작가의 최초 책 발간 연도는 언제입니까?
    -- 작가의 full name과 발간 연도를 보여주세요.
select min(released_year)
from books;

select concat(author_fname, author_lname), min(released_year)
from books;

    -- 각 작가(풀네임)별 자신이 쓴 책 중 가장 긴 책의 페이지 수를 보여주세요
select max(pages), author_fname, author_lname
from books
group by author_fname, author_lname;

    -- 값을 모두 더 해주는 함수 sum()함수
    -- books 테이블의 모든 책의 페이지 수를 다 더 하면 몇?
select sum(pages)
from books;

    -- 평균 구하는 함수 avg() = python mean()
    -- books 테이블의 페이지 수 평균을 구하면?
select avg(pages)
from books;

    -- 연도 별로 stock_quantity의 평균을 구하시오.
select released_year, avg(stock_quantity)
from books;

select released_year, avg(stock_quantity) 
from books
group by released_year
order by released_year desc;

    -- 출간 연도가 2017년도인 데이터를 가져오시오.
select *
from books
where released_year = 2017;
    -- 출간 연도가 2017년도가 아닌 데이터를 가져오시오.
select *
from books
where released_year != 2017;

    -- 작가의 author_lname이 'Harris'가 아닌 데이터를 가져오되,
    -- 책 제목과 페이지 수만 가져오시오.
select title, pages
from books
where author_lname != 'Harris';

    -- 책 제목에 W가 포함된 책을 찾으시오.
select *
from books
where title like '%W%';
    -- 책 제목에 W가 포함되지 않은 책을 찾으시오.
select *
from books
where title not like "%W%";

    -- 책의 재고가 100 이상인 데이터에서, 책 제목과 재고만 보여주세요.
select title, stock_quantity
from books
where stock_quantity >= 100;

    -- 출간 연도가 2000년 이상인 책에 대해서
    -- 최신 책으로 정렬해서, 제목과 연도를 보여주세요.
select title, released_year
from books
where released_year >= 2000
order by released_year desc;

    -- 출간 연도가 1990년에서 2015년 사이의 책 데이터를 가져오시오.
select *
from books
where released_year>=1990 and released_year <= 2015;
select *
from books
where released_year between 1990 and 2015 ;
-- BETWEEN start_value AND end_value;
    -- 책 재고가 100보다 크거나 30보다 작은 책들만 가져오시오.
select *
from books
where stock_quantity > 100 or stock_quantity < 30;

    -- author_lname이 Eggers 이거나
    -- 출간 연도가 2010년 이상인 데이터를 가져오세요.
select *
from books
where author_lname = 'Eggers' or released_year >=2010;

    -- 연도별 stock_quantity의 평균값이 70보다 큰 책들의
    -- 연도와 평균값을 보여주세요
select released_year, avg(stock_quantity) 'avg_stock'
from books
group by released_year having avg_stock >= 70;
-- GroupBy로 생긴 데이터에서 조건을 넣으려면 "group by 칼럼 having 조건"

    -- 출간 연도가 2000년 이상인 데이터에서
    -- 연도별 stock_quantity의 평균값이 70보다 큰 책들의
    -- 연도와 평균값을 오름차순으로 보여주세요.
select released_year, avg(stock_quantity) 'avg_stock' -- 1번 방법
from books
group by released_year having released_year >= 2000 and avg_stock >=70
order by released_year asc;
select released_year, avg(stock_quantity) 'avg_stock' -- 2번 방법
from books
where released_year >=2000
group by released_year having avg_stock>=70;

select * from books;