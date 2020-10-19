"""
Challenge 1: Create a Stellar Account
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create Another account
print("Loading Accounts...")

random_keypair = Keypair.random()
random_keypair_pub_key = random_keypair.public_key
random_keypair_priv_key = random_keypair.secret

# 2. Fund Another account using TestBot
print("Funding Random Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key})
print(f"Friendbot responded with {response}")


# 3. Use said account to fund my account
print("Building Transaction...")

base_fee = server.fetch_base_fee()
random_account = server.load_account(random_keypair_pub_key)

transaction = (
    TransactionBuilder(
        source_account=random_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_create_account_op(
    	destination=quest_account_pub_key, 
    	starting_balance="1000",
    )
    .build()
)
print('Signing Transaction...')
transaction.sign(random_keypair)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
