"""
I generated this code by taking the Free Code Camp:
Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial
links:
Youtube: https://youtu.be/M576WGiDBdQ
GitHub: https://github.com/smartcontractkit/full-blockchain-solidity-course-py

1. aave assets
2. % split between aseets
3. non Stable coin assets:
    return: price, open, low, high, close, volume, best_apy
4. if best_apy is not the same as supply asset then swap
"""
from scripts.helpful_scripts import get_account
from brownie import network, config, interface
from web3 import Web3


def main():
    aacount = get_account()
    lending_pool = get_pool()
    print(f"Lending Pool address: {lending_pool.address}")
    get_full_reserves_incentive_data(lending_pool, aacount)


def get_full_reserves_incentive_data(lending_pool, account):
    # aggragate_reserve_data = []
    # user_reserve_data = []
    test_interface = interface.IUiIncentiveDataProviderV3(lending_pool.address)
    print(f"Test Interface : {test_interface}")
    test_get_data = test_interface.getReservesIncentivesData(test_interface)
    print(test_get_data)
    # .getReservesIncentivesData(
    #         lending_pool.address)
    # print(f"Aggregate data : {aggragate_reserve_data}")
    # print(f"User Data: {user_reserve_data}")


def get_pool():
    lending_pool_addresses_provider = inter
