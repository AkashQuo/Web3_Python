from web3 import Web3
import time

infura_url = "https://goerli.infura.io/v3/b8b2ea2f8f4e4ccab7405e9e802ac175"
user_address = '0x3EAC7cE1c7250b840e74Afd25D06284f07bF1372'

web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.is_connected():
    print("Connected to Ethereum node")
else:
    print("Failed to connect to Ethereum node")
    exit()

"""
Function Date_ trigger(Address)
start_block = latest data block - 10  
end_block = latest data block + 1

"""


def trigger_transaction(address):
    start_block = web3.eth.block_number - 5
    end_block = web3.eth.block_number + 1
    transactions = fetch_transactions(start_block, end_block, address)
    time.sleep(10)

    return transactions


def fetch_transactions(start_block, end_block, address, count=1):
    try:
        transactions = []
        if not web3.is_address(address):
            return []
        for block_number in range(start_block, end_block):
            transactions_count = web3.eth.get_transaction_count(address, block_identifier=block_number)

            print(f"Number of Transactions Found: {transactions_count}")

            for i in range(transactions_count):
                transaction_hash = web3.eth.get_transaction_by_block(block_number, i)
                if transaction_hash:
                    transactions.append(transaction_hash)

    except:
        if count > 50:
            transactions = fetch_transactions(start_block, end_block, address, count + 1)
        else:
            transactions = trigger_transaction(address)
    return transactions


address = '0x3EAC7cE1c7250b840e74Afd25D06284f07bF1372'

transactions_details = trigger_transaction(address)

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
        print(f"Block Number: {transaction_obj['blockNumber']}\n")
else:
    print("No transactions found for the given address.")
