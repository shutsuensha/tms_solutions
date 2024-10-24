def print_lines(file_path, s1=None, s2=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # a) Print the first line
        if len(lines) >= 1:
            print("a) First line:", lines[0].strip())
        else:
            print("a) The file has less than 1 line.")

        # b) Print the fifth line
        if len(lines) >= 5:
            print("b) Fifth line:", lines[4].strip())
        else:
            print("b) The file has less than 5 lines.")

        # c) Print the first 5 lines
        print("c) First 5 lines:")
        for line in lines[:5]:
            print(line.strip())

        # d) Print lines from s1 to s2 (inclusive)
        if s1 and s2:
            print(f"d) Lines from {s1} to {s2}:")
            for line in lines[s1-1:s2]:
                print(line.strip())

        # e) Print the entire file
        print("e) Entire file content:")
        for line in lines:
            print(line.strip())

file_path = 'a.txt'
s1, s2 = 3, 6  # Example values for lines s1 to s2 (inclusive)
print_lines(file_path, s1, s2)
