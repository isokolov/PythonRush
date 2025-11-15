# Шаг 1: Создаем новое виртуальное окружение с именем "myenv"
python -m venv myenv
# Шаг 2: Активируем виртуальное окружение
source myenv/bin/activate
# Шаг 3: Устанавливаем библиотеки pandas и openpyxl с помощью pip
pip install pandas openpyxl
# Шаг 4: Проверяем установку, выводя версии pandas и openpyxl
pip show pandas
pip show openpyxl
