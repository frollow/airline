**Airline**

Установка Windows:

1. Установить *[postgreSQL](http://www.enterprisedb.com/products/pgdownload.do#windows)*.
При установке попросят ввести пароль для пользователя c именем **postgres**, он пригодится в пункте **5**.
2. Перейти в папку проекта

        cd C:\Users\Admin\Desktop\airline
3. Установить зависимости из *requirements.txt* через настройки *PyCharm* в разделе *Project Interpreter*
(если *PyCharm Professional Edition* ) или через командную строку:

        pip install -r requirements.txt

4. Создать БД с именем **avia** через уже установленный *pgAdmin III*
5. Создать пользователя **avia**, пароль **12345** в командной строке

        psql -U postgres -c "CREATE ROLE avia password '12345' LOGIN NOSUPERUSER INHERIT CREATEDB CREATEROLE;" avia
6. Запустить *migrate* для создания необходимых таблиц в БД

        python manage.py migrate

<hr/>
Python has a little SMTP server built-in. You can start it in a second console with this command:

python -m smtpd -n -c DebuggingServer localhost:1025
This will simply print all the mails sent to localhost:1025 in the console.

You have to configure Django to use this server in your settings.py:

        EMAIL_HOST = 'localhost'
        EMAIL_PORT = 1025