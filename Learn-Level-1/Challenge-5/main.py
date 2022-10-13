"""
Challenge 5: Path Payment
"""
from stellar_sdk import Asset, Server, Keypair, TransactionBuilder, Network
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("SECRET")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Path
path = [
    Asset("USDT", "GDMUX3LEQ2HBJDMHTYNSR23YC3JZWTWY63KRMZ7B4Z5II6X5BGB73UWS"),
    Asset("BTC", "GDMUX3LEQ2HBJDMHTYNSR23YC3JZWTWY63KRMZ7B4Z5II6X5BGB73UWS"),
]

# 3. Transaction

print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)
print('IF IT FAILS CHECK THE TESTNET ORDERBOOK AND CHANGE DEST ASSET')
transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
     .append_path_payment_strict_receive_op(
        destination="GDMUX3LEQ2HBJDMHTYNSR23YC3JZWTWY63KRMZ7B4Z5II6X5BGB73UWS",
        send_asset=Asset.native(),
        send_max="1000",
        dest_asset=Asset(
            "1INCH", "GDMUX3LEQ2HBJDMHTYNSR23YC3JZWTWY63KRMZ7B4Z5II6X5BGB73UWS"
        ),
        dest_amount=".1",
        path=path,
    )
    .set_timeout(30)
    .build()
)

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the response from selling the token: {response}")
