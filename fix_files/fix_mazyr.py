import re


input_file = 'restaurants_mazyr.md'
output_file = 'mazyr.md'

def fix(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    fixed_content = re.sub(
        r"https://ru\.restaurantguru\.com/([^\s\)\]]+)",
        r"https://restaurantguru.ru/\1",
        content
    )
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(fixed_content)

    print("🔥 Ссылки успешно обновлены и сохранены в", output_file)

fix(input_file, output_file)