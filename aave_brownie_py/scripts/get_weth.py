"""
I generated this code by taking the Free Code Camp:
Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial
links:
Youtube: https://youtu.be/M576WGiDBdQ
GitHub: https://github.com/smartcontractkit/full-blockchain-solidity-course-py
"""
from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH.
    :return:
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10**18})
    tx.wait(1)
    print("Received 0.1 WETH")
    return tx
