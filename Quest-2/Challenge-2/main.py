"""
Challenge 2: Create a Multi Operation Transaction
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Asset
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create Another account
print("Loading Accounts...")

random_keypair = Keypair.random()
random_keypair_pub_key = random_keypair.public_key
random_keypair_priv_key = random_keypair.secret

print('⚠️ SAVE THE FOLLOWING PUBLIC AND PRIVATE KEY! ISSUING ACCOUNT:')
print(f'Public key: {random_keypair_pub_key}')
print(f'Private key: {random_keypair_priv_key}')

# 3. Fund Another account using TestBot
print("Funding Random Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key})
print(f"Friendbot responded with {response}")


# 4. Create Multi Transaction
print("Building Transaction...")
asset = Asset("HUGS", random_keypair_pub_key)

base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)

transaction = (
    TransactionBuilder(
        source_account=account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    ).append_change_trust_op(
        asset_code=asset.code, asset_issuer=asset.issuer
    ).append_payment_op(
        destination=quest_account_pub_key,
        amount="42", # You get the point....
        asset_code=asset.code,
        asset_issuer=asset.issuer,
        source=asset.issuer
    )
    .build()
)
print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
transaction.sign(random_keypair_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
