"""
Analysis:
This program calculates an employee's total weekly pay, including
regular pay and overtime pay.

Design (Pseudocode):
1. Prompt the user for hourly wage
2. Prompt the user for regular hours worked
3. Prompt the user for overtime hours worked
4. Calculate regular pay
5. Calculate overtime pay at 1.5 times the hourly wage
6. Calculate total weekly pay
7. Display the total pay
"""

hourly_wage = float(input("Enter the hourly wage: "))
regular_hours = float(input("Enter the total regular hours worked: "))
overtime_hours = float(input("Enter the total overtime hours worked: "))

regular_pay = hourly_wage * regular_hours
overtime_pay = overtime_hours * hourly_wage * 1.5
total_pay = regular_pay + overtime_pay

print("The employee's total weekly pay is $" + str(round(total_pay, 2)))
