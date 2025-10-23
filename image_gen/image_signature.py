import os
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Получаем API ключи из переменных окружения
api_key = os.getenv("OPENAI_API_KEY")  # Устанавливаем ключ OpenAI из переменной окружения
base_url = os.getenv("OPENAI_BASE_URL", "https://api.proxyapi.ru/openai/v1")

openai = OpenAI(api_key=api_key, base_url=base_url)

def generate_post(topic):
    prompt = f"""
        Используй тему для генерации оригинальной вдохновляющей цитаты.
        Она должна быть краткой, лаконичной и легкой для понимания.
        Цитата должна иметь потенциал изменить чью-то жизнь.
        Максимум 25 слов.
        ---
        Тема: {topic}
        Вдохновляющая цитата:
        """
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

# Текст, который нужно добавить
# text = generate_post("парящий орёл")
# print(text)
text = "Парящий орёл не боится высоты; он знает, что только преодолевая страх, можно увидеть мир с новой перспективы."
# Открываем изображение
img = Image.open('story.jpg').convert('RGBA')

# Создаем объект для рисования на изображении
draw = ImageDraw.Draw(img)

# Задаем шрифт и размер шрифта (обязательно шрифт с поддержкой кириллицы)
font_path = 'Roboto-Thin.ttf'  # Убедитесь, что шрифт поддерживает кириллицу
font = ImageFont.truetype(font_path, 65)

# Получаем размеры изображения
img_width, img_height = img.size

# Задаем начальную позицию для текста
x, y = 100, 100

# Разбиваем текст на строки по переносу
lines = []
line = ""
for word in text.split():
    if draw.textlength(line + word, font) <= img_width - 200:
        line += word + " "
    else:
        lines.append(line.strip())
        line = word + " "
lines.append(line.strip())

# Получаем высоту строки
ascent, descent = font.getmetrics()
line_height = ascent + descent

# Получаем размеры текста
text_width = max(draw.textlength(line, font) for line in lines)
text_height = line_height * len(lines)

# Создаем новый слой с темно-синим цветом и прозрачностью 70%
overlay = Image.new('RGBA', (int(text_width), int(text_height)), (0, 0, 128, 180))

# Объединяем изображение и слой с помощью наложения
img.paste(overlay, (int(x), int(y)), mask=overlay)

# Добавляем текст на изображение, перенося на новую строку при необходимости
for line in lines:
    draw.text((x, y), line, font=font, fill=(255, 0, 0))
    y += line_height

# Удаляем альфа-канал
img = img.convert("RGB")

# Сохраняем изображение в формате JPEG
img.save("story_text.jpg")

if __name__ == "__main__":
    img = Image.open("story_text.jpg")
    img.show()