def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def print_fibonacci_sequence(n):
    sequence = [fibonacci_recursive(i) for i in range(1, n+1)]
    print("Последовательность Фибоначчи:")
    print(" ".join(map(str, sequence)))


n = int(input("Сколько чисел Фибоначчи вы хотите вывести? "))
print_fibonacci_sequence(n)