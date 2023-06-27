# 사진 분석 API photo.py

# AWS의 여러 서비스들을 이용할 수 있는 파이썬 라이브러리(boto3)
# import boto3

# '/review'로 들어온 것을 해당 Resource로 처리
class PhotoReviewResource(Resource):
    def post(self):
        # # 사진이랑 내용이 필수다
        print(request.files) # form의 파일 
        print(request.form) # form의 내용
        # # request.files에 사진이 없다면?
        # if 'photo' not in request.files:
        #     return {'result':'fail', 'error': '사진은 필수'}
        # # request.form에 내용이 없다면?
        # if 'content' not in request.form:
        #     return {'result': 'fail', 'error': '내용은 필수'}
        
        if 'photo' not in request.files or 'content' not in request.form:
            return {'result': 'fail', 'error': '필수항목 확인'}, 400
        
        file = request.files['photo']
        content = request.form['content']
        rating = request.form['rating']
        rating = int(rating) # 타입 변환 같은 것은 바로 다시 변수처리 한다.
        # int로 변환하지 않으면 아래 rating*20이 제대로 작동하지 않는다.
        
        ### S3 저장 코드는 동일 ###
        ## content와 image_url은 DB에 저장한다.
                
        # rating은 0부터 5까지 인데,
        # 이 값을 0~100 사이의 값으로 변경하여 클라이언트에게 보내시오
        rating = rating * 20
        
        return {'rating' : rating}


class PhotoResource(Resource): 

    def detect_labels(self, photo, bucket):

        client=boto3.client('rekognition', 
                            'us-east-1',
                            aws_access_key_id = Config.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key = Config.AWS_SECRET_ACCESS_KEY)

        # Image= 이미지 위치(?), MaxLabels= 최대 정확도 몇개만 보여달라.
        response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
            MaxLabels=10)

        print('Detected labels for ' + photo) 
        print()   

        label_list = []
        # response는 dictionary
        for label in response['Labels']:

            label_list.append(label['Name'])

            print ("Label: " + label['Name'])
            # print ("Confidence: " + str(label['Confidence']))
            # print ("Instances:")
            # for instance in label['Instances']:
            #     print ("  Bounding box")
            #     print ("    Top: " + str(instance['BoundingBox']['Top']))
            #     print ("    Left: " + str(instance['BoundingBox']['Left']))
            #     print ("    Width: " +  str(instance['BoundingBox']['Width']))
            #     print ("    Height: " +  str(instance['BoundingBox']['Height']))
            #     print ("  Confidence: " + str(instance['Confidence']))
            #     print()

            # print ("Parents:")
            # for parent in label['Parents']:
            #     print ("   " + parent['Name'])
            # print ("----------")
            print ()
        return label_list
    

# # search.py
# from flask_restful import Resource # 상속 받을 리소스
# from flask import request

# ## restful api를 코드에서 사용할 때 필요한 라이브러리 ##
# import requests # flask request랑 헷갈리지 말 것.
# from config import Config


class NewsSearchResource(Resource) :

    def get(self) :
        
        # 1. 클라이언트로부터 데이터를 받아온다.(qeury params 의 key 와 value)
        keyword = request.args.get('keyword')
        
        # 2. 네이버의 APi를 호출한다.
        # requests.get() 함수를 사용 하는 이유는?
        # 네이버 뉴스 검색 API의 http 메소드가 GET 이니까!
        # get url은 파라미터는 네이버뉴스 API에 요청URL
        # params 파라미터는 네이버 뉴스 query 파라미터
        response = requests.get('https://openapi.naver.com/v1/search/news.json',
                    params= {'query' : keyword,
                             'display' : 25,
                             'sort' : 'date'} ,
                    headers= { 'X-Naver-Client-Id' : Config.X_NAVER_CLIENT_ID,
                               'X-Naver-Client-Secret' : Config.X_NAVER_CLIENT_SECRET }  )
        
        print(response.json())
        
        # 우리 서버의 api에 맞게 데이터 가공
        items = response.json()['items']

        return {'result' : 'success',
                'count' : len(items) ,
                'items' : items }




    
    
# # serverless.yml

# service: aws-image-openapi-test

# frameworkVersion: '3'

# custom:
#   wsgi:
#     app: app.app

# provider:
#   name: aws
#   runtime: python3.10
# #   region: ap-northeast-2

# functions:
#   api:
#     handler: wsgi_handler.handler
#     events:
#       - httpApi: '*'

# plugins:
#   - serverless-wsgi
#   - serverless-python-requirements


# # requirements.txt
# Flask==1.1.4
# Werkzeug==1.0.1
# markupsafe==2.0.1

# flask-restful
# requests==2.25.0