"""
I generated this code by taking the Free Code Camp:
Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial
links:
Youtube: https://youtu.be/M576WGiDBdQ
GitHub: https://github.com/smartcontractkit/full-blockchain-solidity-course-py
"""

from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    # print(account)
    # account = accounts.load("tutorial-account")
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
