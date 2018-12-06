# Git 기초 명령어



## 깃 설치하고 처음에 설정하는거

~~~cmd
git config --global user.name "이름"
git config --global user.email "이메일"
~~~

local 하면 폴더 안에서만 그런거



## 공유

```cmd
git clone 공유할 주소
```



## 새로 레포지토리 파기

로컬에 폴더 만든 다음에 동기화 시키는 것

~~~cmd
git init
git add README.md
git commit -m "설명"
git remote add origin 주소
git push -u origin master
~~~



## 업로드

~~~cmd
git add .(모든거)/파일명
git commit -m "설명"
git pull
git push
~~~

중간에 pull 을 하는 이유는 내가 올리기 전에 다른 사람이 push 했을 수도 있으니 충돌 안나게 해주려고!

혼자하면 안해도 됨



## 로컬 저장소를 원격 저장소에 맞게 갱신

~~~cmd
git pull (origin master-어떤 브렌치 인지)
~~~
