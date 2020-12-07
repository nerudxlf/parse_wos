#Парсер сайта publons

Данная программа получает данные об авторе с сайта publons.com.

Получаемые данные:
1) Name
2) Publications
3) Total time cited
4) h-index

На входе програама используется файл с id аторов.
(Пример id - S-6929-2018).
Файл должен называться id.txt и находится в главной директории проекта.

На выходе получается .xlsx таблица с полученными значениями


## Установка и использование
Программа использует Selenium и в качестве браузера используется Chrome
Вы должны установить webdirver для Chrome https://chromedriver.chromium.org/downloads

Для парсинга используется bs4, для выгрузки данных в таблицу pandas

    pip install selenium
    pip install pandas
    pip install bs4

