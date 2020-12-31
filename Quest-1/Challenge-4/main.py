"""
Challenge 4: Multisign
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create Another account
print("Loading Accounts...")

random_keypair = Keypair.random()
random_keypair_pub_key = random_keypair.public_key
random_keypair_priv_key = random_keypair.secret

print('⚠️ SAVE THE FOLLOWING PUBLIC AND PRIVATE KEY!')
print(f'Public key: {random_keypair_pub_key}')
print(f'Private key: {random_keypair_priv_key}')

# 3. Fund Another account using TestBot
print("Funding Random Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key})
print(f"Friendbot responded with {response}")

# 4. Use Stellar Quest Account and set multisign
print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)
signer_rand_account = Signer.ed25519_public_key(account_id=random_keypair_pub_key, weight=1)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_set_options_op(
        signer = signer_rand_account
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the response from adding another signer: {response}")

# ====================================================

# 5. Now use the other account to do something.

print('Using other multisign account to bump transaction...')

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_bump_sequence_op(
       bump_to = 0
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(random_keypair_priv_key)
response = server.submit_transaction(transaction)

print(f"Final response: {response}")

