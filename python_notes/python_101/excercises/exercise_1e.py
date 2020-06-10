"""  name = input('Whats your name?')
 print("Hello, %s!" %name) """
#----------------------------------------------------------1-----
""" name = input("Whats your name?")
uppername = name.upper()
leng = len(name)
print('Hello, %s! you have %s letters in your name!' % (uppername,leng)) """
#------------------------------------------------------------2---
""" name = input("Enter a name:")
food = input("Enter a food:")
adj = input("Enter Something gross:") 

print("%s went to the Market to buy some %s , but it smelled like %s so he returned it." % (name,food,adj)) """
#----------------------------------------------------------3-----
""" day = int(input('Day (0-6)? '))
week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
print(week[day]) """
#------------------------------------------------------------4---
""" day = int(input('Day (0-6)? '))
week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
if day == 0 or day == 6:
     print("Sleep in")
else:
    print("Go to Work") """
#----------------------------------------------------------5--------
""" c = int(input("Temperature in Celsius?"))
f = (c * 9/5) + 32 
print("%s degrees Fahrenheit" %f) """
#---------------------------------------------------------------6---------
""" num = 0
while num < 10:
    num +=1
    print(num)"""
#--------------------------------------------------------7-------
""" start = int(input("Startng No."))
end = int(input("Ending No."))

while start < end:
    start +=1
    print(start) """
#-----------------------------------------------------------8----
""" print("*****\n"*5) """
#-----------------------------------------------------------9----
""" n = int(input("How big is the square?"))
row = "*"*n 
block = row*n

print((row + "\n") *n) """
#---------------------------------------------------------10------