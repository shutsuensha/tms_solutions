def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  # Формула для расчета ИМТ
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Недостаточная масса тела"
    elif 18.5 <= bmi < 24.9:
        return "Норма"
    elif 25 <= bmi < 29.9:
        return "Избыточная масса тела"
    else:
        return "Ожирение"

try:
    weight = float(input("Введите ваш вес (в кг): "))
    height = float(input("Введите ваш рост (в метрах): "))
    
    if weight <= 0 or height <= 0:
        raise ValueError("Вес и рост должны быть положительными числами.")

    bmi = calculate_bmi(weight, height)
    
    print(f"Ваш ИМТ: {bmi:.2f}")
    print(f"Категория: {bmi_category(bmi)}")
except ValueError as e:
    print(f"Ошибка ввода: {e}")