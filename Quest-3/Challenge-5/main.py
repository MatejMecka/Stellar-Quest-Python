"""
Challenge 5: Successfully submit a clawback operation
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer, Asset
import requests

# 1. Load Keys
# In this case this account will be the issuer.
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create Another account
# In this case this one will receive the new token
print("Loading Accounts...")

random_keypair = Keypair.random()
random_keypair_pub_key = random_keypair.public_key
random_keypair_priv_key = random_keypair.secret

print('⚠️ SAVE THE FOLLOWING PUBLIC AND PRIVATE KEY! ISSUING ACCOUNT:')
print(f'Public key: {random_keypair_pub_key}')
print(f'Private key: {random_keypair_priv_key}')

# 3. Fund Other account using TestBot
print("Funding Random Account...")
url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair_pub_key})
print(f"Friendbot responded with {response}")

print("Funding Personal Account...")
response = requests.get(url, params={'addr': quest_account_pub_key})
print(f"Friendbot responded with {response}")

# 4. Create an object to represent the new asset
asset = Asset("[FIGURE IT OUT]", random_keypair_pub_key)

# 5. Allow for clawbacks

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)

print("Allowing Clawbacks...")

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_set_options_op(
        set_flags=10 # Authorization clawback enabled (8) + Authorization revocable (2) = 10
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)
print(f"This is the response from enabling clawbacks: {response}")


# 6. Distributor Account should trust the Issuing account
print("Establishing Trustline...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(random_keypair_pub_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_change_trust_op(
        asset_code=asset.code, 
        asset_issuer=asset.issuer
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(random_keypair_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the response from trusting the Issuer: {response}")

# 7. Now transfer some funds to the distributor account

print('Transfering Tokens from Issuer to Distributor and performing a clawback...')

stellar_account = server.load_account(quest_account_pub_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_payment_op(
        destination=random_keypair_pub_key,
        amount="69", # You get the point....
        asset_code=asset.code,
        asset_issuer=asset.issuer,
    ).append_clawback_op(
        asset=asset,
        from_=random_keypair_pub_key,
        amount="42",
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"Final response: {response}")
