**Для чего**

Находит 10 самых больших по размеру запросов. Выдает url, код,
число запросов и размер. 

**Как использовать**
./top_10_by_size.sh "путь к log-файлу или папке" "путь к файлу, в который записать результат"

python top_10_by_size.py --file "путь к log-файлу" --result_file "путь к файлу, в который записать результат"

При использовании bash-скрипта можно вместо пути к файлу задать путь к директории, и скрипт
выполнится для каждого log-файла в этой директории.

При использовании python-скрипта можно не указывать путь к файлу, в который нужно записать результат. В этом случае
результат будет записан в файл script_result.txt, который будет создан в директории, из которой 
запускается скрипт. 

Кроме того, в качестве файла с результатом можно указыть *.json файл, 
результат будет записан в формате json. 

**Как работает**

Из всего log-файла выбираются столбцы, содержащие информацию об
url, status code и размере запроса. 

После этого подсчитывается количество уникальных запросов.

Запросы сортируются по размеру. В файл записываются 10 самых
больших.