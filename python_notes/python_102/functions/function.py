# def my_func():
#     my_item = "this is nice"
#     return my_item



# results =my_func()

# print(results)


def btc_count(start_count,end_count):
    balance= (start_count - end_count)
    return balance


print(btc_count(100,25))


def btc_count(start_count,end_count):
    balance= (start_count - end_count)
    if balance <= 0:
        return 'Your wallet has been emptied'
    return balance

print(btc_count(100,125))



hash_adddress="1f1gvf313fdd4ghdfg161dcd61f64g6h1654fvhj"

def calc_hash():
    print(len(hash_adddress))

len_=calc_hash()
print(len_)


block = []
block.append(len_)
print(block)


wallet = "you have 2.25 BTC"    ###GLOABAL VARIABLE###
def new_wallet():
    wallet="you now have 10 BTC"  #### DOES NOT CHANGE VARIABLE GLOBALLY, ONLY LOCALLY ###
    print(wallet)

new_wallet()                ##THIS WILL PRINT ###
print(wallet)              ###THIS WILL PRINT GLOBAL wallet: 'you have 2.25 BTC'###





