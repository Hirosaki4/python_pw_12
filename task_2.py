students = {"Іван": 80, "Марія": 95, "Олег": 78, "Анна": 85}

name = input("Введіть ім'я студента: ")

try:
    print(f"Оцінка студента {name}: {students[name]}")
except KeyError:
    print(f"Студента з іменем {name} не знайдено.")
