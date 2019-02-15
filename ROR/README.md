# Ruby on Rails 설치하기

1. ### Homebrew

   ~~~cmd
   ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ~~~

2. ### Ruby

   ~~~cmd
   brew install rbenv ruby-build
   
   # Add rbenv to bash so that it loads every time you open a terminal
   echo 'if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi' >> ~/.bash_profile
   source ~/.bash_profile
   
   # Install Ruby
   rbenv install 2.4.4
   rbenv global 2.4.4
   ruby -v
   ~~~

3. ### Rails

   ~~~cmd
   gem install rails -v 4.2.10
   rbenv rehash
   rails -v
   ~~~



[gorails참고](https://gorails.com/setup/osx/10.13-high-sierra)

### 프로젝트 만들기

~~~cmd
rails new 이름
~~~



### 프로젝트 실행

~~~cmd
rails s
~~~



### gem 삭제

~~~cmd
gem uninstall <이름>

#이거는 전체삭제 이거하면 rails 도 삭제됨
gem uninstall -aIx
~~~

