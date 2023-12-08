from PIL import Image

def flip_image_vertical(input_path, output_path):
    # Открываем изображение
    original_image = Image.open(input_path)

    # Отражаем изображение по вертикали
    flipped_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)

    # Сохраняем отраженное изображение
    flipped_image.save(output_path)

if __name__ == "__main__":
    input_path = "images/player2.png"
    output_path = "images/player1.png"

    flip_image_vertical(input_path, output_path)