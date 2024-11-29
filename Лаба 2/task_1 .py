money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
money_spend = 0
while money_capital > money_spend :
        money_capital += salary
        money_spend += spend
        spend += spend * increase
        month += 1
print(month)
