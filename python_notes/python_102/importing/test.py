import hashlib


class Wallet1():
    
    def __init__(self,hash_string):
        self.hash_string=hash_string
    
    def encrypt_trans(self):
        signature = hashlib.sha256(self.hash_string.encode()).hexdigest()
        return signature
    
    def retun(self):
        encrypt_trans()
        print(signature)

my_wallet=Wallet1('4514354562')
import_code=my_wallet.encrypt_trans()
print(import_code)