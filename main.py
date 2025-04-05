import asyncio
from pathlib import Path
from project.parser import parse_restaurants, save_to_md
from project.main_parser import parse_data


BASE_DIR = Path("D:/Projects/RestaurantGuru")
PRE_DATA_DIR = BASE_DIR / "pre_data"
OUTPUT_DIR = BASE_DIR / "output_files"

MD_FILE_PATH = PRE_DATA_DIR / "restaurants_Kalinkavichy.md"
OUTPUT_FILE_PATH = OUTPUT_DIR / "data_Kalinkavichy.md"

async def run():
    print("🚀 Запуск парсинга ресторанов...")
    restaurants = parse_restaurants()

    if not restaurants:
        print("❌ Ошибка: Не удалось получить список ресторанов!")
        return


    PRE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("\n💾 Сохранение данных...")
    save_to_md(restaurants, PRE_DATA_DIR)

    print("\n🔍 Запуск парсинга номеров телефонов...")
    await parse_data(MD_FILE_PATH, OUTPUT_FILE_PATH)
    print("✅ Парсинг завершен ")

if __name__ == "__main__":
    asyncio.run(run())