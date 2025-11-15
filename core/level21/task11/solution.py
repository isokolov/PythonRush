import pandas as pd

# Чтение данных из Excel-файла "employees.xlsx" с указанием листа "Данные"
try:
    df = pd.read_excel("employees.xlsx",sheet_name="Данные")
    df_30 = df[df["Возраст"]>30]
    print(df_30)
except:
    print("We have error!")
# Фильтрация строк, где значение в колонке 'Возраст' больше 30


# Вывод отфильтрованных данных на экран
