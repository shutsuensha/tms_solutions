from functools import reduce

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

# Используем map() для вычисления площади каждой комнаты
areas = map(lambda room: room['length'] * room['width'], rooms)

# Используем reduce() для суммирования всех площадей
total_area = reduce(lambda x, y: x + y, areas)

print(f"Общая площадь квартиры: {total_area:.2f} кв. м.")