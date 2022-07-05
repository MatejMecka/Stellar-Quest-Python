"""
Challenge 6: Mint a Stellar Quest style NFT
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer, Asset
import requests
import base64
from math import ceil

# 1. Load Keys
# In this case this account will be the issuer.
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("SD5ECGLV25MRROSWKZ5VE7WVCCHCTIISY3MQYQCPI5IPY4VCLZYRL3YT")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

# 2. Download the image and encode it
data = requests.get('[URL HERE]').content
base_encoded_data = base64.b64encode(data)

# 3. Fund the Account

print("Funding Account...")
url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': quest_account_pub_key})
print(f"Friendbot responded with {response}")

# 4. Splice the image into manage data ops

# Credits: W00kie
def chunk(text: str, size: int) -> list:
    return [text[i : i + size] for i in range(0, len(text), size)]


base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)

transaction = TransactionBuilder(
    source_account=account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=base_fee,
)

i = 0

for entry in chunk(base_encoded_data, 62 + 64):
    key = f"{i:02d}{entry[:62].decode('utf8')}"
    value = entry[62:]

    print(key)

    transaction.append_manage_data_op(
        data_name = key,
        data_value = value,
    )
    i += 1

# 5. Submit the Transaction

transaction = transaction.build()
transaction.sign(stellar_quest_keypair)
response = server.submit_transaction(transaction)
print(f"This is the final response: {response}")
