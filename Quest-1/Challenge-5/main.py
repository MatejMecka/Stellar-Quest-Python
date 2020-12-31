"""
Challenge 5: Release your own token!
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer, Asset
import requests

# 1. Load Keys
# In this case this account will be the distributor.
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create Another account
# In this case this one will Issue the new token
print("Loading Accounts...")

random_keypair = Keypair.random()
random_keypair_pub_key = random_keypair.public_key
random_keypair_priv_key = random_keypair.secret

print('⚠️ SAVE THE FOLLOWING PUBLIC AND PRIVATE KEY! ISSUING ACCOUNT:')
print(f'Public key: {random_keypair_pub_key}')
print(f'Private key: {random_keypair_priv_key}')

# 3. Fund Issuer account using TestBot
print("Funding Random Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key})
print(f"Friendbot responded with {response}")

# 4. Create an object to represent the new asset
asset = Asset("HEYY", random_keypair_pub_key)

# 5. Distributor Account should trust the Issuing account
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
        asset_code=asset.code, asset_issuer=asset.issuer
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the response from trusting the Issuer: {response}")

# 6. Now transfer some funds to the distributor account

print('Transfering Tokens from Issuer to Distributor...')
issuer_account = server.load_account(random_keypair_pub_key)

transaction = (
    TransactionBuilder(
        source_account=issuer_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_payment_op(
        destination=quest_account_pub_key,
        amount="42", # You get the point....
        asset_code=asset.code,
        asset_issuer=asset.issuer,
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(random_keypair_priv_key)
response = server.submit_transaction(transaction)

print(f"Final response: {response}")

