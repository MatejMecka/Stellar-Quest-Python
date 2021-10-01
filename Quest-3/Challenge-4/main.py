"""
Challenge 4: Submit a pre-authorized transaction
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Fund Account

print("Funding account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': stellar_quest_keypair.public_key})
print(f"Friendbot responded with {response}")

print("Building Transaction...")

base_fee = server.fetch_base_fee()
original_stellar_account = server.load_account(quest_account_pub_key)
stellar_account = server.load_account(quest_account_pub_key)
stellar_account.increment_sequence_number()

# 3. Create PreAuth transaction

preauth_transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    ).append_manage_data_op(
        data_name="Hello",
        data_value="World"
    )
)

transaction_first = preauth_transaction.build()
transaction_hash = transaction_first.hash()

# 4. Submit the other transaction

transaction = (
    TransactionBuilder(
        source_account=original_stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    ).append_pre_auth_tx_signer(
        transaction_hash, 
        1
    )
)

transaction = transaction.build()
print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the first response: {response}")

response = server.submit_transaction(transaction_first) 
print(f"Final response: {response}")
