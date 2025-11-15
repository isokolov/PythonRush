# Создание виртуального окружения в директории 'venv'
python -m venv myenv

# Активация виртуального окружения
source myenv/bin/activate

# Установка необходимых библиотек
pip install pandas
pip install openpyxl
# Вывод версий установленных библиотек
pip show pandas
pip show openpyxl

# Деактивация виртуального окружения
source deactivate
