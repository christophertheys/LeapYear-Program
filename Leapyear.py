# Compulsory Task 2

# Simple program to determine which year is a leap year. A leap year occurs every 4 years

year_entered_by_user = int(input("What year do you want to start with : "))
amount_of_years = int(input("How many years do you want to check : "))
end_index_of_year = year_entered_by_user + amount_of_years

print("\n")

for year_entered_by_user in range(year_entered_by_user, end_index_of_year):
    if year_entered_by_user % 4 == 0:
        print("{} is a leap year".format(year_entered_by_user))
    else:
        print("{} isn't a year year".format(year_entered_by_user))
