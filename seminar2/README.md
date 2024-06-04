### Урок 2. SQL & Big Data

Условие:
Загрузите датасет по ценам на жилье Airbnb, доступный на kaggle.com: https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
Подсчитайте среднее значение и дисперсию по признаку ”price” в hive
Используя Python, реализуйте скрипт mapper.py и reducer.py для расчета
Проверьте правильность подсчета статистики методом mapreduce в сравнении со hive.

### Выполнение
#### Скрип и подсчёты отражены mapper.py и reducer.py  отражены в - seminar2.ipynb.

#### Подсчёт среднего значения и дисперсии по признаку ”price” в hive.

Произведём установку и запуск контейнеров в терминале Ubuntu на Virtualbox, предварительно удалив все предыдущие образы, которые были установлены ранее. 

<image src="img/Запуск контейнеров.png" alt="wind">

Заходим на have-server и учимся создавать таблицы:

<image src="img/таб.png" alt="wind">

Произведём чтение и запись файлов для дальнейшей обработки в контейнер namenode, предварительно скопировав их и поменяв права пользователя для дальнейшей обработки файлов в контейнере have-server:

<image src="img/Копирование файлов.png" alt="wind">

Подтверждение, что файлы не пустые 

<image src="img/Подтверждение.png" alt="wind">

Чтение файла artists.csv

<image src="img/Чтение файла.png" alt="wind">

Cоздали и заполнили таблицу ab_nyc на hive-server

<image src="img/S1.png" alt="wind">

<image src="img/Таблица ДЗ.png" alt="wind">

Все таблицы

<image src="img/Созданные таблицы.png" alt="wind">

Искомые средняя цена и дисперсия

<image src="img/Искомые дисперсия и средняя цена.png" alt="wind">

Контейнеры в браузере

<image src="img/Hue.png" alt="wind">

<image src="img/localhost.png" alt="wind">

Finish

<image src="img/Закрытие.png" alt="wind">
