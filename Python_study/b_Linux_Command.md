### Linux 명령어
    mkdir 폴더명 (디렉토리 생성)  
    mkdir -p 상위폴더/하위폴더 (폴더를 만들 때 상위 폴더가 없으면 만든다.)  
    (tree 명령어를 사용하면 디렉토리, 파일 구조를 트리형식으로 볼 수 있다.)  

    mkdir -m 700 폴더명 (디렉토리를 만들 때 권한까지 지정)  

    rm "파일명" (파일만 삭제 디렉토리는 불가)  
    rm -rf "디렉토리명" (디렉토리 전부 삭제)  
    rmdir 폴더명 폴더명 (빈 디렉토리만 삭제 가능 여러개도 ok)  
    mkdir -p 상위폴더/하위폴더 (폴더를 삭제할 때 상위 폴더도 함께 삭제한다.)  
    (다른 폴더나 파일이 존재할 경우 상위 폴더는 삭제되지 않는다.)  

    rm -f "파일명" (-f 옵션을 붙이면 삭제할 건지 다시 묻지 않고 바로 삭제)  
    rm -f * (현재 폴더에 있는 모든 파일을 바로 삭제합니다. 폴더는 삭제안됨)  
    rm -r  폴더명(파일이 들어있는 디렉토리를 삭제할 때는 rm -r 명령을 사용)  
    rm *.txt (확장자 txt 모든 파일 삭제. 각 파일에 대해 삭제여부를 물음.)  
    rm* (현재 폴더에 있는 모든 파일을 삭제. 각 파일에 대해 삭제여부를 묻고, 폴더가 있다면 삭제할 수 없다는 메시지 출력)  
    $ Sudo yum install git : git 설치 (yum은 Linux 설치 명령어)  
    $ sudo yum update : yum 업데이트  
    $ git clone "주소"  
    $ $ps 내 터미널에서 돌아가는 작업 보기, $ ps -ef 돌아가는 작업 전체보기  
    $ netstat -tnlp (현재 돌아가는 포트(서버)확인)  
    $ ps -ef | grep streamlit : |은 연쇄작용, grep은 찾아달라.  
        ec2-user "PID:숫자" : 해당 포트(서버)를 kill(끄기)하려면 PID 필요  
    $ nohup streamlit run app.py --server.port 포트번호 & (백그라운드 계속 실행)  
    $ ec2-user , $ conda activeate app_dash  가상환경 진입
### 포트(서버) 끄기  
    $ ps -ef | grep streamlit or netstat -tnlp 로 PID 확인 후 kill PID  
    지정해도 실행 안되는 포트번호가 있으니 주의  

