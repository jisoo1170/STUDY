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