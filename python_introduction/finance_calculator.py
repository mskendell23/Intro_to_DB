MonthlyIncome = int(input("Enter your monthly income: "))

MonthlyExpenses = int(input("Enter your monthly expenses: "))

MonthlySavings = int(MonthlyIncome - MonthlyExpenses)

ProjectedSavings = int(MonthlySavings * 12 + (MonthlySavings * 12 * 0.05))


print("Your monthly saving are $", MonthlySavings)
print("Projected savings after one year, with interest, is: $",ProjectedSavings)


