import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_driver():
    """Настройка и запуск Selenium WebDriver."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def parse_restaurants():
    """Парсит список ресторанов (название, ID, ссылка) и возвращает данные в виде списка словарей."""
    driver = setup_driver()
    url = 'https://restaurantguru.ru/Mazyr#restaurant-list'
    driver.get(url)
    time.sleep(5)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("✅ Саня начинает парсинг...")


    restaurant_cards = driver.find_elements(By.CLASS_NAME, "rest_info")
    name_elements = driver.find_elements(By.CLASS_NAME, "item__title")

    if not restaurant_cards or not name_elements:
        print("❌ Ошибка: Не найдены рестораны на странице!")
        driver.quit()
        return []

    restaurants = []

    for index, (card, name_el) in enumerate(zip(restaurant_cards, name_elements), start=1):
        try:
            link_element = card.find_element(By.CLASS_NAME, "title")
            link = link_element.get_attribute("href")

            raw_name = name_el.text.strip()
            name = re.sub(r"^\d+\.\s*", "", raw_name).strip()

            restaurants.append({
                "№": index,
                "Название": name,
                "Ссылка": link
            })

        except Exception as e:
            print(f"Ошибка при парсинге ресторана: {e}")
            continue
    driver.quit()
    return restaurants


def save_to_md(data, output_file="restaurants_mazyr.md"):
    """Сохраняет список ресторанов в Markdown с кликабельными ссылками, обработкой пустых значений."""
    if not data:
        print(" Нет данных для сохранения!")
        return

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("#  Список ресторанов Мозыря\n\n")
        file.write("| №  | Название | Ссылка |\n")
        file.write("|----|----------|--------|\n")

        for row in data:
            index = row.get("№", "N/A")
            name = row.get("Название", "Неизвестно").strip()
            link = row.get("Ссылка", "").strip()

            link_md = f"[Ссылка]({link})" if link else "Нет ссылки"

            file.write(f"| {index} | {name} | {link_md} |\n")


    print(f"✅ Данные успешно сохранены в {output_file}")

restiki = parse_restaurants()
save_to_md(restiki)
