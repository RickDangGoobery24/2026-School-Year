"""
Analysis:
This program calculates the total number of minutes in a given number
of years provided by the user.

Design (Pseudocode):
1. Prompt the user for the number of years
2. Convert years to days
3. Convert days to minutes
4. Display the total number of minutes
"""

years = int(input("Enter the number of years: "))

minutes_per_year = 365 * 24 * 60
total_minutes = years * minutes_per_year

print("The number of minutes in", years, "years is", total_minutes)
