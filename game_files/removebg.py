from PIL import Image, ImageOps, ImageDraw

def remove_background(input_image_path, output_image_path, threshold=200):
    # Загрузка изображения
    image = Image.open(input_image_path)

    # Преобразование изображения в оттенки серого
    gray_image = ImageOps.grayscale(image)

    # Создание маски по порогу яркости
    mask = gray_image.point(lambda p: p < threshold and 255)

    # Применение маски к изображению
    result = Image.new("RGBA", image.size, (255, 255, 255, 0))
    result.paste(image, mask=mask)

    # Сохранение результата
    result.save(output_image_path, format="PNG")

# Пример использования
input_path = 'images/arrow.jpg'
output_path = 'images/arrow_requiem.jpg'
remove_background(input_path, output_path)

