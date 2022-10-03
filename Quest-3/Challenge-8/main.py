"""
Challenge 8: Use SEP-0006 to acquire some MULT from testanchor.stellar.org
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer, Asset, TransactionEnvelope
from stellar_sdk.sep.stellar_toml import fetch_stellar_toml
import requests
import json

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("SDF7VTA4U7TUEZFPGSPTN3UVMKBVX4QJM6WUPPHYAQG5T246A6BGMBTF")
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
print("OBTAINING TOKEN!")
anchor_token_response = requests.post(TEST_ANCHOR, data={"transaction": xdr})
print(anchor_token_response.text)

if anchor_token_response.status_code != 200:
	raise ValueError("Failed Fetching Auth Token!")

anchor_token_json = json.loads(anchor_token_response.text) 
token = anchor_token_json["token"]

# 6. Perform KYC on Anchor
print("ATTEMPTING KYC")
authorization = {
	'Authorization': f'Bearer {token}'
}

kyc = {
  "account": quest_account_pub_key,
  "first_name": "Kim",
  "last_name": "Pine",
  "email_address": "kim@testmail.com",
  "bank_account_number": "5412341",
  "bank_number": "234123"
}


KYC_URL = f"{toml.get('KYC_SERVER')}/customer"
response = requests.put(KYC_URL, headers=authorization, params={'account':quest_account_pub_key}, data=kyc)
print(response.text)
if response.status_code != 202:
	raise ValueError("Failed to perform KYC!")

response = requests.get(KYC_URL, headers=authorization, params={'account':quest_account_pub_key})
print(response.text)
if response.status_code != 200:
	raise ValueError("Failed to retrieve KYC information about ourselves!")

# 7. Establish Trustline
ASSET = Asset("MULT","GDLD3SOLYJTBEAK5IU4LDS44UMBND262IXPJB3LDHXOZ3S2QQRD5FSMM")

transaction = (
	TransactionBuilder(
		source_account = server.load_account(account_id=quest_account_pub_key), 
		network_passphrase = NETWORK, 
		base_fee=100
	)
) 
transaction.append_change_trust_op(ASSET) 
transaction = transaction.build()

transaction.sign(stellar_quest_keypair)
response = server.submit_transaction(transaction)

# 8. Deposit Fake Money for Asset
# Note: There's no MULT :thinking_face:?
deposit = toml.get("TRANSFER_SERVER")
data = {
	'asset_code':'MULT',
	'account':quest_account_pub_key,
	'type':'bank_account',
	'amount': 420
}

response = requests.get(f"{deposit}/deposit", headers=authorization, params=query)
print(response.json())

