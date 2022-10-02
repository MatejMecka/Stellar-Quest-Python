"""
Challenge 7: Acquire and make use of a SEP-0010 JWT
"""

from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer, Asset, TransactionEnvelope
from stellar_sdk.sep.stellar_toml import fetch_stellar_toml
import requests
import json

# Credits: W00kie
def chunk(text: str, size: int) -> list:
    return [text[i : i + size] for i in range(0, len(text), size)]

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhhhhhhh..... :P")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret
NETWORK = Network.TESTNET_NETWORK_PASSPHRASE

# 2. Fund the Account
print("Funding Account...")
url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': quest_account_pub_key})
print(f"Friendbot responded with {response}")

# 3. Obtain WEB_AUTH_ENDPOINT 
try:
	print("OBTAINING WEB AUTH ENDPOINT!")
	toml = fetch_stellar_toml("testanchor.stellar.org", None)
	TEST_ANCHOR = toml.get("WEB_AUTH_ENDPOINT")
except Exception as e:
	raise ValueError(f"Could not Access .toml file! Error: {str(e)}")


# 4. Obtain XDR from Anchor
print("OBTAINING XDR!")
TEST_ANCHOR = "https://testanchor.stellar.org/auth"
anchor_response = requests.get(TEST_ANCHOR, params=f"account={quest_account_pub_key}")
if anchor_response.status_code != 200:
	raise ValueError(f"Request to Anchor failed! Error {anchor_response.text}")

json_response_anchor = json.loads(anchor_response.text)
xdr = json_response_anchor["transaction"]
print("OBTAINED XDR!")

transaction = TransactionEnvelope.from_xdr(xdr, NETWORK)
transaction.sign(quest_account_priv_key)
xdr = transaction.to_xdr()
print(xdr)

# 5. Retrieve Token
anchor_token_response = requests.post(TEST_ANCHOR, data={"transaction": xdr})
print(anchor_token_response.text)

if anchor_token_response.status_code != 200:
	raise ValueError("Failed Fetching Auth Token!")

anchor_token_json = json.loads(anchor_token_response.text) 
token = anchor_token_json["token"]

# 6. Build Transaction
transaction = (
	TransactionBuilder(
		source_account = server.load_account(account_id=quest_account_pub_key), 
		network_passphrase=NETWORK, 
		base_fee=10000
	) 	
)

i = 0

for entry in chunk(token, 62 + 64):
    key = f"{i:02d}{entry[:62]}"
    value = entry[62:]

    print(key)

    transaction.append_manage_data_op(
        data_name = key,
        data_value = value,
    )
    i += 1


# 7. Submit the Transaction
transaction = transaction.build()
transaction.sign(stellar_quest_keypair)
response = server.submit_transaction(transaction)
print(f"This is the final response: {response}")



