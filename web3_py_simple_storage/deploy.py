from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()
install_solc("0.6.0")

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
# print(compiled_sol)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# when you deploy you need bytecode and abi
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
# print(abi)

# for connecting locally  to Ganache
# w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:8545'))
# chain_id = 1337
# my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
# private_key = os.getenv("PRIVATE_KEY")

# for connecting to test net using Infura
w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/36da14d84abf4510b8c2e6a63cb59436'))
chain_id = 4 #chainlist.org
my_address = "0x3b62cC24c0f68a978b16eA3eD3eCeD3b83343962"
private_key = os.getenv("PRIVATE_KEYmm")

# create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)

# get the latest transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)
# 3 steps: 
# 1. Build transaction 
# 2. Sign Transaction 
# 3. Send Transactions

transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId":chain_id, 
    "from":my_address, 
    "nonce":nonce,
    "gasPrice":2700000000})
# print(transaction)
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# print(signed_txn)

# send the tx
print("deploying contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("deployed!")
# Working with the contract, you always need
# contract address
# contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)



# when making txs theres 2 diff ways to interact w them
#1. Call -> simulate making the call and getting a return value
#2. Transact -> actually make a state change

# inital value of fav number, call() is just a simulation
print(simple_storage.functions.retrieve().call())
print(simple_storage.functions.store(15).call())
print(simple_storage.functions.retrieve().call())

# transact
print("updating contract...")
store_transaction = simple_storage.functions.store(15).buildTransaction({
    "chainId":chain_id, 
    "from":my_address, 
    "nonce":nonce+1,
    "gasPrice":2700000000})

signed_store_txn = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
transaction_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("updated!")
print(simple_storage.functions.retrieve().call()) # now it'll show the state change

