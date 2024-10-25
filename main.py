def calculate_monthly_payment(s, i, n):
    # Годовая процентная ставка i переводится в месячную
    p = i / 12 / 100
    # Формула расчета ежемесячной выплаты
    m = s * p * (1 + p)**n / ((1 + p)**n - 1)
    return m

def calculate_total_payment(m, n):
    # Общая сумма выплат
    return m * n

def calculate_overpayment(total_payment, s):
    # Переплата
    return total_payment - s

# Ввод данных от пользователя
s = float(input("Введите сумму займа (s): "))
i = float(input("Введите годовую процентную ставку (i) в %: "))
n = int(input("Введите количество месяцев (n): "))

# Расчет ежемесячной выплаты
monthly_payment = calculate_monthly_payment(s, i, n)

# Общая сумма выплат и переплата
total_payment = calculate_total_payment(monthly_payment, n)
overpayment = calculate_overpayment(total_payment, s)

# Вывод результатов
print(f"\nЕжемесячная выплата: {monthly_payment:.2f}")
print(f"Общая сумма выплат: {total_payment:.2f}")
print(f"Переплата: {overpayment:.2f}")