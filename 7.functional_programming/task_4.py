import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запоминаем время начала
        result = func(*args, **kwargs)  # Выполняем декорируемую функцию
        end_time = time.time()  # Запоминаем время окончания
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

# Пример использования
@time_it
def example_function():
    time.sleep(1)  # Задержка в 1 секунду для демонстрации
    return "Функция завершена"

result = example_function()
print(result)