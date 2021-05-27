"""
Challenge 1: Bump the Sequence Number
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network
import hashlib
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Fund Another account using TestBot
print("Funding Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': quest_account_pub_key})
print(f"Friendbot responded with {response}")

# 3. Get the Sequence Number
KEYWORD = b"" # Figure it out mate :D Gotta make it harder for you somehow.
SEQUENCE_NUMBER = "".join([str(elem) for elem in KEYWORD])


# 4. Load stuff...
print("Building Transaction...")

base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)

# 5. Bump Sequence

transaction = (
    TransactionBuilder(
        source_account=account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_bump_sequence_op(
    	bump_to=int(SEQUENCE_NUMBER),
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(stellar_quest_keypair)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
