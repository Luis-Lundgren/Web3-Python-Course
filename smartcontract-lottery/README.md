1. Users can enter lottery with ETH based on a USD fee
2. an admin will choose when the lottery is over
3. The lottery will select a random winner

How do we want to this?

1. 'mainnet-fork'
2. 'development' with mocks
3. 'testnet'
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/Ffy3sLc2L9FSHsRSykdm46cgixI1yKy5 accounts=10 mnemonic=brownie port=8545
