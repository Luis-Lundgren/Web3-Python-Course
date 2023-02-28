"""
I generated this code by taking the Free Code Camp:
Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial
links:
Youtube: https://youtu.be/M576WGiDBdQ
GitHub: https://github.com/smartcontractkit/full-blockchain-solidity-course-py
"""
#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, network, config, interface
import json


def main():
    flatten()


def flatten():
    file = open("./AdvancedCollectible_flattened.json", "w")
    json.dump(AdvancedCollectible.get_verification_info(), file)
    file.close()
