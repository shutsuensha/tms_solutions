string = "hhhabchghhh"

first_h_index = string.find('h')
last_h_index = string.rfind('h')

middle_part = string[first_h_index+1:last_h_index].replace('h', 'H')
result = string[:first_h_index+1] + middle_part + string[last_h_index:]

print(f"Result: {result}")