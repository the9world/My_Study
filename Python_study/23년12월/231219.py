

# 입력된 텍스트 및 파일을 업로드한다.
class PhotoResource(Resource) :
    
    def post(self):
        # request.args는 물음표로 들어온 것을 처리 (body: Value의 파일)
        print(request.files) 