"""
I generated this code by taking the Free Code Camp:
Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial
links:
Youtube: https://youtu.be/M576WGiDBdQ
GitHub: https://github.com/smartcontractkit/full-blockchain-solidity-course-py
"""
#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, config, network
from scripts.helpful_scripts_test import (
    get_breed,
    fund_with_link,
    listen_for_event,
    get_contract,
)
import time


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        {"from": dev},
    )
    fund_with_link(advanced_collectible.address)
    transaction = advanced_collectible.createCollectible("None", {"from": dev})
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(1)
    print("New token has been created!")
    return advanced_collectible, transaction
    # time.sleep(35)
    # listen_for_event(
    #     advanced_collectible, "ReturnedCollectible", timeout=200, poll_interval=10
    # )
    # requestId = transaction.events["RequestedCollectible"]["requestId"]
    # token_id = advanced_collectible.requestIdToTokenId(requestId)
    # breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    # print("Dog breed of tokenId {} is {}".format(token_id, breed))
