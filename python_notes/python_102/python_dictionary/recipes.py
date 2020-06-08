""" Create a program that will present a list (only in the visual sense) of recipies with an identifier of some sort 
in front of the recipe name. (1,2,3, or a,b,c etc) When the user inputs that identifer it presents the recipe.
Make at least three recipies (they can be totally imaginary if you want.) Everything that is printed related to a 
recipie must all be contained in a single dictionary. (instructions to users does not have to be in the dictionary)

(Challange) Make it where you can go back to the main menu.

(Extra Challange) Make it where the recipies have instructions and you can step through the instructions. """
#---------------------------------------------------------------------------------------------------------------------------
food={
    'F1': {'Name':'Fried Rice', 'Ingredients':[
        {'Item':'White Rice', 'Amount': '4 Cups'} , 
        {'Item':'Mixed Veggies', 'Amount': '1 Cup'},
        {'Item':"Soy Sauce", 'Amount':'4 Tbsp'}]#,
    #"Directions": 'Boil rice and Refridgerate'
        },
    'F2':{'Name':'Cheesesticks', 'Ingredients': [
        {'Item':'Mozzerella Cheese','Amount':'1lb'},
        {'Item': 'Bread Crumbs','Amount':'2 Cups'},
        {'Item': 'Whole Eggs', 'Amount':2}]#,
        #"Directions":'Freeze cheese overnight.'
        },
    'F3':{'Name':"Mac N' Cheese" ,'Ingredients': [
        {'Item':'Cheddar Cheese','Amount':'1lb'},
        {'Item': 'Elbow Pasta','Amount':'1lb'},
        {'Item': 'Milk', 'Amount':'2 Cups'}]#,
        #Directions: "Bring water to boil"
    }
}
f1_name= food['F1']['Name']
f2_name= food['F2']['Name']
f3_name= food['F3']['Name']
f1=food['F1']
f2=food["F2"]
f3=food['F3']


#def recipe_log():
    try:
        num=int(input("\nHello! Input the number corresponding to the Food to View The Recipe\n1. %s \n2. %s\n3. %s\n" % (f1_name,f2_name,f3_name)))
    except ValueError:
        print('Please inputa valid number')
        recipe_log()
    while num != '':
        if num==1:
            print(f1_name + '\n')
            for item in f1['Ingredients']:
                litem=[(i,a) for i,a in item.items()]
                print('%s: ---- %s' % (litem[0][1], litem[1][1]))
                #print(f1['Directions'])
            break
            reset = input('\n\nTo return to the main menu, press any letter\n')            
        elif num==2:
            print(f2_name + '\n')
            for item in f2['Ingredients']:
                litem=[(i,a) for i,a in item.items()]
                print('%s: ---- %s\n' % (litem[0][1], litem[1][1]))
                #print(f2['Directions'])
            break
            reset = input('\n\nTo return to the main menu, press any letter\n')        
        elif num==3:
            print(f3_name + '\n')
            for item in f3['Ingredients']:
                litem=[(i,a) for i,a in item.items()]
                print('%s: ---- %s\n' % (litem[0][1], litem[1][1]))
                #print(f3['Directions'])  
            break
            reset = input('\n\nTo return to the main menu, press any letter\n')
        elif num != 1 or 2 or 3:
            print('Please enter a valid number.')
            recipe_log()
            break
    reset = input('\n\nTo return to the main menu, press any letter\n')
    recipe_log()
recipe_log()
#---------------------------------------------------------------------------------------------------------------------------





    






    
    



    

    
