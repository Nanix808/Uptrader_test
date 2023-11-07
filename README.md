<h1 align="center">✨ TEST UpTrader ✨</h1>

<p align="center">  
<img src="https://img.shields.io/badge/python-3.12 -blueviolet.svg">

</p>


## ***Навигация***
- [Описание](#описание)
- [Технологии](#Технологии)
- [How to install](#how_to_install)

<a name="описание"></a> 
## ***Описание***

![](https://github.com/Nanix808/Uptrader_test/blob/main/static_repo/demo.gif)


Тестовое задание для компании UpTrader

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
 
Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
{% draw_menu 'main_menu' %}
При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

<a name="computer_vision_and_machine_learning"></a> 
### Технологии

- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/)

<a name="how_to_install"></a> 
## ***How to install***

- Метод (Подходит для разворачивания с помощью Docker):
  - Клонировать репозиторий
  - Перейти в папку где находится файл docker-compose.yml
  - Выполнить команду docker-compose build
  - Выполнить команду docker-compose up
  - Пререйти по адресу 127.0.0.1:8000/menu/


- Метод (Подходит для разворачивания локально):
  - Установить python
  - Клонировать репозиторий
  - Выполнить команду  RUN python -m pip install --upgrade pip
  - Выполнить команду RUN python -m pip install -r requirements.txt
  - Выполнить команду python manage.py runserver
  - Пререйти по адресу 127.0.0.1:8000/menu/



Логин и пароль к админке:

User: uptrader

Password: uptrader