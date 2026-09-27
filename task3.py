from data import cities
from main import find_best_program

for city_data in cities.values():
    for attraction in city_data["attractions"]:
        attraction["time"] *= 1.2

best_program = find_best_program(1800)

print("Лучший вариант после увеличения времени на 20%:")
print("Город:", best_program["city"])

print("Достопримечательности:")
for attraction in best_program["selected_attractions"]:
    print("-", attraction["name"])

print("Стоимость:", best_program["total_cost"], "юаней")
print("Время:", round(best_program["total_time"], 1), "часов")
print("Интерес:", best_program["total_interest"])