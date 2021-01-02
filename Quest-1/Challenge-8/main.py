"""
Challenge 8: Path Payments
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Asset
import json

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create Asset Objects
asset_to_buy = Asset("SRT", "GCDNJUBQSX7AJWLJACMJ7I4BC3Z47BQUTMHEICZLE6MU4KQBRYG5JY6B") 
native_asset = Asset('XLM')

# 3. Get Path Payment

path_payments = Server.strict_receive_paths(server, source=[native_asset], destination_asset=asset_to_buy, destination_amount='100').call()
path = [Asset(asset['destination_asset_code'], asset['destination_asset_issuer']) for asset in path_payments['_embedded']['records']]
print(path)

# 4. Use Stellar Quest account to send path payment
print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    ).append_change_trust_op(
        asset_code=asset_to_buy.code, asset_issuer=asset_to_buy.issuer
    ).append_path_payment_strict_send_op(
        destination=quest_account_pub_key,
        send_code="XLM", 
        send_issuer=None, 
        send_amount="10",
        dest_code=asset_to_buy.code,
        dest_issuer=asset_to_buy.issuer,
        dest_min="1", 
        path=path
    ) 
    ).build()

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
