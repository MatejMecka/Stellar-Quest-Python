"""
Challenge 7: Release your own token!
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer, Asset
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create Another account
# In this case this one will serve as the one paying the fees
print("Loading Accounts...")

random_keypair = Keypair.random()
random_keypair_pub_key = random_keypair.public_key
random_keypair_priv_key = random_keypair.secret


# 3. Fund Random account with TestBot
print("Funding Random Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key}) # This is probably waaaay too much to pay fees, but meh.
print(f"Friendbot responded with {response}")

# 4. Create Another account
# In this case this one this account will be payed
print("Loading Accounts...")

random_random_keypair = Keypair.random()
random_random_keypair_pub_key = random_keypair.public_key
random_random_keypair_priv_key = random_keypair.secret

# 5. Fund Another Random account with TestBot
print("Funding Random Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key}) 
print(f"Friendbot responded with {response}")

# 6. Issue Payment
base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)
channel_account = server.load_account(random_keypair_pub_key)

transaction = (
    TransactionBuilder(
        source_account=channel_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_payment_op(
        destination=random_random_keypair_pub_key,
        amount="10",
        asset_code="XLM",
        source=quest_account_pub_key,
    )
    .build()
)


print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
transaction.sign(random_keypair_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the response from trusting the Issuer: {response}")