# get user input for the initial principal amount
principal = float(input("Enter the initial principal amount (e.g. 1000): "))

# get the annual interest rate
rate = float(input("Enter the annual interest rate as a percentage (e.g. 5): ")) / 100

# get the number of years to compound the interest
years = int(input("Enter the number of years: "))

# calculates balance per year
for year in range (1, years + 1):
    # formula: A = P * (1 + r)
    principal = principal * (1 + rate)
    print(f"Year {year}: Balance = ${principal:.2f}")
