def compare_files(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, \
         open(file2_path, 'r', encoding='utf-8') as file2:
        
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

        if len(file1_lines) != len(file2_lines):
            print("The files do not have the same number of lines.")
            return

        for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines), start=1):
            if line1.strip() != line2.strip():
                print(f"The files differ at line {i}.")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")
                return
        
        print("The files are identical.")

file1_path = 'file1.txt'
file2_path = 'file2.txt'
compare_files(file1_path, file2_path)
