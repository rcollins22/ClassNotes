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

#------------------------------------------------------------------------------------------------------------
""" # 2. Matrix Addition
Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an 
list of lists,Calculate the result of adding the two matrices. The number in each position in the resulting matrix should 
be the sum of the numbers in the corresponding addend matrices.  """

idx=0
final=[]
mtrx1= [[2, -2],
   [5, 3]]
g0,g1=mtrx1

mtrx2=[[4,2],
   [3,1]]
h0,h1=mtrx2

for x in mtrx1:
    for y in g0:
        f0=g0[idx]+h0[idx]
        final.append(f0)
        idx+=1

print(final)
    


#------------------------------------------------------------------------------------------------------------


final=[]
mtrx1= [[2, -2],
   [5, 3]]
g0,g1=mtrx1

mtrx2=[[4,2],
   [3,1]]
h0,h1=mtrx2

for x in range(len(mtrx1)):
    for y in range(len(mtrx1[0])):
        final[x][y]=mtrx1[x][y]+mtrx2[x][y]


#------------------------------------------------------------------------------------------------------------
""" # 3. Matrix Addition II
Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they
 have the same size. """



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

#