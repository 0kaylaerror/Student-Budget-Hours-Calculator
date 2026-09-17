print("Let's estimate your weekly work hours based on your monthly budget!") #Welcome Message
Hourly = float(input("What's your hourly wage? $"))        #Storage Information                 
Rent = float(input("Rent(Housing Contribution): $"))
Internet_Service = float(input("Internet Service(Phone Plan): $"))
Groceries = float(input("Groceries: $"))
Fun = float(input("Fun Allowance(Leisure Spending): $"))

Total_Exp = round((Rent + Internet_Service + Groceries + Fun),2) #Calculations
Hours = round((Total_Exp / Hourly)/4,1)
Total_SH = round((((Total_Exp + 100)/4)/19),1) #Weekly hours with $100
Saving_H = round((Total_SH / Hourly)/4,1)

Hourly = str(Hourly)       #Conversion of inputs to str for near future strings
Rent = str(Rent)
Internet_Service = str(Internet_Service)
Groceries = str(Groceries)
Fun = str(Fun)

Total_Exp = str(Total_Exp) #Convert to str for + sign instead of comma in near future strings
Hours = str(Hours)
Total_SH = str(Total_SH)
Saving_H = str(Saving_H)

print("Your hourly wage is $" + Hourly)
print("Monthly Expenses;")
print("Rent(Housing Contribution) $" + Rent )
print("Internet Service(Phone Plan) $" + Internet_Service)
print("Groceries $" , Groceries)
print("Fun Allowance(Leisure Spending) $" + Fun)
print("Your total monthly expenses cost $" + Total_Exp)
print("Hours per week require to break even: " , Hours , "Hours")
print("Hours per week required to save $100 per month:", Total_SH , "Hours")

print("As your hourly wage is", Hourly , "your total monthly expenses cost $" + Total_Exp ,
". To cover these expenses, you'd have to work", Hours ,
"hours per week to break even, and to save $100 per month you'd need to work"
, Total_SH ,"hours.")

#The values I’ve used to test my program were “Hourly, Rent, Total_Exp,Total_S,Saving_H,” etc.
# I verified the calculations by doing them on my calculator first and then making sure the same --
# answer was given for the different tests. I would say it wasn’t as if I didn’t have to think, 
# but it was very off the top of my head in under an hour and then making correction while --
# seeing the syntax or type errors I had, so it wasn’t difficult or truly challenging..