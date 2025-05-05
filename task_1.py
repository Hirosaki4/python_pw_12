cities = ["Київ", "Одеса", "Львів", "Харків", "Житомир"]
city_set = set(cities)

for city in ["Одеса", "Полтава"]:
    if city in city_set:
        print(f"{city} присутнє у списку.")
    else:
        print(f"{city} відсутнє у списку.")
