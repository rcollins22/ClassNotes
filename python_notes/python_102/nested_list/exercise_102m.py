""" 1. Multiply Vectors
Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in 
corresponding positions in the two lists. Example:
 """
idx=0
list_a=[2, 4, 5]
list_b=[2, 3, 6]
list_c=[]
for x in list_a:
    pop=list_a[idx]*list_b[idx]
    list_c.append(pop)
    idx+=1
print(list_c)
#------------------------------------------------------------------------------------------------------------
""" # 2. Matrix Addition
Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an 
list of lists,Calculate the result of adding the two matrices. The number in each position in the resulting matrix should 
be the sum of the numbers in the corresponding addend matrices.  """

mtrx_1 = [
    [1, 3],
    [2, 4]
]
mtrx_2 = [
    [5, 2],
    [1, 0]
]
print(str(mtrx_1[0][0] + mtrx_2[0][0]) + ' ' + str(mtrx_1[0][1] + mtrx_2[0][1]))
print(str(mtrx_1[1][0] + mtrx_2[1][0]) + ' ' + str(mtrx_1[1][1] + mtrx_2[1][1]))
    

#------------------------------------------------------------------------------------------------------------
""" # 3. Matrix Addition II
Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they
 have the same size. """

ar1= [[2,3,6,7,2,6] , 
     [5,2,6,5,3,1], 
     [4,5,7,1,8,3]]
                                                                               
ar2=[[3,6,1,7,8,5] , 
    [2,6,4,8,3,5],
    [6,2,1,8,3,9]]                            
result=[]
i=0                                                                            

while i <len(ar1):
   send_result=[]                                                
   c=0
   while c<len(ar1[0]):
      send_result.append(ar1[i][c]+ar2[i][c])                  
      c+=1                                                  
   i+=1                                                          
   result.append(send_result)                                   
print(result)       

#------------------------------------------------------------------------------------------------------------
""" # 4. De-dup
Given a list of numbers or strings, create a new list containing the same elements as the first list, except with
any duplicate values removed. Print the list. """


#------------------------------------------------------------------------------------------------------------
""" # 5. Leetspeak
Given a paragraph of text as a String, print the paragraph in leetspeak. To translate a String to leetspeak, 
you need to replace make the following character replacements (treat all input characters as uppercase): Letter 
Translates To 
Example: If your program is given the String "I am a leet programmer", it should print "1 4m 4 l337 pr0gr4mm3r" 
as the leetspeak translation """


my_string='Blockchain is the key to the future. Blockchain has several utilizations for our future and you guys should get ahead!!'
my_string.replace('a','4')
my_string.replace('e','3')
my_string.replace('g','6')
my_string.replace('i','4')
my_string.replace('o','0')
my_string.replace('s','5')
my_string.replace('t','7')
# A	4
# E	3
# G	6
# I	1
# O	0
# S	5
# T	7
print(my_string)


#------------------------------------------------------------------------------------------------------------
""" # 6. Long-long Vowels
Given a word as a string, print the result of extending any long vowels to the length of 5.
Examples:
Good => Goooood
Cheese => Cheeeeese
Man => Man 
Spoon => Spooooon"""


#------------------------------------------------------------------------------------------------------------
# 7. Caesar Cipher
""" Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? Learn about it here.
Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq" """

