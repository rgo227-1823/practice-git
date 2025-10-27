# Get a number input
age_str = input("Enter your age: ")

# Convert the string input to an integer for calculations
try:
    age_int = int(age_str)
    next_year_age = age_int + 1
    print(f"Next year, you will be {next_year_age}!")
except ValueError:
    print("That wasn't a valid whole number for age.")