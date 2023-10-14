# AutomiqTest

## Python Version
***python version 3.11.4***

## Libraries
+ ***PyQt-6.5.2 для создания интерфейса***
+ ***PyInstaller-6.0.0 для создания исполняемых файлов***
+ ***logging для логирования***
+ ***json для работы с конфиг файлами***
+ ***unittest для тестирования***

## Запуск исполняемых файлов
Для запуска интерфейса программы нужно в папке dist запустить файл Window_UI.exe.<br/><br/>
Для запуска тестов нужно в папке dist запустить файл algorithm_tests.exe, после запуска перейти в папке dist в файл logging.log, где и будут описаны результаты прохождения тестов.

## Main algorithm
Скрипт алгоритма находится в файле algorithm.py.<br/><br/>
Сортировка происходит методом слияния, но также в комментах предложен альтернативный способ сортировки.
```
# return sorted(objects, key=lambda obj: self.order.index(obj.color))
```

## UI Script
Скрипт интерфейса находится в файле Window_UI.py.<br/><br/>
Для работы с интерфейсом представлена функция автоматической генерации данных для сортировки и порядка сортировки(**event on_ButtonRandom_clicked**), и сама функция сортировки(**event on_ButtonSort_clicked**).<br/>

## Algorithm Testing
Скрипт тестирования алгоритма находится в файле algorithm_test.py, ***но запускать тесты нужно только через исполняемый файл***.<br/><br/>
Всего тестируется 3 ситуации:

1. Позитивные ситуации описаны в конфиг файле dist/positive_testcases.json
2. Ситуации с неправильным вводом последовательности сортировки в конфиг файле dist/negative_order_testcases.json
3. Ситуации с неправильным вводом данных для сортировки в конфиг файле dist/negative_input_testcases.json

Для каждого конфиг файла написан класс с циклом, проверяющий все тест-кейсы. Для того, чтобы добавить новый тест-кейс, надо в конфиг файле добавить новый json объект в массив.<br/><br/>

### Логирование
Логирование всех тестовых ситуаций ведётся в файл logging.log
