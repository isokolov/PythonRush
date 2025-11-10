# Создание и удаление директорий

# Напишите программу, которая создает новую директорию new_directory.
# Затем создает вложенную директорию parent_directory/child_directory.
# А затем удаляет созданные директории.

import os
import shutil

# Створення директорії new_directory
# Write your code here
os.mkdir('new_directory')

# Створення вкладеної директорії parent_directory/child_directory
# Write your code here
os.makedirs('parent_directory/child_directory')

# Видалення директорії new_directory
# Write your code here
os.rmdir('new_directory')

# Видалення вкладеної директорії parent_directory/child_directory
# Write your code here
path = os.path.join('parent_directory', 'child_directory')
os.removedirs(path)
