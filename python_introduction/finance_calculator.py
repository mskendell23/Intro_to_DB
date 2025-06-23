monthly_income = int(input("Enter your monthly income: "))

monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_savings = int(monthly_income - monthly_expenses)

ProjectedSavings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))


print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $",ProjectedSavings)


