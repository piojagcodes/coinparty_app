from bitcash import PrivateKeyTestnet
from bitcash import Key
import json
from dataclasses import dataclass
import time 


time = time.asctime()
print(time)

#Creating address and private key

key = Key()
addr = key.address
pub_key = key.public_key


@dataclass
class BC_Instance:
    bc_key: any 
    bc_addr: any
    bc_pubkey: any

print(60*"*")

p = BC_Instance(bc_key= key, bc_addr=addr,bc_pubkey=pub_key)

jsonified_p = f'{{"Bitcoin_cash" : {p.bc_key}, "bitcoin_cash_address" : {p.bc_pubkey}}}'

file = open('dataset.csv', "w")
if file.writable():
    file.write(jsonified_p)
    file.close()    

if file.readable():
    message = file.read()
    print(message)

print(60*"*")

balance = key.get_balance('usd')
print("Actual ammount: " + balance + " USD")

support = int(balance)
    
if support == 0:
        print("Insufficient funds for transaction.")
    






