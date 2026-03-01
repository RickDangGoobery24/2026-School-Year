initial_population = int(input("Enter the initial population: "))
growth_rate = float(input("Enter the growth rate: "))
growth_period = int(input("Enter the number of hours to achieve the growth rate: "))
total_hours = int(input("Enter the total number of hours of growth: "))

population = initial_population
cycles = total_hours // growth_period

for _ in range(cycles):
    population *= growth_rate

print(f"Predicted population after {total_hours} hours: {int(population)}")
