import pandas as pd

# Создаем данные для каждого квартала
data_first_quarter = {
    "Товар": ["Товар A", "Товар B", "Товар C"],
    "Количество": [100, 150, 200],
    "Прибыль": [1000, 1500, 2000]
}

data_second_quarter = {
    "Товар": ["Товар D", "Товар E", "Товар F"],
    "Количество": [110, 160, 210],
    "Прибыль": [1100, 1600, 2100]
}

data_third_quarter = {
    "Товар": ["Товар G", "Товар H", "Товар I"],
    "Количество": [120, 170, 220],
    "Прибыль": [1200, 1700, 2200]
}

# Создаем DataFrame для каждого квартала
df1 = pd.DataFrame(data_first_quarter)
df2 = pd.DataFrame(data_second_quarter)
df3 = pd.DataFrame(data_third_quarter)


# Пишем DataFrame в Excel файл на разные листы
with pd.ExcelWriter("quarterly_sales.xlsx") as writer:
    df1.to_excel(writer,sheet_name="Первый квартал",index=False)
    df2.to_excel(writer,sheet_name="Второй квартал",index=False)
    df3.to_excel(writer,sheet_name="Третий квартал",index=False)
