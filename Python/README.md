# Python 설치하기

mac 에 기본으로 파이썬 2.x 버전이 깔려 있어서 설치가 너무 어려웠다...

포맷을 몇 번 했는지 모르겠다. 그래서 정리해보는 mac에 파이썬 설치하기!!



Anaconda를 사용해서 설치했다. 아나콘다는 다양한 라이브러리 한번에 설치해줌

그냥 파이썬, 장고를 한다면 굳이 필요는 없고 딥러닝 할 때 사용하면 좋을 듯



### 1. Homebrew 설치

~~~cmd
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
~~~



### 2. pyenv 설치

~~~cmd
$ brew install pyenv
~~~



### 3. Anaconda 설치

~~~cmd
$ pyenv install anaconda3
~~~



### 4. 기본 값 설정

~~~cmd
$ pyenv global anaconda3
~~~



## Pyenv

1. #### 가상환경 생성

   가상환경을 만들고 싶은 폴더 안에서 명령어 실행할 것.

   ```cmd
   $ pyenv virtualenv 3.6.5 name
   ```

2. #### 활성화

   폴더 안에서 자동으로 활성화 되게 만들 수 있음.

   ```cmd
   $ pyenv local name
   ```

3. #### 장고 설치

   먼저 pip 최신 버전으로 만들어 준다.

   ```cmd
   $ python3 -m pip install --upgrade pip
   ```

   그 다음 장고 설치

   ```cmd
   $ pip install django~=1.11.0
   ```

4. #### 비활성화

   로컬 설정 삭제 해주기

   ```cmd
   $ pyenv local —unset
   ```

5. #### 삭제

   ```cmd
   $ pyenv uninstall name
   ```



## Anaconda

1. #### 콘다에서 가상환경 생성하기

   ```cmd
   $ conda create -n 이름 python=x.x
   ```

   버전을 안쓰면 가장 최신 버전으로 깔아준다.

2. #### 활성화

   ```cmd
   $ source activate name
   ```

3. #### 비활성화

   ```cmd
   $ source deactivate
   ```

4. #### 삭제

   ```cmd
   $ conda remove -n name --all
   ```

끝! 가상환경 사용하니까 맘도 편하고 아주 간단하다.



[참고](https://qiita.com/y4m3/items/19246624d3ba4d299313)