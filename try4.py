from web3 import Web3
 
ethereum_node_url = "https://goerli.infura.io/v3/b8b2ea2f8f4e4ccab7405e9e802ac175"

eth_address = "0x3EAC7cE1c7250b840e74Afd25D06284f07bF1372"

w3 = Web3(Web3.HTTPProvider(ethereum_node_url))

if w3.is_connected():
    print("Connected to Ethereum node")

    # Get the pending transactions
    pending_txns = w3.eth.get_pending_transactions()

    if pending_txns:
        print("Pending Transactions:")
        for tx_hash in pending_txns:
            tx = w3.eth.get_transaction(tx_hash)
            if eth_address.lower() == tx['to'].lower() or eth_address.lower() == tx['from'].lower():
                print(f"Transaction Hash: {tx['hash'].hex()}")

    # Get the latest block number
    latest_block_number = w3.eth.block_number

    # Specify the block range for confirmed transactions
    block_range = range(latest_block_number - 10, latest_block_number + 1)  # Adjust the range as needed

    confirmed_txns = []

    for block_number in block_range:
        block = w3.eth.get_block(block_number, full_transactions=True)

        if block and 'transactions' in block:
            for tx in block['transactions']:
                if eth_address.lower() == tx['to'].lower() or eth_address.lower() == tx['from'].lower():
                    confirmed_txns.append(tx)

    if confirmed_txns:
        print("\nConfirmed Transactions:")
        for tx in confirmed_txns:
            print(f"Transaction Hash: {tx['hash'].hex()} - Block Number: {tx['blockNumber']}")
    else:
        print("\nNo confirmed transactions for the address.")
else:
    print("Failed to connect to Ethereum node.")

