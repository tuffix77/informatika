money_capital = 20000 # Подушка безопасности
salary = 5000 # Ежемесячная зарплата
spend = 6000 # Траты за первый месяц
increase = 0.05 # Ежемесячный рост цен

# TODO Посчитать количество месяцев, которое можно протянуть без долгов

t = spend
for m in range (1, 100):
    if t > salary:
        money_capital -= ( t - salary)
        if money_capital < 0:
            ms = m - 1
            break
    else:
        ms = m
    t *= ( 1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", ms)