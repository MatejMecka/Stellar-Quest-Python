"""
Challenge 5: Claim a Claimable Balance
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, FeeBumpTransaction, ClaimPredicate, Claimant, Asset
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create Transaction
print("Building Transaction...")

base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)

# Claim Claimable Balance
balance_id = "" # Feel free to specify the balance ID if you know it
if len(balance_id) == 0:
    balances = server.claimable_balances().for_claimant("GDOIK3Z6ED2QD44IJVJ2D7OQ5JCONGSYJ4JLN7PY3TYFHXVZBIWZJNXS").call()
    balance_id = balances["_embedded"]["records"][0]["id"]

print(f"Attempting Balance ID: {balance_id}...")

transaction = TransactionBuilder(
    source_account=account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE
).append_claim_claimable_balance_op(
    balance_id=balance_id,
    source=quest_account_pub_key
).build()

transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
