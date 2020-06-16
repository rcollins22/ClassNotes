##'class' DEFINES A NEW CLASS##
class Player():
    ## _________ FUNCTIONS ARE TO BE USED WITHIN AN OBJECT. OR 'PRIVATE'##
    def __init__(self):
        print('Ive Started')
    ##WHENEVER USING CLASS METHOD, 'self' MUST BE FIRST ARGUMENT##
    ##FUNCTIONS CAN BE DEFINED WITHIN CLASSES##
    def movement(self,dir,speed,position):   
        if dir == 'left':
            position['x'] -= speed
        elif dir == 'right':
            position ['x']+= speed
        elif dir == 'up':
            positon['y']-= speed
        elif fir == 'down':
            position['y'] += speed

player1= Player()
player1.position = {'x':0,'y':0}
player1.speed=10
print(player1.position)
player1.movement('left',10,player1.position)
print(player1.position)

player2=Player()
position2= position
player1.movement('left',10,position) 
print(player1)

Player()

class Character():
    ## _________ FUNCTIONS ARE TO BE USED WITHIN AN OBJECT. OR 'PRIVATE'##
    ##ADDING 'name' ARGUMENT ALLOWS US TO SET OUR NAME IN ARGUMENT BELOW##
    def __init__(self,name,position,speed=10,health=100,attack_power=5):
        self.name=name
        ##SELF CONTAINED VARIABLES IN CLASSES ALLOW MUTIPLE OBJECTS OF CLASS TO ACT AS OWN ENTITY.##
        self.speed = speed
        self.position={'x':0,'y':0}
        self.health= health
        self.attack_power = attack_power
        ##NOW EACH PLAYER WILL HAVE THEIR OWN 'position' AND 'speed"##

    def attack(self):
        return self.attack_power
        
   ## 'self.' CAN BE USED IN THE FUNCTION, THE FOLLOWING RUNS THE SAME AS ABOVE##
   ##AFTER ADDING 'self.' IN THE INTERNAL ARGUMENTS WE NO LONGER NEED TO CLOSE THEM##
    def movement(self,dir):   
        if dir == 'left':
            self.position['x'] -= self.speed
        elif dir == 'right':
            self.position['x']+= self.speed
        elif dir == 'up':
            self.positon['y']-= self.speed
        elif dir == 'down':
            self.position['y'] += self.speed

##SUB-CLASS##
class Player(Character):
    def heal(self):
        self.health += 25

class Enemy(Character):
    def __init__(self,name,position):
        ##'super' CALLS PARENT CLASS AREGUMENTS##
        super().__init__(name,position)
        self.health=50
        self.speed=4
    
    def roll(self):
        self.position['x'] -=25

##SETS A VARIABLE TO THE CLASS 'Player()'##
##ABLE TO NAME PLAYER WITH 'name' ARGUMENT##
player1= Player('Rashad',{'x':0,'y':0})
print(player1.speed)

antag=Enemy('Gorg',{'x':10,'y':30})
print(antag)


#player2=Player('Chels')

