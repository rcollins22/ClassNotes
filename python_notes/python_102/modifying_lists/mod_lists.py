# desc = ['mean', 'rude', 'bitter', 'sad']
# print(desc)

# desc[1]='Nice'          #CHANGES MEAN TO NICE
# desc[3]= 'Happy'        #CHANGES SAD TO HAPPY.

# print(desc)

#------------------------------------------------------------------------------------------------------------
# car_parts = ['windshield', 'seatbelt' , 'tires', 'door', 'hubcap']
# print(car_parts)

# mods = ['turbo', 'rims']

# print(car_parts[1:3])       #PRINTS SEATBELT, TIRES

# car_parts[1:3]=mods         #REPLACES SEATBELT/TIRES WITH TURBO/RIMS
# print(car_parts)
#------------------------------------------------------------------------------------------------------------
# parts = ['windshield', 'seatbelt' , 'tires', 'door', 'hubcap']
# parts.append('trunk')                     #APPEND ADDS ITEM TO END OF LIST
# print(parts)                       # PRINTS['windshield', 'seatbelt', 'tires', 'door', 'hubcap', 'trunk']


# parts.extend(['motor', 'muffler'])   #EXTEND ADDS ITEMS TO END OF LIST
# print(parts)         #PRINTS ['windshield', 'seatbelt', 'tires', 'door', 'hubcap', 'trunk', 'motor', 'muffler']

#------------------------------------------------------------------------------------------------------------
# cparts=[           #LISTS CAN BE VERTICAL W/ INDENTATION
#     'tires',
#     'cap',
#     'oil',
#     'gas tank'
# ]
# print(cparts)

# dparts = cparts + ['nitrus']     #NEW LIST PRINTS ['tires', 'cap', 'oil', 'gas tank', 'nitrus']
# print(dparts)

#------------------------------------------------------------------------------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphalist = list(alphabet)
alphalist[0] = "4"

print(alphalist)

alphabet = "".join(alphalist)
print(alphabet)





#------------------------------------------------------------------------------------------------------------

""" Create a program that asks for several numbers from a user and then adds them up. You must use a List.

After the user enters a number it prints all the numbers the user has entered and ask for another number to be entered.
Let the user know if they enter 0 it will do the addition. Then when they push enter it does the addition and prints the results.
(Challenge) You cannot use an if statement.
(Extra Challange)The only variables allow are "number", "numbers", and "result" (IE only 3 variables allowed and they are all named those specific things)
(Extra Extra) do not have the List print with the 0 at the end of the list. """

num=None
numbers = []
result=[]

while num != 0:
    try:
        num = int(input("\nPlease enter a number.\nBy inputting zero you will run your calculations:\n"))
    except ValueError:
        print("numbers only please!")
        num = int(input("\nPlease enter a number.\nBy inputting zero you will run your calculations:\n"))
    except TypeError:
        print("Thats not a number")
        num = int(input("\nPlease enter a number.\nBy inputting zero you will run your calculations:\n"))
    numbers.append(num)
    print("\nyour number(s) are %s." % numbers)
while num==0:
    result=sum(numbers)
    print("\nZero was entered so we tallyed up your score. Your magic number is:\n %d\n" % result)
    exit()
    

