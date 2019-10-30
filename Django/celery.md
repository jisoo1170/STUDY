# [django] Celery 를 이용한 비동기 태스크

### 1. RabbitMQ 설치하기 (mac)

Homebrew를 이용해서 설치할거라서 brew가 없다면 아래 명령어를 통해 설치해준다.

~~~cmd
$ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
~~~



그 다음 rabbitmq 설치

~~~cmd
$ brew install rabbitmq
~~~



브로커(rabbitMQ)를 시작하고 중지 할 수 있도록 경로에 다음을 추가해 준다.

 쉘의 시작 파일 (예 : `.bash_profile`또는 `.profile`)에 추가

```cmd
$ vi ~/.bash_profile

PATH=$PATH:/usr/local/sbin

변경한거 적용
$ source ~/.bash_profile
```



서버 시작

```cmd
$ sudo rabbitmq-server
```

`-detached`옵션 을 추가하여 백그라운드에서 실행가능

```cmd
$ sudo rabbitmq-server -detached
```



서버 중지

```cmd
$ sudo rabbitmqctl stop
```



### 2. Celery 설치하기

~~~cmd
$ pip install celery
~~~



### 3. 설정하기

**project/project/celery.py** 파일을 만든다. project/project 안에는 __init.py, settings.py 등이 있다.

그리고 그 안에 다음과 같은 코드를 포함해준다.

~~~python
from __future__ import absolute_import

import os

from celery import Celery

# Django의 세팅 모듈을 Celery의 기본으로 사용하도록 등록합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from django.conf import settings  # noqa

app = Celery('project')

# 문자열로 등록한 이유는 Celery Worker가 Windows를 사용할 경우
# 객체를 pickle로 묶을 필요가 없다는 것을 알려주기 위함입니다.
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#위 코드로 celery는 자동적으로 장고 세팅에 재사용 가능한 앱에서 tasks.py를 찾을 겁니다.
#app/tasks.py

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
~~~



**init.py**

~~~python
from __future__ import absolute_import

# 아래 import는 장고가 시작될 때 항상 import되기 때문에
# shared_task가 장고에서 작동하는 것을 가능하게 해 줍니다.
from .celery import app as celery_app # Celery를 import합니다.

__all__ = ('celery_app',)
~~~



**settings.py**

~~~python
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_RESULT_BACKEND = 'amqp://localhost'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
~~~



**app/tasks.py**

~~~python
from __future__ import absolute_import

from celery import shared_task

@shared_task
def add(x, y):
    return x + y
~~~



저 task 를 어떻게 해야 호출이 일어난 다음에 불러올까 찾아봤는데 답은!!! 일단 view로 보내서 view에서 task를 호출해주면 된다.

~~~python
from project.tasks import add

def clickview(request,pk):
    add.delay(pk이런식으로 넘겨줄 인자?들)
    
    //여기는 다시 돌아갈 페이지
    return redirect('board:playlist_detail', pk)
~~~



### 4. 실행 시키기

Celery 실행

~~~cmd
celery -A project worker -l info
~~~



다른 cmd 창에서 장고 실행

아 RabbitMQ는 실행중이어야 한다.



### 5. 결과 저장하기

먼저 필요할 라이브러리 설치

~~~cmd
$ pip install django-celery-results
~~~



settings.py 안에 추가해준다.

~~~python
INSTALLED_APPS = (
    ...,
    'django_celery_results',
)
~~~



마이그레이트 해주기

~~~cmd
$ python manage.py migrate django_celery_results
~~~



settigs.py에 아래 부분을 수정

~~~python
//db에 저장하고 싶으면
CELERY_RESULT_BACKEND = 'django-db'

//cache에 저장하고 싶으면
CELERY_RESULT_BACKEND = 'django-cache'

~~~

