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

### Клонирование репозитория и переход в него в командной строке:

```bash
git clone git@github.com:Eugenii1996/scrapy_parser_pep.git
```

```bash
cd scrapy_parser_pep
```

### Cоздать и активировать виртуальное окружение:

Виртуальное окружение должно использовать Python 3.7

```bash
pyhton -m venv venv
```

* Если у вас Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

### Установка зависимостей из файла requirements.txt:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

### Запуск проекта:

Из корневой деректории проекта scrapy_parser_pep выполнить команды:

```bash
scrapy crawl pep
```
