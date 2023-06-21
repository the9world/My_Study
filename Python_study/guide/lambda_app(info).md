
lambda_app 가상환경 파이썬버전 3.10  
flask, flask-restful, email-validator

### AWS Credentials 만들기
1. IAM 사용자 추가.
   1. 사용자 이름: flask_app_user
   2. 권한옵션 직접정책연결
      - AmazonAPIGatewayAdministrator
      - AmazonRDSDateFullAccess
      - CloudFrontFullAccess
      - IAMFullAccess
      - CloudWatchFullAccess
      - AmzonS3FullAccess
      - AWSCloudFormationFullAccess
      - AWSLambda_FullAccess
2. 생성-> 사용자 정보-> 보안 자격 증명
   - 액세스 키 만들기
   - 로컬코드-> 하단 동의(체크)-> 다음-> 태그 안써도 됨-> 다음
   - 억세스키 생성 됨, csv(필수) 없으면 접근 권한 없음.
3. ServerLess Framework 접속 및 설치
   - Docs-> Framework(Documetation)-> install in first
   - Default Setting install
   - 로그인-> CreateApp