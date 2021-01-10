"""
Challenge 2: Create a Multi Operation Transaction
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, FeeBumpTransaction
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

# 3. Fund Another account using TestBot
print("Funding Random Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key})
print(f"Friendbot responded with {response}")


# 4. Create Inner Transaction
print("Building Inner Transaction...")

base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)
other_account = server.load_account(random_keypair_pub_key)

inner_transaction = (
    TransactionBuilder(
        source_account=account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
        v1=True
    ).append_bump_sequence_op(
        bump_to=1
    )
    .build()
)

print('Signing Inner Transaction...')
inner_transaction.sign(quest_account_priv_key)

# 5. Create Fee Bump transactionn
fee_bump_tx = TransactionBuilder.build_fee_bump_transaction(
    fee_source=random_keypair, 
    base_fee=base_fee, 
    inner_transaction_envelope=inner_transaction,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE
)

fee_bump_tx.sign(random_keypair_priv_key)
response = server.submit_transaction(fee_bump_tx)

print(f"This is the final response: {response}")
