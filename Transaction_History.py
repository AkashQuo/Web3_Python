from web3 import Web3

# web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/b8b2ea2f8f4e4ccab7405e9e802ac175"))
web3 = Web3(Web3.HTTPProvider(""))

if web3.is_connected():
    print(f"Connected to Ethereum node: {web3.provider.endpoint_uri}")
else:
    print("Failed to connect to Ethereum node.")
    exit(1)


def fetch_transactions(address, count=1):
    try:
        transactions = []

        block_number = web3.eth.block_number

        if not web3.is_address(address):
            return []

        transactions_count = web3.eth.get_transaction_count(address, block_identifier=block_number)

        print(f"Number of Transactions Found: {transactions_count}")

        for i in range(transactions_count):
            transaction_hash = web3.eth.get_transaction_by_block(block_number, i)
            if transaction_hash:
                transactions.append(transaction_hash)
    except:
        if count < 5:
            transactions = fetch_transactions(address, count + 1)
    return transactions


# address = '0x3EAC7cE1c7250b840e74Afd25D06284f07bF1372'

address = ""
transactions_details = fetch_transactions(address)

if transactions_details:
    for index, transaction_obj in enumerate(transactions_details):
        print(f"\n {index + 1}. Transaction Details:")
        print(f"Transaction Hash: {transaction_obj['hash'].hex()}")
        print(f"Nonce: {transaction_obj['nonce']}")
        print(f"From: {transaction_obj['from']}")
        print(f"To: {transaction_obj['to']}")
        print(f"Value: {web3.from_wei(transaction_obj['value'], 'ether')} Ether")
        print(f"Gas Price: {web3.from_wei(transaction_obj['gasPrice'], 'gwei')} Gwei")
        print(f"Gas Used: {transaction_obj['gas']}")
        print(f"Max Priority Fee Per Gas: {transaction_obj['maxPriorityFeePerGas']}")
        print(f"Block Number: {transaction_obj['blockNumber']}\n")
else:
    print("No transactions found for the given address.")
