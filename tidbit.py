purchase_price = float(input("Enter the purchase price: "))

down_payment = purchase_price * 0.10
balance = purchase_price - down_payment
monthly_payment = purchase_price * 0.05
annual_rate = 0.12
monthly_rate = annual_rate / 12

month = 1

print("\nMonth  Balance     Interest  Principal  Payment   Remaining")
print("-------------------------------------------------------------")

while balance > 0:
    interest = balance * monthly_rate
    principal = monthly_payment - interest

    if principal > balance:
        principal = balance
        monthly_payment = interest + principal

    balance -= principal

    print(f"{month:<6} ${balance + principal:>9.2f} "
          f"${interest:>8.2f} ${principal:>9.2f} "
          f"${monthly_payment:>8.2f} ${balance:>9.2f}")

    month += 1
