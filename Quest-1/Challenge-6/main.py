"""
Challenge 6: Sell your own token!
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer, Asset
import requests

# 1. Load Keys
# In this case this account will be the distributor.
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create an object to represent the new asset
issuer_pub_key = "The one that issued the Token"
asset = Asset("[ASSET NAME HERE]", issuer_pub_key)

# 3. Sell of Asset
print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_manage_sell_offer_op(
        selling_code=asset.code, 
        selling_issuer=asset.issuer,
        buying_code="XLM",
        buying_issuer=None,
        amount="1", # Feel free to change this.
        price="10",
        offer_id=0
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the response from selling the token: {response}")