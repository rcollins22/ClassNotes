crypto={
    "Bitcoin": 'currency',                  ##{} USED FOR DICTIONARIES
    "Ethereum":'scaleable platform',                 
    "Ripple":'Centrilized',
    "Storj":'Decentralized Cloud Data',
    "litecoin": 'currency'
}
print(crypto)                       ###PRINTS:{'Bitcoin': 'currency', 'Ethereum': 'scaleable platform',
                                            #'Ripple': 'Centrilized', 'Storj': 'Decentralized Cloud Data'}



dict_2= {
    "currency":["Bitcoin","Litecoin"],
    "Centralized":"Ripple",                 ##YOU CAN COMBINE ITEMS UNDER THE SAME KEYWORDS##
    "Decentalized Could Data":["Storj"],
    "scaleable platform":["Ethereum"]
 }
for key in dict_2:                            ###LOOPS THROUGH AND PRINTS ALL KEYWORDS
    print(key)

dict_3= {
    "a":"The is a Test",
    "b":[2,4,5],                                ##DICTIONARIES CA BE MADE OF [l,i,s,t,s],'strings',40.5 etc..###
    "c":45.5
}


                                               ##EASY TO TARGET ANY PORTION OF DICTIONARY##
print(dict_3["b"][2])                           ## PRINTS 5
print(dict_2["Centralized"])                    ## PRINTS Ripple
print(dict_3["b"])



big_crypto= { "Bitcoin" : {'Supply':21000000 , 'Type':'currency'},    ##DICTIONARIES CAN NEST IN DISCTIONARIES###
    "Ethereum":'scaleable platform',                 
    "Ripple":'Centrilized',
    "Storj":'Decentralized Cloud Data',
    "litecoin": 'currency'
}

big_crypto['Bitcoin']['Year Created']=2008            ##ADDS A NEW ITEM(2008) AND KEYWORD('Year Created')
print(big_crypto)  


ttl_supply=big_crypto['Bitcoin']['Supply']             ###ABLE TO ASSIGN VARIABLES TO NESTED DITIONARY ELEMENTS##
print(ttl_supply)                                      ## PRINTS 21000000
