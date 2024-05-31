## Урок 3. Инструменты работы и визуализации
Соберите данные о погоде в разных городах мира за последний месяц.
Используйте открытые источники данных, такие как АPI погодных сервисов
или веб - скрейпинг.

Выведите график изменения температуры в разных городах,
график распределения тпемпературы.

Ход выполнения.

Из семинара "Superset"
Установка Superset выпонялась в VirtualBox.
Установлена последняя версии VirtualBox и Ubuntu.
Выполнены необходимые действия для загрузки файла 
в формате csv. 
Изучались различные гайды по установке !!!

https://habr.com/ru/articles/773296/

https://web.archive.org/web/20220415100312/https://habr.com/ru/post/661159/

https://datafinder.ru/products/kak-ustanovit-na-ubuntu-apache-superset

Установка выполняется успешно, но загрузить файл в формате csv - не получается.
Все необходимые действия при подключении были выполнены!

Необходимые скриншоты для пояснения.

Teminal
<image src="img/Terminal.png" alt="wind">
<image src="img/Логи.png" alt="wind">

Настройки в superset

<image src="img/Настройки.png" alt="wind">
<image src="img/Настройки2.png" alt="wind">
<image src="img/Настройки3!.png" alt="wind">

Загрузка файла

<image src="img/Загрузка файла.png" alt="wind">
<image src="img/Загрузка2.png" alt="wind">

Файл далее не загружается ???

Выполнение ДЗ!

Для сбора данных использовался сайт 
https://openweathermap.org/

К сожалению Limits - Hourly forecast: unavailable
Daily forecast: unavailable
Calls per minute: 60
3 hour forecast: 5 days

#### С учётом этого получаем данные и сохраняем их для дальнейшего использования в файле [text](weather_data.json) - weather_data.json

#### Обработка файла и построение графиков выполнено в google colab и сохранено в файле 
#### weathergraf.ipynb

