age = input("What is your current age? ")

current_age = int(age)
years = 90 - current_age
days = 365 * years
weeks = 52 * years
months = 12 * years

print(f"You have {days} days, {weeks} weeks, and {months} months left.")