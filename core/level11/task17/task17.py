
# Пересечение имен.
import math as std_math
import importlib.util
# Вызовите функцию sqrt вашего модуля math.
# Вызовите функцию sqrt встроенного модуля math.

# Напишите тут ваш код
print(std_math.sqrt(5))

custom_math_path = 'core/level11/task17/math.py'
spec = importlib.util.spec_from_file_location('custom_path', custom_math_path)
custom_math = importlib.util.module_from_spec(spec)
spec.loader.exec_module(custom_math)

custom_math.sqrt(5)