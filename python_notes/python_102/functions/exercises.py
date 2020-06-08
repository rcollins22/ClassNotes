""" 1. Madlib function
Write a function that accepts two arguments: a name and a subject.The function should return a 
String with the name and subject interpolated in. Provide default arguments in case one or both are omitted.
 """

#x=input('Verb:')
#y=input('Noun:')
def madlib(x,y):
    ##IF VERB IS LEFT EMPTY REPLACE WITH 'POP'##
    if x == '':
        x=='Pop'
    ##IF NOUN IS LEFT EMPTY RREPLACE WITH WEASEL##
    elif y =='':
        y = "Weasel" 
    print('%s goes the %s' % (x,y))
        
#madlib(x,y)
 
 #---------------------------------------------------------------------------------------------------------------------------
""" Celsius to Fahrenheit conversion
The formula to convert a temperature from Celsius to Fahrenheit is: F = (C * 9/5) + 32
Write a function that takes a temperature in Celsius, converts it Fahrenheit, and returns the value. """

#c=int(input('Enter temp in C:'))
def converter(c):
    f=((c)* 9/5) + 32
    print('The temp in Fahrenheit is %s' %f)

#converter(c)

##FOR CONVERTING TO FAHRENHEIT##
#f=int(input('Enter temp in F:'))
def converter(f):
    c= (f-32)*(5/9)
    print('The temp in Celsius is %s' %c)

#converter(f)

#---------------------------------------------------------------------------------------------------------------------------
def is_even():
    n=int(input("input a number"))
    if n % 2 == 0:
        print('EVEN!!')
    else:
        print('ODD')

#is_even()

def is_odd():
    ##RUNS THE EXACT SAME FUNCTION AS ABOVE (LINE 40)##
    is_even()

#is_odd()
#---------------------------------------------------------------------------------------------------------------------------
""" Write a function that accepts a List of numbers as an argument.
Return a new List that includes the only the even numbers. """
final=[]
def give_even(lst): 
    for num in lst:
        if num % 2==0:
            ##PUSHES ALL EVEN NUMBERS TO EMPTY 'FINAL' LIST##
            final.append(num)
    print(final)
give_even([24,33,1,89,54,24,16])
#---------------------------------------------------------------------------------------------------------------------------
""" Write a function that accepts a List of numbers as an argument.
Return a new List that includes the only the odd numbers. """
final=[]
def is_odd(lst):
    for num in (lst):
        if num % 2 != 0:
            ##PUSHES ALL ODD NUMBERS TO EMPTY 'FINAL' LIST##
            final.append(num)
    print(final)
is_odd([24,33,1,89,54,24,16])
#---------------------------------------------------------------------------------------------------------------------------
""" Write a function smallest that accepts a List of numbers as an argument.
It should return the smallest number in the List.  Complete one for the largest as well"""
def smallest(lst):
    ##CREATES A VARIABLE 'SORT' THAT CONTAINS THE SORTED LIST OOF ITEMS##
    sort=sorted(lst)
    ##PRINTS THE FIRST ELEMENT IN THE NEW SORTED LIST##
    print(sort[0])

def largest(lst):
    ##CREATES A VARIABLE 'SORT' THAT CONTAINS THE SORTED LIST OOF ITEMS##
    sort=sorted(lst)
    ##PRINTS THE LAST ELEMENT IN THE NEW SORTED LIST##
    print(sort[-1])


smallest([24,33,1,89,54,24,16])
largest([24,33,1,89,54,24,16])
#---------------------------------------------------------------------------------------------------------------------------


strng=input('Enter a Sentence:\n')
def shortest_string():
    ##SPLITS STRING INTO LIST OF WORDS##
    manip=strng.split()
    print(manip)
    ##SORTS LIST LIST BY LENGTH OF EACH ITEM##
    manip=sorted(manip, key=len)
    ##PRINTS THE FIRST ELEMENT IN THE NEW SORTED LIST##
    print(manip[0])

shortest_string()

def longest_string():
    #SPLITS STRING INTO LIST OF WORDS##
    manip=strng.split()
    print(manip)
    ##SORTS LIST LIST BY LENGTH OF EACH ITEM##
    manip=sorted(manip, key=len)
    ##PRINTS THE LAST ELEMENT IN THE NEW SORTED LIST##
    print(manip[-1])

longest_string()
#---------------------------------------------------------------------------------------------------------------------------
def move(board,location,player):
    board=[['','',''],
        ['','',''],
        ['','','']]
    location=()
 #---------------------------------------------------------------------------------------------------------------------------
""" Using functions write a program that will write a random sentence like 'The [noun][verb] the [noun]' from a dictionary of 
lists of nouns and verbs. (IE "The house ate the cat" where 'house' and 'cat' are in a noun list and 'ate' is in a verb list.)
Make it print several sentense that are seperated by "Also, ..."(Challange ) Using recursion, have it wait for user input to go
onto the next randon sentence. (Look recursion in the learning portal or online) (you may have to do ctrl-c to exit)
(Extra Challange) Have it where the user can enter "quit", "q", or "exit" and it will leave the program. """

import random
import pickle
wrds= {
    'Nouns' : ['cat','zombie','dog','moose','hacker','priest','cowboy','guinea pig','bird','tiger'] ,
    'Verbs' : ['ran','crawled', 'trotted','danced','twerked', 'moonwalked','crip walked',] ,
    'Vehicle' : ['wheelchair','motorbike','horse','unicycle','bird scooter','skateboard','giraffe'] ,
    'Pronouns' : ['Elon Musk','Ronald Mcdonald','Carol Baskin','Joe Exotic','Rick Sanchez', 'Beyonce','Snoop Dogg']  
}
input('\n\nIm JokeBot 2000.\n\nPress Enter to Generate a Laugh:\n')
#print(joke)
def joke_bot2000():
    for person in wrds['Pronouns']:
        ##SET RANDOM VARIABLES IN LOOP TO GENERAGE NEW JOKE EACH LOOP## 
        r_noun=random.choice(wrds['Nouns'])
        r_veh=random.choice(wrds['Vehicle'])
        r_verb=random.choice(wrds['Verbs'])
        protag=random.choice(wrds['Pronouns'])
        ##ACTUAL JOKE I INTEND ON SAVING AS A JSON OR PICKLE###
        joke = ("""\n\n %s and their best friend, who just so happens to be a %s BTW,
 
were walking down the street one day when they noticed that there were girl scouts selling cookies just ahead.

knowing they had just started their diet they quickly %s away in the other direction. 

But the girls were NOT taking no for an answer.

In quite the panic, they quickly hopped on a %s and sped off as fast as they could!\n\n\nBut did you know...""" % (protag,r_noun,r_verb,r_veh))
        ##PRINTS FINAL JOKE##
        print(joke)
        QUIT=input("Push enter to continue or q to quit")
    ##QUIT FUNTCIONALITY##
    if QUIT == 'q' or 'Q':
        exit()
    else:
    ##LOOPS JOKES W/ RECURSION##
        joke_bot2000()

joke_bot2000()

