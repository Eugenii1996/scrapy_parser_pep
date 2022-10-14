# Проект асинхронного парсинга python документации

### Разработчик:

 - [Мирошниченко Евгений](https://github.com/Eugenii1996)

### О проекте:

Проект представляет собой парсер официальной документации PEP python на основе фреймворка [Scrapy](https://docs.scrapy.org/en/latest/index.html). 
Парсер имеет следующие возможности:
 - Сбор данных обо всех PEP с номером, названием и статусом
 - Подсчет общего количества PEP в каждом статусе

Стек технологий:
 - Python 3
 - Scrappy
 - Acyncio
 - Git
 - Pytest

### Клонировать репозиторий c GitHub:

```bash
git clone git@github.com:Eugenii1996/scrapy_parser_pep.git
```

После клонирования необходимо установить и активировать виртуальное окружение находясь в директории scrapy_parser_pep:

```bash
pyhton -m venv venv
```

Далее нужно обновить менеджер пакетов pip и установить зависимости:

```bash
pip install -r requirements.txt
```

### Запуск проекта:

Чтобы запустить проект, из директории scrapy_parser_pep нужно выполнить команду:

```bash
scrapy crawl pep
```
