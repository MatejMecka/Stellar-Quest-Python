"""
Challenge 2: Pay a Stellar Account
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

# 3. Fund Another account using TestBot
print("Funding Random Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key})
print(f"Friendbot responded with {response}")


# 4. Use Stellar Quest account to fund a random one
print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_payment_op(
    	destination=random_keypair_pub_key, 
    	amount="10",
        asset_code="XLM",
    )
    .build()
)
print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
