# Виджет банковских операций

## Создан для отработки навыков при обучении на backend-разработчика ##

*Данный проект будет дополняться и обновляться*

### Функционал:
 * Сокрытие данных карт / номеров счетов
 * Смена формата даты
 * Сортировка списков:
    * По слову
    * По Дате
 * Генерация 16-ти символьных номеров карт
 * Вывод операций по определенному коду валюты
 * Вывод описания операций

### Для запуска:
*PyCharm*

1. Клонируйте репозиторий по [ссылке](git@github.com:ngiubaba/home_work10.git)
2. Активируйте виртуальное окружение poetry
3. Установите зависимости по команде:
```
poetry add --group lint flake8@7.1.1 mypy@1.15.0 black@25.1.0 isort@6.0.0
```
4. Запустите файл **main.py**

## Тестирование
### Добавлены модули для теста:
#### Модуль test_masks.py:
* Тест Функции get_mask_card_number
* Тест Функции get_mask_account

#### Модуль test_widget.py
* Тест функции mask_account_card
* Тест функции get_date

#### Модуль test_processing.py
* Тест для функции filter_by_state
* Тест для функции sort_by_date

#### Модуль test_generators.py
* Тест для функции filter_by_currency
* Тест для функции transaction_descriptions
* Тест для функции card_number_generator

### Для запуска теста:
1. Установите зависимости через виртуальное окружение poetry:
```commandline
poetry add --group dev pytest
```
2. Запустите тесты командой: 
```commandline
pytest
```
3. Для просмотра и вывода отчета установите зависимость:
```commandline
poetry add --group dev pytest-cov
```
*Что бы вывести отчет введите команду:*
```commandline
pytest --cov
```
 — при активированном виртуальном окружении.
```
poetry run pytest --cov
```
 — через poetry.
```
pytest --cov=src --cov-report=html
```
 — чтобы сгенерировать отчет о покрытии в HTML-формате, где 
src
 — пакет c модулями, которые тестируем. Отчет будет сгенерирован в папке 
htmlcov
 и храниться в файле с названием 
index.html

## Вы великолепны ##
*Разработчик Владислав Рябоконь*

*файл обновлен 24.02.2025*