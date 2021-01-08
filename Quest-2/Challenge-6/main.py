"""
Challenge 6: Sponsoring Reserves
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, FeeBumpTransaction, ClaimPredicate, Claimant, Asset
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

other_account = Keypair.random()
other_account_pub_key = other_account.public_key
other_account_priv_key = other_account.secret

# 2. Create Transaction
print("Building Transaction...")

base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)

transaction = TransactionBuilder(
    source_account=account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=base_fee,
).append_begin_sponsoring_future_reserves_op(
    sponsored_id=other_account_pub_key,
    source=quest_account_pub_key
).append_create_account_op(
    destination=other_account_pub_key,
    starting_balance="0",
    source=quest_account_pub_key
).append_end_sponsoring_future_reserves_op(
    source=other_account_pub_key
).build()


transaction.sign(quest_account_priv_key)
transaction.sign(other_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
