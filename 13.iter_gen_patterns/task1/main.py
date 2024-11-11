def cyclic_sequence(sequence):
    while True:
        for number in sequence:
            yield number


sequence = [1, 2, 3]

generator = cyclic_sequence(sequence)

num_elements = int(input("Enter the number of elements to display: "))

for _ in range(num_elements):
    print(next(generator), end=" ")
print()
