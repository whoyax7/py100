salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен

balance = 0

for i in range(months):
    balance += salary
    balance -= spend
    spend *= increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {abs(balance):.2f}")

