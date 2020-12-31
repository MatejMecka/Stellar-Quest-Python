"""
Challenge 8: Path Payments
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Asset
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhh")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Create Another account
asseet_to_buy = Asset("SRT", "GCDNJUBQSX7AJWLJACMJ7I4BC3Z47BQUTMHEICZLE6MU4KQBRYG5JY6B")

# 3. Fund Another account using TestBot
print("Funding Random Account...")

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key})
print(f"Friendbot responded with {response}")


# 4. Use Stellar Quest account to fund a random one
print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    ).append_path_payment_strict_receive_op(
    destination="GBBM6BKZPEHWYO3E3YKREDPQXMS4VK35YLNU7NFBRI26RAN7GI5POFBB",
    send_code="XLM", 
    send_issuer=None, 
    send_max="1000", 
    dest_code="GBP",
    dest_issuer="GASOCNHNNLYFNMDJYQ3XFMI7BYHIOCFW3GJEOWRPEGK2TDPGTG2E5EDW",
    dest_amount="5.50", path=path) 
    ).build()

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
