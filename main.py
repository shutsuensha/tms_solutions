class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Ошибка: Деление на ноль."

def get_operation():
    operations = ('+','-','*','/')

    while True:
        operation = input("Введите операцию (+, -, *, /): ")
        if operation in operations:
            return operation
        else:
            print("Неверная операция. Попробуйте снова.")

def main():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        operation = get_operation()

        calculator = Calculator(num1, num2)

        result = 0
        if operation == '+':
            result = calculator.add()
        elif operation == '-':
            result = calculator.subtract()
        elif operation == '*':
            result = calculator.multiply()
        elif operation == '/':
            result = calculator.divide()

        print(f"Результат: {result}")
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите числовые значения.")

if __name__ == "__main__":
    main()