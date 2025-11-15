import pandas as pd

# Создание первого DataFrame с данными о продуктах
products_data = {
    "Наименование": ["Яблоки", "Бананы", "Апельсины"],
    "Цена": [100, 80, 90]
}


# Создание второго DataFrame с данными о покупателях
customers_data = {
    "Имя": ["Алексей", "Мария", "Иван"],
    "Возраст": [30, 25, 40]
}
df1 = pd.DataFrame(products_data)
df2 = pd.DataFrame(customers_data)

# Запись обоих DataFrame в один Excel-файл
with pd.ExcelWriter("market_data.xlsx") as writer:
    df1.to_excel(writer,sheet_name="Продукты",index=False)
    df2.to_excel(writer,sheet_name="Покупатели",index=False)
