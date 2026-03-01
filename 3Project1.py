"""
Analysis:
This program calculates the main user's income tax based on their gross income
and the number of dependents. The final tax amount is rounded to at the most
two decimal places before being displayed.

Design (Pseudocode):
1. Prompt the user for gross income
2. Prompt the user for number of dependents
3. Calculate taxable income
4. Compute tax owed
5. Round the tax to two decimal places
6. Display the result
"""

STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 3000
TAX_RATE = 0.20

gross_income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

taxable_income = gross_income - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * dependents)
tax = taxable_income * TAX_RATE

tax = round(tax, 2)

print("The income tax is $" + str(tax))
