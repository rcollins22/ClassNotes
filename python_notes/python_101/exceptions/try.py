""" Create a program that asks for a number between 10 - 101. 
If the user enters anything that is not a number, or is less than 10 or greater than 101 throw some sort of insult.
If the number is 42 print a very positive message.
If the number is -1 disregaurd the first point and print a message about being a smart person.
Any other print a message that includes the number given.
 """

num = int(input("Hello, please input a number between 10 and 101\n"))
try: 
    num==int(num)          ## TESTS IF THE INPUT IS A NUMBER ###
except ValueError:                  ### ALLOWS ME TO HANDLE THE DIFFERENT VALUES ###
    Print("Are you dumb?\n")
    num = int(input("Please Try Again"))

while num < 10 or num > 101:

    print("Dude, C'mon")
    num = int(input("Please Try Again"))
if num == -1:
        print("Good Job Smarty pants")
        exit()
elif num == 42:
        print("You're Awesome!")
        exit()
print(num)


    #####
