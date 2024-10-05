# Проект на Django 
Древовидное меню сайта

## Описание:
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/finepik/Menu.git
   cd Menu
   ```
2. **Установите зависимости**
    ```bash
    pip install -r requirements.txt
    ```
3. **Примените миграции:**
   ```bash
   python manage.py migrate
   ```
4. **Запуск сервера**
    ```bash
    python manage.py runserver
    ```

## Использование
После запуска сервера вы сможете получить доступ к приложению по адресу:
- Django API: http://localhost:8000/
