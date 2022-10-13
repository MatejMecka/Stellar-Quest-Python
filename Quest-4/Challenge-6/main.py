#Based on MatejMecka's SQ205.py
#This is a testnet version
"""
Challenge 6: Claim 100 ballances
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Transaction, Network, FeeBumpTransaction, ClaimPredicate, Claimant, Asset
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
quest_account_pub_key = ("YOUR KEY")

# 2. Create Transaction

base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)

# Claim Claimable Balance
balance_id = "" 
if len(balance_id) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id = balances["_embedded"]["records"][0]["id"]

balance_id2 = "" 
if len(balance_id2) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id2 = balances["_embedded"]["records"][1]["id"]

balance_id3 = "" 
if len(balance_id3) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id3 = balances["_embedded"]["records"][2]["id"]

balance_id4 = "" 
if len(balance_id4) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id4 = balances["_embedded"]["records"][3]["id"]

balance_id5 = "" 
if len(balance_id5) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id5 = balances["_embedded"]["records"][4]["id"]    

balance_id6 = "" 
if len(balance_id6) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id6 = balances["_embedded"]["records"][5]["id"]

balance_id7 = "" 
if len(balance_id7) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id7 = balances["_embedded"]["records"][6]["id"]

balance_id8 = "" 
if len(balance_id8) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id8 = balances["_embedded"]["records"][7]["id"]

balance_id9 = "" 
if len(balance_id9) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id9 = balances["_embedded"]["records"][8]["id"]

balance_id10 = "" 
if len(balance_id10) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).call()
    balance_id10 = balances["_embedded"]["records"][9]["id"]

balance_id11 = "" 
if len(balance_id11) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id11 = balances["_embedded"]["records"][10]["id"]

balance_id12 = "" 
if len(balance_id12) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id12 = balances["_embedded"]["records"][11]["id"]

balance_id13 = "" 
if len(balance_id13) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id13 = balances["_embedded"]["records"][12]["id"]

balance_id14 = "" 
if len(balance_id14) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id14 = balances["_embedded"]["records"][13]["id"]

balance_id15 = "" 
if len(balance_id15) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id15 = balances["_embedded"]["records"][14]["id"]    

balance_id16 = "" 
if len(balance_id16) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id16 = balances["_embedded"]["records"][15]["id"]

balance_id17 = "" 
if len(balance_id17) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id17 = balances["_embedded"]["records"][16]["id"]

balance_id18 = "" 
if len(balance_id18) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id18 = balances["_embedded"]["records"][17]["id"]

balance_id19 = "" 
if len(balance_id19) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id19 = balances["_embedded"]["records"][18]["id"]

balance_id20 = "" 
if len(balance_id20) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id20 = balances["_embedded"]["records"][19]["id"]

balance_id21 = "" 
if len(balance_id21) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id21 = balances["_embedded"]["records"][20]["id"]

balance_id22 = "" 
if len(balance_id22) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id22 = balances["_embedded"]["records"][21]["id"]

balance_id23 = "" 
if len(balance_id23) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id23 = balances["_embedded"]["records"][22]["id"]

balance_id24 = "" 
if len(balance_id24) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id24 = balances["_embedded"]["records"][23]["id"]

balance_id25 = "" 
if len(balance_id25) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id25 = balances["_embedded"]["records"][24]["id"]    

balance_id26 = "" 
if len(balance_id26) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id26 = balances["_embedded"]["records"][25]["id"]

balance_id27 = "" 
if len(balance_id27) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id27 = balances["_embedded"]["records"][26]["id"]

balance_id28 = "" 
if len(balance_id28) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id28 = balances["_embedded"]["records"][27]["id"]

balance_id29 = "" 
if len(balance_id29) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id29 = balances["_embedded"]["records"][28]["id"]
    
balance_id30 = "" 
if len(balance_id30) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id30 = balances["_embedded"]["records"][29]["id"]

balance_id31 = "" 
if len(balance_id31) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id31 = balances["_embedded"]["records"][30]["id"]
 
balance_id32 = "" 
if len(balance_id32) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id32 = balances["_embedded"]["records"][31]["id"]

balance_id33 = "" 
if len(balance_id33) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id33 = balances["_embedded"]["records"][32]["id"]

balance_id34 = "" 
if len(balance_id34) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id34 = balances["_embedded"]["records"][33]["id"]

balance_id35 = "" 
if len(balance_id35) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id35 = balances["_embedded"]["records"][34]["id"]    

balance_id36 = "" 
if len(balance_id36) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id36 = balances["_embedded"]["records"][35]["id"]

balance_id37 = "" 
if len(balance_id37) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id37 = balances["_embedded"]["records"][36]["id"]

balance_id38 = "" 
if len(balance_id38) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id38 = balances["_embedded"]["records"][37]["id"]

balance_id39 = "" 
if len(balance_id39) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id39 = balances["_embedded"]["records"][38]["id"] 
 
balance_id40 = "" 
if len(balance_id40) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id40 = balances["_embedded"]["records"][39]["id"]

balance_id41 = "" 
if len(balance_id41) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id41 = balances["_embedded"]["records"][40]["id"]
 
balance_id42 = "" 
if len(balance_id42) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id42 = balances["_embedded"]["records"][41]["id"]

balance_id43 = "" 
if len(balance_id43) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id43 = balances["_embedded"]["records"][42]["id"]

balance_id44 = "" 
if len(balance_id44) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id44 = balances["_embedded"]["records"][43]["id"]

balance_id45 = "" 
if len(balance_id45) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id45 = balances["_embedded"]["records"][44]["id"]    

balance_id46 = "" 
if len(balance_id46) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id46 = balances["_embedded"]["records"][45]["id"]

balance_id47 = "" 
if len(balance_id47) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id47 = balances["_embedded"]["records"][46]["id"]

balance_id48 = "" 
if len(balance_id48) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id48 = balances["_embedded"]["records"][47]["id"]

balance_id49 = "" 
if len(balance_id49) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id49 = balances["_embedded"]["records"][48]["id"]

balance_id50 = "" 
if len(balance_id50) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id50 = balances["_embedded"]["records"][49]["id"]

balance_id51 = "" 
if len(balance_id51) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id51 = balances["_embedded"]["records"][50]["id"]
 
balance_id52 = "" 
if len(balance_id52) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id52 = balances["_embedded"]["records"][51]["id"]

balance_id53 = "" 
if len(balance_id53) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id53 = balances["_embedded"]["records"][52]["id"]

balance_id54 = "" 
if len(balance_id54) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id54 = balances["_embedded"]["records"][53]["id"]

balance_id55 = "" 
if len(balance_id55) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id55 = balances["_embedded"]["records"][54]["id"]    

balance_id56 = "" 
if len(balance_id56) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id56 = balances["_embedded"]["records"][55]["id"]

balance_id57 = "" 
if len(balance_id57) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id57 = balances["_embedded"]["records"][56]["id"]

balance_id58 = "" 
if len(balance_id58) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id58 = balances["_embedded"]["records"][57]["id"]

balance_id59 = "" 
if len(balance_id59) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id59 = balances["_embedded"]["records"][58]["id"]

balance_id60 = "" 
if len(balance_id60) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id60 = balances["_embedded"]["records"][59]["id"]

balance_id61 = "" 
if len(balance_id61) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id61 = balances["_embedded"]["records"][60]["id"]
 
balance_id62 = "" 
if len(balance_id62) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id62 = balances["_embedded"]["records"][61]["id"]

balance_id63 = "" 
if len(balance_id63) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id63 = balances["_embedded"]["records"][62]["id"]

balance_id64 = "" 
if len(balance_id64) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id64 = balances["_embedded"]["records"][63]["id"]

balance_id65 = "" 
if len(balance_id65) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id65 = balances["_embedded"]["records"][64]["id"]    

balance_id66 = "" 
if len(balance_id66) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id66 = balances["_embedded"]["records"][65]["id"]

balance_id67 = "" 
if len(balance_id67) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id67 = balances["_embedded"]["records"][66]["id"]

balance_id68 = "" 
if len(balance_id68) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id68 = balances["_embedded"]["records"][67]["id"]

balance_id69 = "" 
if len(balance_id69) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id69 = balances["_embedded"]["records"][68]["id"]

balance_id70 = "" 
if len(balance_id70) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id70 = balances["_embedded"]["records"][69]["id"]

balance_id71 = "" 
if len(balance_id71) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id71 = balances["_embedded"]["records"][70]["id"]
 
balance_id72 = "" 
if len(balance_id72) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id72 = balances["_embedded"]["records"][71]["id"]

balance_id73 = "" 
if len(balance_id73) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id73 = balances["_embedded"]["records"][72]["id"]

balance_id74 = "" 
if len(balance_id74) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id74 = balances["_embedded"]["records"][73]["id"]

balance_id75 = "" 
if len(balance_id75) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id75 = balances["_embedded"]["records"][74]["id"]    

balance_id76 = "" 
if len(balance_id76) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id76 = balances["_embedded"]["records"][75]["id"]

balance_id77 = "" 
if len(balance_id77) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id77 = balances["_embedded"]["records"][76]["id"]

balance_id78 = "" 
if len(balance_id78) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id78 = balances["_embedded"]["records"][77]["id"]

balance_id79 = "" 
if len(balance_id79) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id79 = balances["_embedded"]["records"][78]["id"]

balance_id80 = "" 
if len(balance_id80) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id80 = balances["_embedded"]["records"][79]["id"]

balance_id81 = "" 
if len(balance_id81) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id81 = balances["_embedded"]["records"][80]["id"]
 
balance_id82 = "" 
if len(balance_id82) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id82 = balances["_embedded"]["records"][81]["id"]

balance_id83 = "" 
if len(balance_id83) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id83 = balances["_embedded"]["records"][82]["id"]

balance_id84 = "" 
if len(balance_id84) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id84 = balances["_embedded"]["records"][83]["id"]

balance_id85 = "" 
if len(balance_id85) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id85 = balances["_embedded"]["records"][84]["id"]    

balance_id86 = "" 
if len(balance_id86) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id86 = balances["_embedded"]["records"][85]["id"]

balance_id87 = "" 
if len(balance_id87) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id87 = balances["_embedded"]["records"][86]["id"]

balance_id88 = "" 
if len(balance_id88) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id88 = balances["_embedded"]["records"][87]["id"]

balance_id89 = "" 
if len(balance_id89) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id89 = balances["_embedded"]["records"][88]["id"]
    
balance_id90 = "" 
if len(balance_id90) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id90 = balances["_embedded"]["records"][89]["id"]

balance_id91 = "" 
if len(balance_id91) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id91 = balances["_embedded"]["records"][90]["id"]
 
balance_id92 = "" 
if len(balance_id92) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id92 = balances["_embedded"]["records"][91]["id"]

balance_id93 = "" 
if len(balance_id93) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id93 = balances["_embedded"]["records"][92]["id"]

balance_id94 = "" 
if len(balance_id94) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id94 = balances["_embedded"]["records"][93]["id"]

balance_id95 = "" 
if len(balance_id95) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id95 = balances["_embedded"]["records"][94]["id"]    

balance_id96 = "" 
if len(balance_id96) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id96 = balances["_embedded"]["records"][95]["id"]

balance_id97 = "" 
if len(balance_id97) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id97 = balances["_embedded"]["records"][96]["id"]

balance_id98 = "" 
if len(balance_id98) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id98 = balances["_embedded"]["records"][97]["id"]

balance_id99 = "" 
if len(balance_id99) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(100).call()
    balance_id99 = balances["_embedded"]["records"][98]["id"]

balance_id100 = "" 
if len(balance_id100) == 0:
    balances = server.claimable_balances().for_claimant(quest_account_pub_key).limit(101).call()
    balance_id100 = balances["_embedded"]["records"][99]["id"]

print(f"Balance: {balance_id}...")
print(f"Balance: {balance_id2}...")
print(f"Balance: {balance_id3}...")
print(f"Balance: {balance_id4}...")
print(f"Balance: {balance_id5}...")
print(f"Balance: {balance_id6}...")
print(f"Balance: {balance_id7}...")
print(f"Balance: {balance_id8}...")
print(f"Balance: {balance_id9}...")
print(f"Balance: {balance_id10}...")
print(f"Balance: {balance_id11}...")
print(f"Balance: {balance_id12}...")
print(f"Balance: {balance_id13}...")
print(f"Balance: {balance_id14}...")
print(f"Balance: {balance_id15}...")
print(f"Balance: {balance_id16}...")
print(f"Balance: {balance_id17}...")
print(f"Balance: {balance_id18}...")
print(f"Balance: {balance_id19}...")
print(f"Balance: {balance_id20}...")
print(f"Balance: {balance_id21}...")
print(f"Balance: {balance_id22}...")
print(f"Balance: {balance_id23}...")
print(f"Balance: {balance_id24}...")
print(f"Balance: {balance_id25}...")
print(f"Balance: {balance_id26}...")
print(f"Balance: {balance_id27}...")
print(f"Balance: {balance_id28}...")
print(f"Balance: {balance_id29}...")
print(f"Balance: {balance_id30}...")
print(f"Balance: {balance_id31}...")
print(f"Balance: {balance_id32}...")
print(f"Balance: {balance_id33}...")
print(f"Balance: {balance_id34}...")
print(f"Balance: {balance_id35}...")
print(f"Balance: {balance_id36}...")
print(f"Balance: {balance_id37}...")
print(f"Balance: {balance_id38}...")
print(f"Balance: {balance_id39}...")
print(f"Balance: {balance_id40}...")
print(f"Balance: {balance_id41}...")
print(f"Balance: {balance_id42}...")
print(f"Balance: {balance_id43}...")
print(f"Balance: {balance_id44}...")
print(f"Balance: {balance_id45}...")
print(f"Balance: {balance_id46}...")
print(f"Balance: {balance_id47}...")
print(f"Balance: {balance_id48}...")
print(f"Balance: {balance_id49}...")
print(f"Balance: {balance_id50}...")
print(f"Balance: {balance_id51}...")
print(f"Balance: {balance_id52}...")
print(f"Balance: {balance_id53}...")
print(f"Balance: {balance_id54}...")
print(f"Balance: {balance_id55}...")
print(f"Balance: {balance_id56}...")
print(f"Balance: {balance_id57}...")
print(f"Balance: {balance_id58}...")
print(f"Balance: {balance_id59}...")
print(f"Balance: {balance_id60}...")
print(f"Balance: {balance_id61}...")
print(f"Balance: {balance_id62}...")
print(f"Balance: {balance_id63}...")
print(f"Balance: {balance_id64}...")
print(f"Balance: {balance_id65}...")
print(f"Balance: {balance_id66}...")
print(f"Balance: {balance_id67}...")
print(f"Balance: {balance_id68}...")
print(f"Balance: {balance_id69}...")
print(f"Balance: {balance_id70}...")
print(f"Balance: {balance_id71}...")
print(f"Balance: {balance_id72}...")
print(f"Balance: {balance_id73}...")
print(f"Balance: {balance_id74}...")
print(f"Balance: {balance_id75}...")
print(f"Balance: {balance_id76}...")
print(f"Balance: {balance_id77}...")
print(f"Balance: {balance_id78}...")
print(f"Balance: {balance_id79}...")
print(f"Balance: {balance_id80}...")
print(f"Balance: {balance_id81}...")
print(f"Balance: {balance_id82}...")
print(f"Balance: {balance_id83}...")
print(f"Balance: {balance_id84}...")
print(f"Balance: {balance_id85}...")
print(f"Balance: {balance_id86}...")
print(f"Balance: {balance_id87}...")
print(f"Balance: {balance_id88}...")
print(f"Balance: {balance_id89}...")
print(f"Balance: {balance_id90}...")
print(f"Balance: {balance_id91}...")
print(f"Balance: {balance_id92}...")
print(f"Balance: {balance_id93}...")
print(f"Balance: {balance_id94}...")
print(f"Balance: {balance_id95}...")
print(f"Balance: {balance_id96}...")
print(f"Balance: {balance_id97}...")
print(f"Balance: {balance_id98}...")
print(f"Balance: {balance_id99}...")
print(f"Balance: {balance_id100}...")

transaction = TransactionBuilder(
    source_account=account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE
).append_claim_claimable_balance_op(
    balance_id=balance_id,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id2,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id3,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id4,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id5,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id6,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id7,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id8,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id9,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id10,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id11,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id12,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id13,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id14,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id15,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id16,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id17,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id18,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id19,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id20,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id21,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id22,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id23,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id24,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id25,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id26,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id27,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id28,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id29,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id30,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id31,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id32,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id33,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id34,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id35,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id36,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id37,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id38,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id39,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id40,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id41,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id42,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id43,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id44,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id45,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id46,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id47,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id48,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id49,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id50,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id51,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id52,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id53,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id54,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id55,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id56,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id57,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id58,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id59,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id60,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id61,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id62,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id63,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id64,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id65,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id66,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id67,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id68,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id69,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id70,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id71,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id72,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id73,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id74,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id75,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id76,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id77,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id78,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id79,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id80,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id81,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id82,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id83,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id84,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id85,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id86,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id87,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id88,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id89,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id90,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id91,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id92,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id93,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id94,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id95,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id96,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id97,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id98,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id99,
    source=quest_account_pub_key
).append_claim_claimable_balance_op(
    balance_id=balance_id100,
    source=quest_account_pub_key    
).build()

xdr = transaction.to_xdr()

print(f"Post this XDR @ SQ Xdr Box: {xdr}")
print(f"Check stellar.expert/explorer if all balances are gone, if all gone, merge using laboratory.stellar.org")
