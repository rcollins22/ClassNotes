""" 1. Sum the Numbers
Create a list of numbers, print their sum. """

list=[4,5,7,8]
print(sum(list))
#------------------------------------------------------------------------------------------------------------
""" 2. Largest Number
Create a list of numbers, print the largest of the numbers. """

list=[4,8,6,5]
list.sort()
print(list[-1])
#------------------------------------------------------------------------------------------------------------
""" 3. Smallest Number
Create a list of numbers, print the smallest of the numbers. """

list=[4,8,6,5]
list.sort()
print(list[:1])
#------------------------------------------------------------------------------------------------------------
""" Even Numbers
Create a list of numbers, print each number in the list that is even.
 """
list=[4,8,6,5]
for even in list:
    if even % 2 == 0:
        print(even)
#------------------------------------------------------------------------------------------------------------
""" Positive Numbers
Create a list of numbers, print each number in the list that is greater than zero. """
list=[-5,15,2,-7,-3,8]
for good in list:
    if good>0:
        print(good)


#------------------------------------------------------------------------------------------------------------
""" Positive Numbers II
Create a list of numbers, create a new list which contains every number in the given list which is positive. """
list=[-5,15,2,-7,-3,8]
pos=[]
for good in list:
    if good>0:
        pos.append(good)
print(pos)
#------------------------------------------------------------------------------------------------------------
""" Multiply a list
Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the 
first list multiplied by the factor. Print this list. """
list=[5,8,4,6,9]
factor=5
new_list=[]
for mtpl in list:
    final = factor*mtpl
    new_list.append(final)
print(new_list)

#------------------------------------------------------------------------------------------------------------
""" Reverse a String
Given a string, print the string reversed. """

string='rashad'
print(string[::-1])
#------------------------------------------------------------------------------------------------------------

