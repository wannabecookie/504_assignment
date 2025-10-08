import sys

def calculate_annual_earnings(monthly_earnings):
    yr_earnings = monthly_earnings * 12
    return yr_earnings


# Sub-function to calculate total annual spending
def calculate_annual_spending(monthly_spendings):
    yr_spending  = monthly_spendings * 12
    return yr_spending
    

# Sub-function to calculate net annual savings
def calculate_net_savings(annual_earnings, annual_spending):
    net_saving = annual_earnings - annual_spending
    return net_saving
    

# Main function to calculate total retirement savings
def calculate_retirement_savings(current_age, retirement_age, monthly_earnings, monthly_spending):
    yr_till_retired = retirement_age - current_age
    annual_earning = calculate_annual_earnings(monthly_earnings)
    annual_spending = calculate_annual_spending(monthly_spending)
    annual_net_saving = calculate_net_savings(annual_earning, annual_spending)
    retirement_savings = yr_till_retired * annual_net_saving
    return retirement_savings
    

current_age = int(sys.argv[1])
retirement_age = int(sys.argv[2])
monthly_earnings = float(sys.argv[3])
monthly_spending = float(sys.argv[4])

total_savings = calculate_retirement_savings(current_age, retirement_age, monthly_earnings, monthly_spending)

# Calculate and print the total savings by retirement
print(f"Total savings by retirement (age {current_age} to {retirement_age}): ${total_savings:,.2f}")
