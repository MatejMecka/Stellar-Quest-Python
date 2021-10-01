"""
Challenge 2: Create 100 Operations
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Fund Account

print("Funding account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': stellar_quest_keypair.public_key})
print(f"Friendbot responded with {response}")

print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
)

for i in range(100):
    transaction.append_manage_data_op(
        data_name=f"Hello{i}", 
        data_value="World",
    )

transaction = transaction.build()
print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
