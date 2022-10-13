"""
Challenge 3: Change Trust
"""
from stellar_sdk import Asset, Server, Keypair, TransactionBuilder, Network
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("SECRET")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Random key and asset
random_keypair = Keypair.random()
random_keypair_pub_key = random_keypair.public_key
random_keypair_priv_key = random_keypair.secret

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key})
asset_quest = Asset("BRLT", random_keypair_pub_key)
print(asset_quest)

# 3. Transaction
print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_change_trust_op(
        asset=asset_quest
    )
    .set_timeout(30)
    .build()
)

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the response from trusting the Issuer: {response}")

