"""
Challenge 3: Submit a hash signed transaction
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network
import requests
import hashlib
import binascii

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

key_value = "Figure out the hint ;)"

h = hashlib.sha256(key_value)
hash_X = h.hexdigest()

# 2. Fund Account

print("Funding account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': stellar_quest_keypair.public_key})
print(f"Friendbot responded with {response}")

print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)

# 3. Add HashX Signer

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    ).append_hashx_signer(
        hash_X, 
        2
    )
)


transaction = transaction.build()
print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the response from adding the signer: {response}")

# 4. Remove HashX Signer

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    ).append_hashx_signer(
        hash_X, 
        0
    )
)

transaction = transaction.build()
print('Signing Transaction...')
transaction.sign_hashx(key_value)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
