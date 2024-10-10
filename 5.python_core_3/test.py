def calculate_days_to_save(N, k):
    # Маша откладывает деньги только 6 дней в неделю
    weekly_savings = k * 6  # Сумма, которую Маша откладывает за неделю

    # Количество полных недель и остаток
    full_weeks = N // weekly_savings
    remaining_amount = N % weekly_savings

    # Количество дней до накопления всей суммы
    total_days = full_weeks * 7  # Каждый цикл недели включает 7 дней (с воскресеньем)

    # Если остаток больше нуля, считаем, сколько дней дополнительно потребуется
    day = 0
    while remaining_amount > 0:
        remaining_amount -= k
        day += 1

        # Если доходим до воскресенья (7-й день), перескакиваем на новый цикл недели
        if day % 7 == 0:
            day += 1

    return total_days + day

# Пример использования:
N = int(input("Введите стоимость телефона: "))
k = int(input("Введите сумму, которую Маша откладывает каждый день: "))
days = calculate_days_to_save(N, k)
print(f"Маша накопит на телефон за {days} дней.")
