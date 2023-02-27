'''

I generated this code by taking the Free Code Camp:
Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial
links:
Youtube: https://youtu.be/M576WGiDBdQ
GitHub: https://github.com/smartcontractkit/full-blockchain-solidity-course-py

'''

import json
from web3 import Web3
import os
from solcx import compile_standard, install_solc
from dotenv import load_dotenv

load_dotenv()
install_solc("0.6.0")


with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)
# CompileOur Solidity
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
# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]
# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
# print(abi)
# for connecting to ganache
# w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
# w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
w3 = Web3(
    Web3.HTTPProvider("https://rinkeby.infura.io/v3/a9efe7001b454999a258da77da10c259")
)
# chain_id = 1337
chain_id = 4
my_address = "0x23787080386c3f02ad6d8D0bF31273c86bF1f210"
# private_key = "0x42b5fd9d73fc840ea3a428616eeacdef458240c92bc8b0aaba93018819797a46"
private_key = os.getenv("PRIVATE_KEY")
# print(private_key)
# create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)
# Get latest transaction
nonce = w3.eth.getTransactionCount(my_address)
# print(nonce)
# 1. Build a transaction
# 2. Sign a transaction
# 3. Send a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
# print(transaction)
# print(os.getenv("SOME_OTHER_VAR"))
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# print(signed_txn)
# Send this signed transaction
print("Deploying Contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!")
# Working with the contract
# Contract Address
# Contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# Call-> Simulate making the call and getting a return value
# Transact -> Actually make a state change
# Initial value of favorite number
print(simple_storage.functions.retrieve().call())
print("Updating Contract...")
# print(simple_storage.functions.store(15).call())
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print("Updated!")
print(simple_storage.functions.retrieve().call())
