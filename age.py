from datetime import datetime

# Get current year
current_year = datetime.now().year

# Ask user for input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculate year when user will turn 100
year_when_100 = current_year + (100 - age)

# Output result
print(f"Hello {name}! You will turn 100 years old in the year {year_when_100}.")

