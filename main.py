from data import cities, HOTEL_FOOD, BUDGET
from itertools import combinations

def evaluate_option(city_data, selected_attractions,budget):
    total_cost = city_data["transport"] + HOTEL_FOOD
    total_time = 0
    total_interest = 0

    for attraction in selected_attractions:
        total_cost += attraction["cost"]
        total_time += attraction["time"]
        total_interest += attraction["interest"]

    if total_cost > budget or total_time > city_data["available_time"]:
        return None  # Option is not feasible

    return {
        "selected_attractions": selected_attractions,
        "total_cost": total_cost,
        "total_time": total_time,
        "total_interest": total_interest
    }

def find_best_for_city(city_data, budget):
    attractions = city_data["attractions"]

    best_option = None

    for r in range(len(attractions) + 1):
        for selected_attractions in combinations(attractions, r):
            option = evaluate_option(city_data, selected_attractions, budget)

            if option is None:
                continue

            if (
                best_option is None
                or option["total_interest"] > best_option["total_interest"]
                or (
                    option["total_interest"] == best_option["total_interest"]
                    and option["total_cost"] < best_option["total_cost"]
                )
                or (
                    option["total_interest"] == best_option["total_interest"]
                    and option["total_cost"] == best_option["total_cost"]
                    and option["total_time"] < best_option["total_time"]
                )
            ):
                best_option = option

    return best_option

def find_best_program(budget):
    best_program = None

    for city_name, city_data in cities.items():
        best_option = find_best_for_city(city_data, budget)
    
        if best_option is None:
            continue

        program = {
            "city": city_name,
            "total_cost": best_option["total_cost"],
            "total_time": best_option["total_time"],
            "total_interest": best_option["total_interest"],
            "selected_attractions": best_option["selected_attractions"]
        }

        if (
            best_program is None
            or program["total_interest"] > best_program["total_interest"]
            or (
                program["total_interest"] == best_program["total_interest"]
                and program["total_cost"] < best_program["total_cost"]
            )
            or (
                program["total_interest"] == best_program["total_interest"]
                and program["total_cost"] == best_program["total_cost"]
                and program["total_time"] < best_program["total_time"]
            )
        ):
            best_program = program

    return best_program


best_program = find_best_program(BUDGET)

#output the best program
print("Лучший вариант:")
print(f"Город: {best_program['city']}")
print("Достопримечательности:")

for attraction in best_program["selected_attractions"]:
    print(f"- {attraction['name']}")

print(f"Стоимость: {best_program['total_cost']} юаней")
print(f"Время: {best_program['total_time']} часов")
print(f"Интерес: {best_program['total_interest']}")