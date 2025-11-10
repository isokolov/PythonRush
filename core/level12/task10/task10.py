# Запись бинарных данных

# Напишите программу, которая читает изображение input_image.jpg и записывает его в другой файл output_image.jpg.

# Напишите тут ваш код
with open('input_image.jpg', 'rb') as infile:
    image_data = infile.read()

with open('output_image.jpg', 'wb') as outfile:
    outfile.write(image_data)
