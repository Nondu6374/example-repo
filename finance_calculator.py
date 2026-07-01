import math

# Finance Calculators
# Allows the user to calculate investment interest or monthly bond repayments.

# Display the menu options to the user
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
print()
calculator_choice = input('Enter either "investment" or "bond" from the menu above to proceed: ')

# Normalise input to lowercase so capitalisation doesn't matter
calculator_choice = calculator_choice.lower()

# ── INVESTMENT CALCULATOR ──────────────────────────────────────────────────────
if calculator_choice == "investment":

# Gather inputs from the user
deposit_amount = float(input("Enter the amount of money you are depositing: "))
interest_rate = float(input("Enter the interest rate (e.g. enter 8 for 8%): "))
years = float(input("Enter the number of years you plan to invest: "))
interest = input('Enter "simple" or "compound" interest: ').lower()

# Convert percentage to a decimal
r = interest_rate / 100

# Calculate total amount based on interest type
if interest == "simple":
# Simple interest formula: A = P(1 + r*t)
total_amount = deposit_amount * (1 + r * years)

elif interest == "compound":
# Compound interest formula: A = P(1 + r)^t
total_amount = deposit_amount * math.pow((1 + r), years)

else:
print("Invalid interest type. Please enter 'simple' or 'compound'.")
total_amount = None

# Display the result
if total_amount is not None:
print()
print("------------------------------------")
print(f"Interest type: {interest.capitalize()}")
print(f"Deposit amount: R{deposit_amount:,.2f}")
print(f"Interest rate: {interest_rate}%")
print(f"Years invested: {years}")
print(f"Total amount: R{total_amount:,.2f}")
print("------------------------------------")

# ── BOND REPAYMENT CALCULATOR ──────────────────────────────────────────────────
elif calculator_choice == "bond":

# Gather inputs from the user
house_value = float(input("Enter the present value of the house: "))
annual_interest_rate = float(input("Enter the annual interest rate (e.g. enter 7 for 7%): "))
repayment_months = int(input("Enter the number of months to repay the bond: "))

# Calculate the monthly interest rate (i)
# Annual rate is divided by 100 to get a decimal, then divided by 12 for monthly
i = (annual_interest_rate / 100) / 12

# Bond repayment formula: repayment = (i * P) / (1 - (1 + i)^(-n))
monthly_repayment = (i * house_value) / (1 - (1 + i) ** (-repayment_months))

# Display the result
print()
print("------------------------------------")
print(f"House value: R{house_value:,.2f}")
print(f"Annual interest: {annual_interest_rate}%")
print(f"Repayment period: {repayment_months} months")
print(f"Monthly repayment: R{monthly_repayment:,.2f}")
print("------------------------------------")

# ── INVALID CHOICE ─────────────────────────────────────────────────────────────
else:
print("Invalid selection. Please run the program again and enter 'investment' or 'bond'.")