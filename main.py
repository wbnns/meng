from goplus.token import Token
from goplus.rug_pull import RugPull

import requests
import json


# Define the attributes indicating higher risk at the global level
risk_indicating_attributes = ['is_mintable', 'can_take_back_ownership', 'owner_change_balance',
                              'hidden_owner', 'is_honeypot', 'transfer_pausable', 'is_blacklisted', 'gas_abuse', 'cannot_sell_all',
                              'anti_whale_modifiable', 'trading_cooldown', 'is_airdrop_scam', 'selfdestruct','transfer_pausable',
                              'cannot_buy', 'is_blacklisted','privilege_withdraw', 'withdraw_missing', 'approval_abuse']
safe_attributes = ['is_open_source', 'is_in_dex', 'is_true_token', 'trust_list', 'is_true_token']



def fetch_token_data(address):
    data = Token(access_token=None).token_security(
        chain_id="1",
        addresses=[address],
        **{"_request_timeout": 10}
    )
    token_data_json = getattr(data, 'result', {})
    return token_data_json.get(address.lower(), {})

def analyze_token_risk(token_attributes):
    risk_score = 0
    failing_risks = []
    
    for attribute in risk_indicating_attributes:
        attribute_value = getattr(token_attributes, attribute, None)
        if attribute_value == '1':
            risk_score += 1
            failing_risks.append(attribute)
    
    for attribute in safe_attributes:
        attribute_value = getattr(token_attributes, attribute, None)
        if attribute_value == '0':  # '1' indicating true/safe condition
            risk_score += 1
            failing_risks.append(attribute)


    is_proxy = getattr(token_attributes, 'is_proxy', None) == '1'

    return risk_score, is_proxy, failing_risks

def run_analysis():
    address = input("Please enter the contract address for analysis: ").strip()
    
    if not address.startswith("0x") or len(address) != 42:
        print("The entered address does not appear to be a valid Ethereum address. Please check and try again.")
        return

    #goplus
    token_data = fetch_token_data(address)
    
    if not token_data:
        print("Goplus was unable to run on the contract. Please reference the contract at https://dexscreener.com/")
        return

    risk_score, is_proxy, failing_risks = analyze_token_risk(token_data)

    if is_proxy:
        print("Detected a proxy contract. Please enter the implementation contract address for further analysis:")
        implementation_address = input("Implementation Address: ").strip()
        
        if not implementation_address.startswith("0x") or len(implementation_address) != 42:
            print("The entered address does not appear to be a valid Ethereum address. Please check and try again.")
            return
        
        token_data = fetch_token_data(implementation_address)
        if not token_data:
            print("Goplus was unable to run on the implementation contract. Please reference the contract at https://dexscreener.com/")
            return
        risk_score, _, failing_risks = analyze_token_risk(token_data)

    print(f"Number of Failing Risks: {risk_score} of ")
    if risk_score > len(risk_indicating_attributes) / 2:
        risk_level = "HIGH risk; more than half the checks failed"
    else:
        risk_level = "LOWER risk; less than half the checks failed"

    # Output the failing risks
    if failing_risks:
        print(f"Failing risks: {', '.join(failing_risks)}")
    else:
        print("No specific failing risks identified.")

    print(f"This contract is considered {risk_level}.")

run_analysis()

