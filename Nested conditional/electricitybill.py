# take input of number of units consumed from the user 
units = int(input(" pleasee enter number of units you consumed : "))

# check conditions of units consumed
# Then calculate amount and surcharge accordingly
# surcharge is the tax value

# check for units less than 50
if(units < 50):
    amount = units * 2.60
    surcharge = 25

# check for units less than 100
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

# check for units less than or equal to 200
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

# check for all the cases other than mentioned 
# when units consumed are more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

# calculate and display the total electricity bill
# total amount - amount = surcharge
total = amount + surcharge
print("\nElectricity Bill - %.2f" %total)