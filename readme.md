✨ Название проекта: 
Scraping_restaurants

✨ Описание:
Код парсера извлекает данные о ресторанах с https://restaurantguru.ru/, в частности:
id | Название | Ссылка
После чего открывает сформированный файл и проходится по каждой ссылке извлекая номера 
телефонов, фиксируя результат в файл директории fix_files.

✨ Стек:
asyncio, playwright, bs4, re, webdriver_manager, selenium. 
Весь список зависимостей находится в файле req.txt

✨Структура проекта:
RestaurantGuru/
│
├── fix_files/
│
├── output_files/
│
├── pre_data/
│
└── project/
    ├── .gitignore
    ├── data.md
    ├── main.py
    ├── readme.md
    ├── req.txt

│
└── venv/

✨Установка и запуск:

1. Копирование проекта: Git clone https://github.com/Brin84/Scraping-restaurants
2. Создать виртуальное окружение: python -m venv venv 
3. Активировать виртуальное окружение: venv\scripts\activate
4. Установка зависимостей: pip install -r req.txt
5. Установка playwright: playwright install
6. Запуск приложения: python main.py
