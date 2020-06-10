

def you_died():
    print('You Be BROKE.')

#you_died()

###YOU CAN SET A FUNCTION CALL TO VARIABLES###

##CREATE NEW VARIABLE AND SET IT = TO THE FUNCTION NAME W/O ()#####
print_dead=you_died
# print_dead()

##NOW ABLE TO USE THE FUNCTION CALL AS ITEM. PLACED IN DICTIONARY BELOW##
btc_wallet = {
    'Message' : print_dead
}

##PRINTS THE FUNTION CALL (You Be Dead.)##
btc_wallet['Message']()

##CREATES NEW FUNCTION  SET TO DICTIONARY ITEM##
##ALLOWS YOU TO SHORTEN LENGHTY DICTIONARY FUNCTION CALL ITEMS## 
empty=btc_wallet['Message']

##PRINTS (You Be Dead.)##
empty()

def movement(dir,speed,position):   
    if dir == 'left':
        position['x'] += speed
    elif dir == 'right':
        position ['x']-= speed
    elif dir == 'up':
        positon['y']-= speed
    elif fir == 'down':
        position['y'] += speed

def attack(power,target):
    re=power-defense
    if re < 0:
        re = 0
    target['Life'] -= 0

player_1= {
    'position':{
        'x':0,
        'y':0
    }
    'times_attack':0 , 
    'attack':attack
    'power':0
    'life':100
    'move':
}

player_1= {
    'position':{
        'x':0,
        'y':0
    }
    'times_attack':  , 
    'attack':
    'power':
    'life':
    'move':
}
