# Git 기초 명령어



## 공유

```cmd
git config --global user.name "이름"
git config --global user.email "이메일"
git clone 공유할 주소
```



## 업로드

~~~cmd
git add .(모든거)/파일명
git commit -m "설명"
git pull
git push (-u origin master 처음에만)
~~~

중간에 pull 을 하는 이유는 내가 올리기 전에 다른 사람이 push 했을 수도 있으니 충돌 안나게 해주려고!

혼자하면 안해도 됨



## 로컬 저장소를 원격 저장소에 맞게 갱신

~~~cmd
git pull
~~~

