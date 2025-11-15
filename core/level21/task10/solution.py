import pandas as pd

# Чтение данных с листа "Q1" в файле "sales_data.xlsx"
try:
    df = pd.read_excel("sales_data.xlsx",sheet_name="Q1")
    print(df.head(10))
except:
    print("We have error!")

# Вывод первых десяти строк DataFrame на экран
