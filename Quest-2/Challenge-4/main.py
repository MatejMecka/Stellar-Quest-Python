"""
Challenge 4: Create a Claimable Balance
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, FeeBumpTransaction, ClaimPredicate, Claimant, Asset
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 3. Create Transaction
print("Building Transaction...")

base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)

# Cluster fuck here...
predicate = ClaimPredicate.predicate_not(ClaimPredicate.predicate_before_absolute_time(1609113600)) # Just convert it... Or send a PR writting code to convert to unix timestamp <3
claimant = Claimant(destination=quest_account_pub_key, predicate=predicate)

transaction = (
    TransactionBuilder(
        source_account=account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,

    ).append_create_claimable_balance_op(
        asset=Asset.native(),
        amount="100",
        claimants=[claimant],
        source=quest_account_pub_key
    )
    .build()
)
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
