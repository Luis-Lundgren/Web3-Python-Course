'''
I generated this code by taking the Free Code Camp:
Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial
links:
Youtube: https://youtu.be/M576WGiDBdQ
GitHub: https://github.com/smartcontractkit/full-blockchain-solidity-course-py
'''

from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
