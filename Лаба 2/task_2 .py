salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
for month in range(months):
    money_capital += spend - salary  # Рассчитываем необходимую сумму для каждого месяца
    spend *= (1 + increase)  # Увеличиваем траты на следующий месяц

result_string = str(round(money_capital, 2))
print(result_string)
