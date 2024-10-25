def write_to_file(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        print("Please enter 6 lines of text:")
        for i in range(6):
            line = input(f"Line {i+1}: ")
            file.write(line + '\n')
    print(f"6 lines have been written to {file_path}")


file_path = 'output.txt'
write_to_file(file_path)
