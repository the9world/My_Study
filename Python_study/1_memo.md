(파이썬 map 함수 사용법)  
https://blockdmask.tistory.com/531  
예측 : regression : 예측(숫자) : A의 자산 추측 등등  
분류 : classification : 지도학습 : 특정된 것에 대한 분류  
군집 : clustering : 비지도학습 : 특정된 것이 없음? 비슷한 그룹끼리 묶음

예측, 분류는 슈퍼바이저러닝 ( 예측할 것에 대한 정보가 있어야함 )  

clustering  군집 :  
비슷한 성향의 사람끼리 묶어본다.  
컴퓨터에게 (?) 그룹씩 묶어 달라 요청할 경우  
데이터(점)간의 좌표(점)위치 거리가 가까운 것 끼리 묶음  
검증이 불가함 : 언슈퍼바이저러닝 : 그루핑(그룹끼리 묶음) (한 번 더 검색)  

아이디 성별 주문메뉴 주문시간 주문수량  
그룹 갯수를 입력하면 그루핑은 컴퓨터가 직접 함(수직이등분선):  
컴퓨터가 랜덤으로 중심점을 잡음, 임의로 그룹 별 평균을 구함?,  
중심점과 평균의 거리를 구함, 수직이등분선 만들고 그룹을 나눔  
이렇게 계속 작동하다가 완전하게 그룹을 나눔(?) (한 번 더 검색)   

중심에서 부터 데이터가 가까울수록 응집력이 높음(?)  
중심에서 부터 데이터의 거리가 중요 (중심점은 랜덤)  
중심점(데이터 점이 아님)과 점사이 거리구함  그 거리를 수직이등분선 거리를 찾음  
(중심점 랜덤문제를 해결한게 K-means++)  
사용자는 그룹을 몇개로 할지 정하는 것이 가장 중요  
wcss = 중심에서 그룹란의 거리가 작은 것  
효율적인 갯수는 엘보우에 있는 수:The Elbow Method(?)  

표준화 = StandardScaler  
정규화 = MinMaxScaler  


## K-means :
1. CSV 파일(데이터)을 넣어주면
2. 데이터를 그루핑(Clustering) 해주는 앱
3. Jupyter NoteBook을 사용하여 분석
4. K-means 예제를 풀어봅시다.

## 05.30 이후 강의 예정
- 데이터 수집 사이트 보시고  
- 기획해서 분석하고(인공지능이 불가한 것은 분석까지만)  
- 인공지능 개발이 가능하다면, 인공지능 만들고  
- 앱 대시보드 화면 / 화면 기획 / 개발  
- 06월 08일 ~ 06월 09일 발표 예정 (진행 상황에 따라 앞당겨 진행할 수 있음)

https://everyday-deeplearning.tistory.com/entry/%ED%98%84%EC%97%85%EC%97%90%EC%84%9C-%EB%A7%8E%EC%9D%B4-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-Python-%EB%AA%A8%EB%93%88-Pandas

https://bioinformaticsandme.tistory.com/70

https://sosoeasy.tistory.com/385

https://snepbnt.tistory.com/32

mae(mean asolute:평균 절대 오차)  
mse(mean squared:평균 제곱 오차)  
깃허브 소스코드에 관한 검색