""" #STRINGS AND LISTS CAN BE NESTED TOGETHER IN AN ARRAY      #LISTS CAN BE MADE UP OF OTHER LISTS!!###
atl=['buckhead', 
['krog','westside','o4w'] ,
'hapeville'
]
print(atl[1])    #PRINTS ['krog', 'westside', 'o4w']
print(atl[0])    #PRINTS 'buckhead'

                                                                     #YOU CAN ASSIGN INDEXED ITEMS TO VARIABLES
neighborhoods=atl[1]
print(neighborhoods)  #PRINTS ['krog', 'westside', 'o4w']




#LOOPING THROUGH LISTS of LISTS
atlanta=['atv', 'lenox', 'phipps']
,['piedmont', 'pride', 'vortex']
,['ormsbys', 'marcel', 'terminal']
idx_1=0
for wtd in atlanta:
    idx_2 =0 
    print("%s. %s" % ((idx_1+1),group))

 """

#-----------------------------------------------------------------------------------------------------------------------

""" Create a program that prints the ingredients of your 3 favorite foods. 
The ingredients must be in a list inside of the foods list
Before each food print "Food # X has the following ingredients". Where X is the index of the food.
(Challange) You can only use the for in operation.
(Extra Challenge) Make it a quiz game of guess the food based on its ingredients. Add more food items if needed. """


fav_food=[['Cheesecake','Cheese','Milk','Eggs'],['Cheesesticks','Bread','Mozzerella','Marinara'],['Mochi','Rice Flour', 'Ice Cream','Matcha']]
[cheesecake,cheese_sticks,mochi]=fav_food

for food in fav_food:                                                  
    print('%s has the following ingredients:\n%s' % (food[0],food[1:]))   ##PRINTS: Cheesecake has the following ingredients:
 #                                                                                  ['Cheese', 'Milk', 'Eggs'] etc...



fav_food=[['Cheese','Milk','Eggs'],
    ['Bread','Mozzerella','Marinara'],
    ['Rice Flour', 'Ice Cream','Matcha']]

idx=0
for food in fav_food:
    print("Food #%d has the following ingredients: " % (idx + 1))   #idx IS AN INDEX(base) NUMBER 
    for i in fav_food[idx]:
        print("     %s" % i)
    idx+=1


