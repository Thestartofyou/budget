def calculate_savings_goal(yearly_goal, monthly_expenses):
    total_expenses = sum(monthly_expenses.values())
    total_savings = yearly_goal - total_expenses
    
    if total_savings <= 0:
        print("Your expenses exceed your savings goal. Consider reducing your expenses.")
    else:
        months = 12
        monthly_savings = total_savings / months
        
        print("Monthly Budget:")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Total Savings: ${total_savings}")
        print(f"Monthly Savings: ${monthly_savings}")
        print("Breakdown of Monthly Expenses:")
        for category, expense in monthly_expenses.items():
            print(f"{category}: ${expense}")


# Monthly expenses
rent = 1200
food = 600
gas = 200

monthly_expenses = {
    "Rent": rent,
    "Food": food,
    "Gas": gas
}

# Yearly savings goal
yearly_goal = 4000

calculate_savings_goal(yearly_goal, monthly_expenses)
