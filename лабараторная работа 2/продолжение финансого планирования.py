salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Инициализация переменных
money_capital = 0  # Подушка безопасности, которую нужно найти
current_spend = spend  # траты за месяц
# Проходим по всем месяцам
for month in range(1, months + 1):
    # Если зарплаты не хватает на расходы, добавляем недостающую сумму к подушке
    if salary < current_spend:
        money_capital += current_spend - salary

    # Увеличиваем расходы на следующий месяц
    if month < months:
        current_spend *= (1 + increase)

# Округляем до целого числа
money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)