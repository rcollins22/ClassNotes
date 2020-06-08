
# """ # 1. Phonebook dictionary
# Given the following dictionary, representing a mapping from names to phone numbers:"""
# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# } 
# """ 
# Write code to do the following:

# Print Elizabeth's phone number.
# Add an entry to the dictionary: Kareem's number is 938-489-1234.
# Delete Alice's phone entry.
# Change Bob's phone number to '968-345-2345'.
# Print all the phone entries. """

# print(phonebook_dict.get('Elizabeth'))

# phonebook_dict['Kareem']=['938-489-123']

# del phonebook_dict['Alice']

# phonebook_dict['Bob']=['968-345-2345']


# print(phonebook_dict)
# #-------------------------------------------------------------------------------------------------------------

# """ # 2. Nested dictionaries
# Given the following dictionary:"""
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# } 
# """
# Write a python expression that gets the email address of Ramit.
# Write a python expression that gets the first of Ramit's interests.
# Write a python expression that gets the email address of Jasmine.
# Write a python expression that gets the second of Jan's two interests. """

# print(ramit['email'])

# print(ramit['interests'][0])

# jas= ramit['friends'][0]
# print(jas['email'])

# jan=ramit['friends'][1]
# print(jan['interests'][1])


# #----------------------------------------------------------------------------------------------------------

# """ # 3. Friend counter
# Using the dictionary from the Nested dictionaries exercise above, write a function countFriends() that accepts a 
# dictionary as an argument and returns a new dictionary that includes a new key """ 

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friendss': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }, 'hi'
#   ]
# } 
# def countFriends(ramit):
#     ramit['total friends']=len(['friendss'])
#     print(ramit)


# countFriends(ramit)
# #------------------------------------------------------------------------------------------------------------
# """ 1. Letter Summary
# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the 
# tally of how many times each letter in the alphabet was used in the word. """

answer={}

def letter_counter():
    word=input('Please input a word:\n')
    for x in word:
        if x in answer:
            answer[x]+=1
        else:
            answer[x]=1
    print(answer)

letter_counter()
# #-----------------------------------------------------------------------------------------------------------------
# """ Word Summary
# Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing 
# the tally of how many times each word in the alphabet was used in the text. """


# occur = {}

# def word_counter():
#     input_string = input('Enter a sentence:\n')
#     words=input_string.split()
#     for word in words:
#         if word in occur:
#             occur[word] +=1
#         else: 
#            occur[word] =1
#     print(occur)
            
# word_counter()
#---------------------------------------------------------------------------------------------------------------------------------
""" Sorting a histogram
Given a histogram tally (one returned from either letter_histogram or word_histogram), print the top 3 words or letters. """

#dictionary = {'D': 1, 'i': 2, 'g': 1, 't': 2, 'a': 2, 'l': 1, 'C': 1, 'r': 1, 'f': 1, 's': 1}
#cge=list(dictionary)

##CREATED SINGLE USE FUNCTION USING LAMBDA TO MAKE SWITCH THE VALUES OF THE OBJECTS##
sort_orders = sorted(answer.items(), key=lambda x: x[1], reverse=True)
top3 = sort_orders[:3]
for x in top3:
    print(x[0], x[1])


print(sort_orders)

#---------------------------------------------------------------------------------------------------------------------------------
