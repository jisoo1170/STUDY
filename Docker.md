# Docker

가벼운 vm

os 단을 가볍게

도커머신 설치하면 컴퓨터를 여러개 만들 수 있는데 그게 컨테이너 = 가상 컴퓨터

도커허브에는 이미 이미지가 많이 있음 

##### 컨테이너 만드는 방법

docker file -> build -> image (설계도) 생성됨 (수정불가/상속가능 - 확장성 용이) -> run -> container (설계도로 만들어진 컴퓨터)



##### 컨테이너 만드는 과정

- from  : 상속받을 이미지

- env : 환경변수 설정

- arg (arguement) : 도커파일 내에 쓸 수 있는 변수 설정

- copy : 의존성을 먼저 복사하고 설치한 다음에 프젝을 옮긴다

  이미지 빌드 할 때 변경 된 파일 라인 밑에부터 새롭게 해야되는데 서버 만들 때 의존성 바뀌는게 없기 때문에 바뀌는게 많은 것을 따로 뺴준것

- workdir : 명령 수행할 디렉토리 설정

- run : 명령어 실행

- 프젝 코드 이동

- expose : 도커 외부랑 통신할 떄 쓰는 포트 , 실행할 때 진행할 수 있음

- cmd : 이미지 빌드에는 안씀. 처음 실행할 때 수행되는 명령어 ["", ""] 하면 띄어쓰기 자동으로 해줌



컨테이너는 각자 컴퓨터에 있는거고 파일을 공유해서 환경을 맞추기 위한것

이미지로 컨테이너를 실행



도커 이미지 만들기

~~~ cmd
docker build -t sample-imgae .
~~~

-t : 태그 이름

. 어디에 이미지를 만들건지 . 은 현재 폴더



~~~cmd
docker images 이름
~~~

하면 지정된 이미지 보임



빌드 실패하면 None 생김 삭제하는 방법

~~~cmd
docker rmi $(docker images -f "dangling=true" -q)
~~~



도커 컨테이너 실행

~~~cmd
docker run -d 이름
~~~

-d : 백그라운드에서 실행





컨테이너 실행할 때 옵션들

~~~cmd
docker run -d --name sample-container --rm -p 4000:4000 -v $PWD:/my-project/web sample-image
~~~

이렇게 하면 도커id 말고 이름으로 다 할 수 있음

--rm : 컨테이너 꺼지면 바로 삭제한다

-p 4000:4000 :  왼쪽이 나 오른쪽이 도커 서버

-v : 볼륨 설정, 내 컴퓨터 코드가 도커에 해당된 디렉터리에 덮어쓰기 그니까 동기화 느낌?



터미널 연결해서 쓰기

~~~cmd
docker run -it --name sample-container -p 4000:4000 -v $PWD:/my-project/web --entrypoint bash sample-image
~~~





꺼진 도커 다시 실행

~~~cmd
docker start 도커이름
~~~



켜진 도커 껐다 다시 켜기

~~~cmd
docker restart 도커이름
~~~



실행 중인 도커 보기

~~~cmd
docker ps
~~~



실제 보고싶다

~~~cmd
docker logs 컨테이너id
~~~



도커 컨테이너  멈추기

~~~cmd
docker stop 컨테이너id
~~~



컨테이너 삭제

~~~cmd
docker rm 컨테이너id
~~~



컨테이너 터미널 들어가기

~~~cmd
docker exec -it  컨테이너이름 /bin/bash
~~~





이미지 삭제

~~~cmd
docker rmi sample-image
~~~





## docker-compose

여러개 껐다 켰다 가능하게

server

build : 도커파일 위치

ports: 포트 설정

volumes: 도커 볼륨 파일 위치



도커 컨테이너 만들기

~~~cmd
docker-compose up -d
~~~

-d : 백에서 돌리기



현재 폴더 이름 뒤에 _server 붙어서 이름이 생성됨



도커 여러개 한번에 종료

~~~cmd
docker-compose stop
~~~



도커 한번에 다 실행

~~~cmd
docker-compose strat
~~~



다 삭제

```cmd
docker-compose down
```



디비 / 서버 / 프론트 따로 만들어서 한번에 올리고 다 끝내고

안헷갈리고 좋음



## Kubernetes/Swarm

도커 컨테이너 묶어서 껏다 켰다 라우팅 - 오케스트레이션

docker-compose 자동실행 한다고 보면됨



## 도커장점

개발이 쉬워진다

배포가 쉬워진다 - 이미지 받아서 실행시켜놓고

aws에 **ElasticBeanstalk** - 도커파일 지원 "ev-deploy" 자동으로 배포해줌



vs코드에서 도커 환경에서 개발하고싶을때

remote-container 설치하고 커맨드 t 누른다음에

~~~cmd
>remote
~~~

연결해서 사용 attach to container

하면 컨테이너 내부에 파일에서 개발할 수 있음

볼륨할 필요는 있음 파일 남기기 위해서





행아웃 말고 디스코드

더브이씨- 스타트업 투자 받은거 보는곳 이걸 봐야