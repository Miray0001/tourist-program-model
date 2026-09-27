from data import cities, HOTEL_FOOD 
from main import find_best_program

budgets = range(1500, 2101)
results = []

for budget in budgets: 
    best_program = find_best_program(budget) 
    results.append({ "budget": budget,
                     "city": best_program["city"], 
                     "total_cost": best_program["total_cost"], 
                     "total_time": best_program["total_time"], 
                     "total_interest": best_program["total_interest"], 
                     "selected_attractions": best_program["selected_attractions"] }) 


print("\nИзменение города:")

previous_city = None

for result in results:
    current_city = result["city"]

    if current_city != previous_city:
        print(
            "Бюджет:", result["budget"],
            "| Город:", result["city"],
            "| Интерес:", result["total_interest"]
        )

        previous_city = current_city


print("\nИзменение оптимальной программы:")

previous_program = None

for result in results:
    current_program = (
        result["city"],
        result["selected_attractions"]
    )

    if current_program != previous_program:
        print("\nБюджет:", result["budget"])
        print("Город:", result["city"])
        print("Стоимость:", result["total_cost"])
        print("Время:", result["total_time"])
        print("Интерес:", result["total_interest"])
        print("Достопримечательности:")

        for attraction in result["selected_attractions"]:
            print("-", attraction["name"])

        previous_program = current_program