# Google Cloud Vision API

# Напишите программу, которая использует Google Cloud Vision API для анализа изображения и распознавания объектов.

# Напишите тут ваш код
from google.cloud import vision

import io

client = vision.ImageAnnotatorClient()

file_name = "path"
with open(file_name, 'rb') as img:
    content = img.read()

image = vision.Image(content=content)
resp = client.object_localization(image=image)
objects = resp.localized_object_annotations

for object_ in objects:
    print(f'Object name: {object_.name}')

