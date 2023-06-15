## PostMan
- API 를 만들고 Test할 수 있는 앱
- PostMan download(64bit) & install

- 가상환경 만들기 (recipe-server)
  - 서버의 환경과 동일하게  
        AWS Lambda를 이용한다. Python 3.10 version  
        (base는 중요X base에서 안함)
  - $conda create -n 가상환경이름 python==3.10
  - $conda activate lambda_app
  - 인터프리터(interpreter) 우측하단 : lambda_app 선택
  - 