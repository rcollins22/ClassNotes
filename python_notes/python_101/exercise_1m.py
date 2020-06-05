""" 1. Tip Calculator
Your task is to write a program that calculates how much of a tip to leave at a restaurant.
Prompt the user for two things:
The total bill amount
The level of service, which can be one of the following: good, fair, or bad
Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:
good -> 20%
fair -> 15%
bad -> 10% """

try:
    amt = float(input("Please input bill amount\n"))
except ValueError:           ###ALLOWS A RETRY FOR A DOLLAR AMT###
    print("Please enter a dollar amount.\n")
    amt = float(input("Please input bill amount\n"))

srvce_lvl = input("Service level?")

while srvce_lvl == "":

    if srvce_lvl == 'good' or 'Good':
        tip = .2*amt
    elif srvce_lvl == 'Fair' or "fair":
        tip = .15*amt
    elif srvce_lvl == "bad" or 'bad':
        tip = .1*amt
    else:
        print("please enter a valid option.")

print("tip amount: $%s" %tip)
print("Total amount: $%s" %ttl)


