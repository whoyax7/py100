money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 1.05  # Ежемесячный рост цен
count = 0

while True:
    money_capital += salary   #Текущий бюджет на 1-е число
    if money_capital >= spend:    #Сравниваем с затратами
        money_capital -= spend
        spend *= increase
        count += 1
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", count)