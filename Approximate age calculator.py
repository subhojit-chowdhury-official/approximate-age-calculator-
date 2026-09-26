"input functions"

print("Follow the Instructions and enter numbers only","Enter your Date of Birth one by one")
dob_year = int(input("Enter year: "))
dob_month = int(input("Enter month: "))
dob_date = int(input("Enter date: "))
print("Enter present date one by one")
present_year = int(input("Enter year: "))
present_month = int(input("Enter month: "))
present_date = int(input("Enter date: "))

"Indian jugad"

jan = 28+31+30+31+30+31+31+30+31+30+31
feb = 31+30+31+30+31+31+30+31+30+31
mar = 30+31+30+31+31+30+31+30+31
apr = 31+30+31+31+30+31+30+31
may = 30+31+31+30+31+30+31
jun = 31+31+30+31+30+31
jul = 31+30+31+30+31
aug = 30+31+30+31
sep = 31+30+31
oct = 30+31
nov = 31
dec = 0

"Calculating age in year and Multiplying that with 365"

age_in_year = present_year - dob_year
age_in_days = (age_in_year + 1)*365

"Calculating leap years between present year and dob year"

i = dob_year
x = 0
for i in range (dob_year,  present_year + 1):
    if i % 4 == 0:
        x+=1
        i+=1
    else:
        i+=1

"Adding the extra leap year days with age in days"

age_in_days = age_in_days + x

"Calculating extra days of present year"

month = present_month
a = 0
if month == 1:
    a = jan
elif month == 2:
    a = feb
elif month == 3:
    a = mar
elif month == 4:
    a = apr
elif month == 5:
    a = may
elif month == 6:
    a = jun
elif month == 7:
    a = jul
elif month == 8:
    a = aug
elif month == 9:
    a = sep
elif month == 10:
    a = oct
elif month == 11:
    a = nov
elif month == 12:
    a = dec
else:
    print("Not valid month entered")

present_month = month

"Calculating extra days of present month"

if present_month in (1,3,5,7,8,10,12):
    b = 31 - present_date
elif present_month in (4,6,9,11):
    b = 30 - present_date
elif present_month == 2:
    b = 28 - present_date
else:
    print("Wront present date entered")

"indian jugad 2.0"

jan = 0
feb = 31
mar = 31+28
apr = 31+28+31
may = 31+28+31+30
jun = 31+28+31+30+31
jul = 31+28+31+30+31+30
aug = 31+28+31+30+31+30+31
sep = 31+28+31+30+31+30+31+31
oct = 31+28+31+30+31+30+31+31+30
nov = 31+28+31+30+31+30+31+31+30+31
dec = 31+28+31+30+31+30+31+31+30+31+30

"Calculating extra days of dob year"

month = dob_month
c = 0
if month == 1:
    c = jan
elif month == 2:
    c = feb
elif month == 3:
    c = mar
elif month == 4:
    c = apr
elif month == 5:
    c = may
elif month == 6:
    c = jun
elif month == 7:
    c = jul
elif month == 8:
    c = aug
elif month == 9:
    c = sep
elif month == 10:
    c = oct
elif month == 11:
    c = nov
elif month == 12:
    c = dec
else:
    print("Not valid month entered")

dob_month = month

"Calculating extra days of dob month"

d = dob_date - 1

"Final output"

age_in_days = age_in_days - (a+b+c+d)
print("Your approximate age is: ",age_in_days)