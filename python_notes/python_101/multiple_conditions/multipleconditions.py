#Username Input
us_name = input("Please Enter your Username:")
while(len(us_name) > 12 or len(us_name) < 6):
    print("Your Username must be 6 and 12 characters long!")
    us_name = input("\nPlease Enter a VALID Username:")
    
password = input("Hello %s! Please Enter your Password:"  %us_name) #password is set in UN Block, Interpololation is tupled

#Password Block
if(len(password) > 12 or len(password) < 6):
    print("Your password must be between 6 and 12 characters long!")
    password = input("Please Try Again, re-enter a passcode between 6 and 12 numbers")
elif password.isdigit():                                 #Checks if password is all digits
    print("Passwords may not numbers")

pw_confirm = input("Please confirm your password")

if (pw_confirm == password):
    print("confirmed! Welcome!")
else:
    print("Passwords didn't match")

