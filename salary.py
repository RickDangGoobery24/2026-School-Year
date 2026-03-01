starting_salary = float(input("Enter starting salary: "))
increase_rate = float(input("Enter yearly percentage increase: ")) / 100
years = int(input("Enter number of years: "))

salary = starting_salary

print("\nYear\tSalary")
print("----------------")

for year in range(1, years + 1):
    print(f"{year}\t${salary:,.2f}")
    salary += salary * increase_rate
