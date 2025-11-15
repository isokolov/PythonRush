import pandas as pd

# Чтение данных из Excel-файла "students.xlsx"


# Вывод первых пяти строк данных в виде DataFrame
try:
    df = pd.read_excel("students.xlsx")
    print(df.head())
except:
    print("We have error!")
