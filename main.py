a = 10
b = 5
c = 3

# Sum
sum_value = a + b + c

# Difference
difference_value = a - b - c

# Product
product_value = a * b * c

# Subtract second from first and add third
result_1 = a - b + c

# Divide product of two variables by the third
if c != 0:
    result_2 = (a * b) / c
else:
    result_2 = "Cannot divide by zero"

# Remainder of the sum of the first two variables divided by the third
if c != 0:
    result_3 = (a + b) % c
else:
    result_3 = "Cannot divide by zero"

print(f"Sum: {sum_value}, Difference: {difference_value}, Product: {product_value},")
print(f"Result 1: {result_1}, Result 2: {result_2}, Result 3: {result_3}")