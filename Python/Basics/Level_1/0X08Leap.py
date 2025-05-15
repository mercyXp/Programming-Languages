#leap year
year = int(input("Enter the year: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year")
else:
    print("Not a leap year")




# ✅ A year is a leap year if:
#It is divisible by 4,

#Except for years divisible by 100,

#Unless it is also divisible by 400.

#For example:
#2024 was a leap year (divisible by 4, not by 100)

#2100 is not a leap year (divisible by 100 but not by 400)

#2400 is a leap year (divisible by 400)