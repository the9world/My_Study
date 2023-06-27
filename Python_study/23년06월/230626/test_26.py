# # 사진 올리는 API

# from flask_restful import Resource # 상속 받을 리소스
# from flask import request 
# from datetime import datetime
# from config import Config


class Config:
    # 억세스아이디와 키를 보안상 변수처리
    AWS_ACCESS_KEY_ID = 'aws키아이디'
    AWS_SECRET_ACCESS_KEY = 'aws엑세스키'
    
    # 버킷이름을 보안상 변수처리
    S3_BUCKET = '버킷이름'
    S3_BASE_URL = 'https://'+S3_BUCKET+'.s3.amazonaws.com/'
    
    # 네이버 클라이언트 ID 및 SECRET 보안상 변수처리
    X_NAVER_CLIENT_ID = '네이버클라이언트ID'
    X_NAVER_CLIENT_SECRET = '네이버클라이언트SECRET'
    
class PhotoResource(Resource): 
    def post(self): 
        # request.args는 물음표로 온 것을 처리..(?)
        print(request.files) # file로 들어온 것을 처리(body: Value의 파일)
        
        # 사진이 필수인 경우의 코드(사진이 없는 경우)
        if 'photo' not in request.files :
            return {'result':'fail', 'error':'파일 없음'}, 400
        
        # 유저가 올린 파일을 변수로 만든다.
        file = request.files['photo']
        
        # 파일명을 유니크하게 만들어준다. (datetime)
        current_time = datetime.now() # 현재 시간 가져오기
        print(current_time.isoformat().replace(':','_').replace(':','_')+'.jpg') 
        # 문자열로 변환 및 파일명
        new_filename = current_time.isoformat().replace(':','_').replace('.','_')+'.jpg'
        
        try:
            # 새로운 파일명으로, S3에 파일 업로드
            # 버킷에 접근할 권한 accessKey(csv파일) 보안상 config에서 관리
            # Config 클래스의 해당 키가 있는 변수를 호출한다.
            s3 = boto3.client('s3',
                        aws_access_key_id = Config.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = Config.AWS_SECRET_ACCESS_KEY)
            
            # 파일을 업로드한다. 1. 파일명 2. 버킷이름(AWS S3)도 보안상 Config 변수 처리
            # 3. 업로드할 때 파일이름 4. 액세스제어는 퍼블릭으로 읽고, 저장타입은 JPG
            s3.upload_fileobj(file,
                              Config.S3_BUCKET,
                              new_filename,
                              ExtraArgs={'ACL':'public-read', 'ContentType':'image/jpeg'})
            
                    # Exception은 파이썬에서 공용으로 사용하는 Error
        except Exception as e:
            print(str(e))
            return {'result':'fail', 'error':str(e)}, 500
        
        # 사진이 저장 되었으면 저장한 사진의 URL이 필요하다.
        # DB에 저장해야 한다.
        
        # URL 주소는 = 버킷명.s3주소/우리가 만든 파일명
        # file_usl= Config.S3_BUCKET+'.s3.amazonaws.com/'+ new_filename
        # 위 처럼하면 지저분(?) 해보여서 Config에 S3_BASE_URL로 변수 처리
        file_url= Config.S3_BASE_URL + new_filename
        
        ### Object Detection 한다.
        # https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html
        ## 권한이 필요하다 -> IAM 권한추가 rekognition FullAccess
        ## class 안에 함수(def) 호출은 class 밖에 있어야 한다.
        
        # 첫 번째 파라미터는 파일명, 두번째 파라미터는 버킷명
        label_list= self.detect_labels(new_filename, Config.S3_BUCKET)
        
        
        # 잘 되었으면, 클라이언트에 데이터를 응답한다. 
        return {'result' : 'success', 'file_url':file_url, 
                'count' : len(label_list), 
                'items' : label_list}