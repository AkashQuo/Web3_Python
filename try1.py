import asyncio
import json
from web3 import Web3
from websockets import connect

infura_ws_url = 'wss://goerli.infura.io/v3/b8b2ea2f8f4e4ccab7405e9e802ac175'
infura_http_url = 'https://goerli.infura.io/v3/b8b2ea2f8f4e4ccab7405e9e802ac175'
web3 = Web3(Web3.HTTPProvider(infura_http_url))

# Used if you want to monitor ETH transactions to a specific address
account = '0x3EAC7cE1c7250b840e74Afd25D06284f07bF1372'


async def get_event():
    async with connect(infura_ws_url) as ws:
        await ws.send('{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}')
        subscription_response = await ws.recv()
        print(subscription_response)

        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=15)
                response = json.loads(message)
                txHash = response['params']['result']
                print(txHash)
                # Uncomment lines below if you want to monitor transactions to
                # a specific address
                # tx = web3.eth.get_transaction(txHash)
                # if tx.to == account:
                #     print("Pending transaction found with the following details:")
                #     print({
                #         "hash": txHash,
                #         "from": tx["from"],
                #         "value": web3.fromWei(tx["value"], 'ether')
                #     })
                pass
            except:
                pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(get_event())
