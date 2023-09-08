from web3 import Web3, HTTPProvider

provider_url = "YOUR_QUICKNODE_NODE_URL"
provider = Web3.HTTPProvider(provider_url)

txpool_data = provider.make_request('txpool_content', [])
first_queued_address = list(txpool_data['result']['queued'].keys())[0]
first_queued_transaction = txpool_data['result']['queued'][first_queued_address]
print("Queued Transaction: ", [i for i in first_queued_transaction.items()])