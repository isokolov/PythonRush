# Словарь с данными о доходах и расходах за каждый день недели
week_financials = {
    "Понедельник": 100,
    "Вторник": 150,
    "Среда": 200,
    "Четверг": 250,
    "Пятница": 300,
    "Суббота": 200,
    "Воскресенье": 200
}

# Вычисление общей прибыли за неделю
total_profit = sum(list(map(int,week_financials.values())))

# Вычисление среднедневной прибыли
average_daily_profit = total_profit/len(week_financials.keys())

# Вывод результатов
print("Общая прибыль за неделю:", total_profit)
print("Среднедневная прибыль:", average_daily_profit)
