import json
import csv
import os

# Paths for JSON and CSV files
json_file_path = 'employees.json'
csv_file_path = 'employees.csv'

# 1. Read JSON data from file
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 2. Convert JSON to CSV
def json_to_csv(json_data, csv_file_path):
    # Check if JSON data is empty
    if not json_data:
        print("No data to convert.")
        return
    
    # Extract CSV header from the first employee entry
    csv_header = list(json_data[0].keys())
    
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_header)
        writer.writeheader()
        writer.writerows(json_data)

    print(f"Data has been written to {csv_file_path}.")

# 3. Save data to CSV
def save_csv(file_path, data, mode='a'):
    fieldnames = data.keys()

    file_exists = os.path.exists(file_path)

    with open(file_path, mode, newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists or mode == 'w':
            writer.writeheader()
        writer.writerow(data)

    print(f"Employee data saved to {file_path}.")

# 4. Add a new employee to JSON file
def add_employee_to_json(file_path):
    employee = input_employee_data()

    # Read existing data from JSON file
    data = read_json(file_path)

    # Append new employee data
    data.append(employee)

    # Save updated data to JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print(f"New employee added to {file_path}.")

# 5. Add a new employee to CSV file
def add_employee_to_csv(file_path):
    employee = input_employee_data()
    save_csv(file_path, employee)

# Helper function to input employee data
def input_employee_data():
    name = input("Enter name: ")
    birthday = input("Enter birthday (DD.MM.YYYY): ")
    height = float(input("Enter height (in cm): "))
    weight = float(input("Enter weight (in kg): "))
    car = input("Does the employee own a car? (yes/no): ").strip().lower() == 'yes'
    languages = input("Enter programming languages (comma-separated): ").split(',')

    return {
        'name': name,
        'birthday': birthday,
        'height': height,
        'weight': weight,
        'car': car,
        'languages': [lang.strip() for lang in languages]
    }

# 6. Search for an employee by name
def search_employee_by_name(json_data):
    name = input("Enter the name of the employee to search: ").strip()
    for employee in json_data:
        if employee['name'].lower() == name.lower():
            print(f"Found employee: {employee}")
            return
    print("Employee not found.")

# 7. Filter employees by programming language
def filter_by_language(json_data):
    language = input("Enter the programming language to filter by: ").strip().lower()
    filtered_employees = [emp for emp in json_data if language in [lang.lower() for lang in emp['languages']]]
    
    if filtered_employees:
        print(f"Employees who know {language}:")
        for employee in filtered_employees:
            print(employee)
    else:
        print(f"No employees found who know {language}.")

# 8. Filter employees by birth year and calculate average height
def filter_by_birth_year_and_avg_height(json_data):
    try:
        year = int(input("Enter the birth year to filter by: "))
    except ValueError:
        print("Invalid year format.")
        return

    filtered_employees = []
    for employee in json_data:
        birth_year = int(employee['birthday'].split('.')[-1])
        if birth_year < year:
            filtered_employees.append(employee)

    if not filtered_employees:
        print(f"No employees found born before {year}.")
        return

    total_height = sum([emp['height'] for emp in filtered_employees])
    avg_height = total_height / len(filtered_employees)

    print(f"Average height of employees born before {year}: {avg_height:.2f} cm")

# 9. Interactive menu
def interactive_menu():
    while True:
        print("\n--- Employee Management Menu ---")
        print("1. Convert JSON to CSV")
        print("2. Add new employee to JSON")
        print("3. Add new employee to CSV")
        print("4. Search employee by name")
        print("5. Filter employees by programming language")
        print("6. Filter employees by birth year and average height")
        print("7. Exit")

        choice = input("Select an option (1-7): ")

        if choice == '1':
            json_data = read_json(json_file_path)
            json_to_csv(json_data, csv_file_path)
        elif choice == '2':
            add_employee_to_json(json_file_path)
        elif choice == '3':
            add_employee_to_csv(csv_file_path)
        elif choice == '4':
            json_data = read_json(json_file_path)
            search_employee_by_name(json_data)
        elif choice == '5':
            json_data = read_json(json_file_path)
            filter_by_language(json_data)
        elif choice == '6':
            json_data = read_json(json_file_path)
            filter_by_birth_year_and_avg_height(json_data)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    interactive_menu()
