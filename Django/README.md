# [Django] 설치

venv 로 가상환경을 만들면 폴더가 생기는데 git에 올릴 때는 가상환경을 올리지 않는다고 한다

pyenv는 따로 폴더가 생기지 않으니 저걸로 그냥 해야겠다.

## Pyenv

먼저 home-brew 를 설치해야 한다

~~~cmd
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
~~~



```cmd
$ brew install pyenv
$ brew install pyenv-virtualenv
$ vi ~/.bash_profile
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv virtualenv-init -)"
eval "$(pyenv init -)"

$ source ~/.bash_profile
```

> 처음 brew install pyenv 만 했는데 오류남 ㅎ



1. #### 가상환경 생성

   가상환경을 만들고 싶은 폴더 안에서 명령어 실행할 것.

   ```cmd
   $ pyenv install 3.6.5
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

4. #### 확인, 삭제

   ~~~cmd
   $ pyenv versions
   하면 설치된 pyenv 버전들 보여줌
   
   $ pyenv uninstall name
   ~~~


## Venv

Venv는 Python 3.3 버전 이후 부터 기본 모듈에 포함된다.



1. #### 가상환경 생성

   가상환경을 만들고 싶은 폴더 안에서 명령어 실행할 것.

   ```cmd
   $ python3 -m venv name
   ```

2. #### 활성화

   ```cmd
   $ source name/bin/activate
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

   ```cmd
   $ deactivate
   ```

5. #### 삭제

   ```cmd
   $ rm -rf name
   ```

   그냥 폴더 삭제하면 되는 듯.


