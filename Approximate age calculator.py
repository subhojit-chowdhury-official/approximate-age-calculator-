#Approximate age Calculator

#intro

print("Its a approximate age calculator which converts your age into days.....its made by a beginner python programmer Named Subhojit chowdhury....dont trust blindly its says approximate values")

#Input Category

print("Enter your DOB")

dob_year = int(input("Enter year:" ))
dob_month = int(input("Enter month:" ))
dob_day = int(input("Enter day:" ))

print("Enter Present date")

present_year = int(input("Enter year:"))
present_month = int(input("Enter month:"))
present_day = int(input("Enter day:"))

#Age Calculation In year

age_in_year = present_year - dob_year

#Multiplication with 365

total_days = age_in_year*365

#Find how many leap years between dob_year & present_year & add it in total days

for i in range(dob_year , present_year  + 1):
    if i % 400 == 0:
        total_days = total_days + 1
    else:
        i+=1

#add the extra days after recent birth day


if dob_month < present_month:
    month = present_month - dob_month
    total_days = total_days + (month * 30)
elif dob_month > present_month:
    month = dob_month - present_month
    total_days = total_days + (month * 30)
elif dob_month == present_month:
    total_days = total_days
else:
    print ("wrong input")

#final output

print("Your approximate age is: ",total_days)
