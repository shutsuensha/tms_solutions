def calculate_days_to_save(N, k):
    result = 0
    cnt = 6
    weeks = 0
    # сколько недель надо маше на покупку, последнюю неделю не считаем
    while True:
        result += cnt * k
        if result > N:
            result -= cnt * k
            break
        weeks += 1
    days = weeks * 7
    # количество дней без учета последней недели + кол-во дней
    while True:
        result += k
        days += 1
        if result >= N:
            return days
    

N = int(input("Введите стоимость телефона: "))
k = int(input("Введите сумму, которую Маша откладывает каждый день: "))
days = calculate_days_to_save(N, k)
print(f"Маша накопит на телефон за {days} дней.")