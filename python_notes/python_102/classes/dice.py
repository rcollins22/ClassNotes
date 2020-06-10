""" Create a program (using using only a single class) that creates a dice rolling system for a d6, d12, d20.
Have the user choose one of the 3 dice and roll it. 
Have each dice keep a record of how many times it was rolled and what was rolled.
Have the user be able to request the average roll for a single dice.
(Challange) Create a Cheat d20 dice that has a cheat_roll function that will ask for a target number and get within
two of that number. However it can only be used once every 10 rolls. (this can be a subclass)
(Extra Challange) Allow a user to 'create' their own dice of any size, and be able to use it in the program.
(Extra Extra Challange) have a menu for each dice to have options like "show rolls, show averages,reset roll count. """
#--------------------------------------------------------------------------------------------------------------------------
import random
d_tr=input("\n Ready to DIE?\n\n")

class Die():    
    def __init__(self,name,side,history=[], counter=0):
        self.side= side
        self.history= history
        self.counter= counter
        self.name= name
        
    
    def choice(self):
        if d_tr == 'a' or 'A':
            dicea.roll()
            return
        elif d_tr == 'b' or 'B':
            diceb.roll()
            return
        elif d_tr == 'c' or 'C':
            dicec.roll()
            return

    def roll(self):
        final=random.choice(self.side)
        self.counter += 1
        self.history.append(final)
        result()


    def result(self):
        name=self.name
        final=random.choice(self.side)
        print("%s's die history is %s" % (self.name, self.history))
        print('The number on %s is %s' % (name, final ))

dicea = Die('D6',6)
diceb= Die('D12', 12)
dicec= Die('D20',20)




#if dt_r 

    


            



