from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/b8b2ea2f8f4e4ccab7405e9e802ac175"))

if web3.is_connected():
    print(f"Connected to Ethereum node: {web3.provider.endpoint_uri}")
else:
    print("Failed to connect to Ethereum node.")
    exit(1)

pending_tx_filter = web3.eth.filter('pending')
pending_tx = pending_tx_filter.get_new_entries()


for hash in pending_tx:
    print('Hash of a Pending Transaction:', web3.toHex(hash))
 # web3.exceptions.MethodUnavailable: {'code': -32601, 'message': 'The method eth_newPendingTransactionFilter does not exist/is not available'}