import os
import re
import sqlite3
from datetime import datetime
from goplus.token import Token
from goplus.rug_pull import RugPull

def analyze_token(address):
    """
    Analyze token security and rug pull risk for a given token address.

    Args:
        address (str): The address of the token contract to analyze.

    Returns:
        dict: A dictionary containing the token security and rug pull analysis results.
    """
    try:
        chain_id = "1"  # Ethereum mainnet

        # Analyze token security
        token_data = Token(access_token=None).token_security(
            chain_id=chain_id, addresses=[address]
        )

        # Analyze rug pull risk
        rug_pull_data = RugPull().rug_pull_security(
            chain_id=chain_id, address=address
        )

        # Combine the results into a single dictionary
        result = {
            "token_security": token_data.to_dict(),
            "rug_pull_security": rug_pull_data.to_dict()
        }

        return result

    except Exception as e:
        print(f"Error occurred during analysis: {str(e)}")
        return None

def generate_report(result, current_date):
    """
    Generate a Markdown report from the analysis results.

    Args:
        result (dict): The analysis results dictionary.
        current_date (str): The current date.

    Returns:
        str: The generated Markdown report.
    """
    report = f"# Token Analysis Report - {current_date}\n\n"

    # Token Security Analysis
    report += "## Token Security Analysis\n"
    report += "```json\n"
    report += str(result["token_security"]) + "\n"
    report += "```\n\n"

    # Token Security Analysis Breakdown
    report += "### Token Security Analysis Breakdown\n"
    token_data = list(result["token_security"]["result"].values())
    if token_data:
        token_data = token_data[0]
        report += f"- Open Source: {'Yes' if token_data.get('is_open_source') == '1' else 'No' if token_data.get('is_open_source') == '0' else 'Unknown'}\n"
        report += f"- Proxy Contract: {'Yes' if token_data.get('is_proxy') == '1' else 'No' if token_data.get('is_proxy') == '0' else 'Unknown'}\n"
        report += f"- Mint Function: {'Yes' if token_data.get('is_mintable') == '1' else 'No' if token_data.get('is_mintable') == '0' else 'Unknown'}\n"
        report += f"- Owner Address: {token_data.get('owner_address', 'Unknown')}\n"
        report += f"- Can Take Back Ownership: {'Yes' if token_data.get('can_take_back_ownership') == '1' else 'No' if token_data.get('can_take_back_ownership') == '0' else 'Unknown'}\n"
        report += f"- Owner Can Change Balance: {'Yes' if token_data.get('owner_change_balance') == '1' else 'No' if token_data.get('owner_change_balance') == '0' else 'Unknown'}\n"
        report += f"- Hidden Owner: {'Yes' if token_data.get('hidden_owner') == '1' else 'No' if token_data.get('hidden_owner') == '0' else 'Unknown'}\n"
        report += f"- Selfdestruct: {'Yes' if token_data.get('selfdestruct') == '1' else 'No' if token_data.get('selfdestruct') == '0' else 'Unknown'}\n"
        report += f"- External Call: {'Yes' if token_data.get('external_call') == '1' else 'No' if token_data.get('external_call') == '0' else 'Unknown'}\n"

        report += f"- In DEX: {'Yes' if token_data.get('is_in_dex') == '1' else 'No' if token_data.get('is_in_dex') == '0' else 'Unknown'}\n"
        report += f"- Buy Tax: {token_data.get('buy_tax', 'Unknown')}\n"
        report += f"- Sell Tax: {token_data.get('sell_tax', 'Unknown')}\n"
        report += f"- Can't Buy: {'Yes' if token_data.get('cannot_buy') == '1' else 'No' if token_data.get('cannot_buy') == '0' else 'Unknown'}\n"
        report += f"- Can't Sell All: {'Yes' if token_data.get('cannot_sell_all') == '1' else 'No' if token_data.get('cannot_sell_all') == '0' else 'Unknown'}\n"
        report += f"- Slippage Modifiable: {'Yes' if token_data.get('slippage_modifiable') == '1' else 'No' if token_data.get('slippage_modifiable') == '0' else 'Unknown'}\n"
        report += f"- Honeypot: {'Yes' if token_data.get('is_honeypot') == '1' else 'No' if token_data.get('is_honeypot') == '0' else 'Unknown'}\n"
        report += f"- Transfer Pausable: {'Yes' if token_data.get('transfer_pausable') == '1' else 'No' if token_data.get('transfer_pausable') == '0' else 'Unknown'}\n"
        report += f"- Blacklist: {'Yes' if token_data.get('is_blacklisted') == '1' else 'No' if token_data.get('is_blacklisted') == '0' else 'Unknown'}\n"
        report += f"- Whitelist: {'Yes' if token_data.get('is_whitelisted') == '1' else 'No' if token_data.get('is_whitelisted') == '0' else 'Unknown'}\n"
        report += f"- Anti Whale: {'Yes' if token_data.get('is_anti_whale') == '1' else 'No' if token_data.get('is_anti_whale') == '0' else 'Unknown'}\n"
        report += f"- Anti Whale Modifiable: {'Yes' if token_data.get('anti_whale_modifiable') == '1' else 'No' if token_data.get('anti_whale_modifiable') == '0' else 'Unknown'}\n"
        report += f"- Trading Cooldown: {'Yes' if token_data.get('trading_cooldown') == '1' else 'No' if token_data.get('trading_cooldown') == '0' else 'Unknown'}\n"
        report += f"- Personal Slippage Modifiable: {'Yes' if token_data.get('personal_slippage_modifiable') == '1' else 'No' if token_data.get('personal_slippage_modifiable') == '0' else 'Unknown'}\n"

        report += f"- Token Name: {token_data.get('token_name', 'Unknown')}\n"
        report += f"- Token Symbol: {token_data.get('token_symbol', 'Unknown')}\n"
        report += f"- Holder Count: {token_data.get('holder_count', 'Unknown')}\n"
        report += f"- Total Supply: {token_data.get('total_supply', 'Unknown')}\n"
        report += f"- Creator Address: {token_data.get('creator_address', 'Unknown')}\n"
        report += f"- Creator Balance: {token_data.get('creator_balance', 'Unknown')}\n"
        report += f"- Creator Percent: {token_data.get('creator_percent', 'Unknown')}\n"

        report += f"- LP Holder Count: {token_data.get('lp_holder_count', 'Unknown')}\n"
        report += f"- LP Total Supply: {token_data.get('lp_total_supply', 'Unknown')}\n"

        report += f"- Is True Token: {'Yes' if token_data.get('is_true_token') == '1' else 'No' if token_data.get('is_true_token') == '0' else 'Unknown'}\n"
        report += f"- Is Airdrop Scam: {'Yes' if token_data.get('is_airdrop_scam') == '1' else 'No' if token_data.get('is_airdrop_scam') == '0' else 'Unknown'}\n"
        report += f"- Is In Trust List: {'Yes' if token_data.get('trust_list') == '1' else 'Unknown'}\n"

        report += f"- Other Potential Risks: {token_data.get('other_potential_risks', 'Unknown')}\n"
        report += f"- Note: {token_data.get('note', 'Unknown')}\n"

        fake_token = token_data.get('fake_token')
        if fake_token:
            report += f"- Fake Token: {'Yes' if fake_token['value'] == 1 else 'No'}\n"
            report += f"  - True Token Address: {fake_token['true_token_address']}\n"
        else:
            report += f"- Fake Token: Unknown\n"
    else:
        report += "No token security data available.\n"

    report += "\n"

    # Rug Pull Security Analysis
    report += "## Rug Pull Security Analysis\n"
    report += "```json\n"
    report += str(result["rug_pull_security"]) + "\n"
    report += "```\n\n"

    # Rug Pull Security Analysis Breakdown
    report += "### Rug Pull Security Analysis Breakdown\n"
    rug_pull_data = result["rug_pull_security"]["result"]
    if rug_pull_data:
        owner = rug_pull_data.get("owner")
        if owner:
            report += f"- Owner Name: {owner.get('owner_name', 'Unknown')}\n"
            report += f"- Owner Address: {owner.get('owner_address', 'Unknown')}\n"
            report += f"- Owner Type: {owner.get('owner_type', 'Unknown')}\n"
        else:
            report += "- Owner: No owner information available.\n"

        report += f"- Privilege Withdraw: {'Yes' if rug_pull_data.get('privilege_withdraw') == 1 else 'No' if rug_pull_data.get('privilege_withdraw') == 0 else 'Unknown'}\n"
        report += f"- Cannot Withdraw: {'Yes' if rug_pull_data.get('withdraw_missing') == 1 else 'No' if rug_pull_data.get('withdraw_missing') == 0 else 'Unknown'}\n"
        report += f"- Contract Verified: {'Yes' if rug_pull_data.get('is_open_source') == 1 else 'No'}\n"
        report += f"- Blacklist Function: {'Yes' if rug_pull_data.get('blacklist') == 1 else 'No' if rug_pull_data.get('blacklist') == 0 else 'Unknown'}\n"
        report += f"- Contract Name: {rug_pull_data.get('contract_name', 'Unknown')}\n"
        report += f"- Self-Destruct: {'Yes' if rug_pull_data.get('selfdestruct') == 1 else 'No' if rug_pull_data.get('selfdestruct') == 0 else 'Unknown'}\n"
        report += f"- Potential Approval Abuse: {'Yes' if rug_pull_data.get('approval_abuse') == 1 else 'No' if rug_pull_data.get('approval_abuse') == 0 else 'Unknown'}\n"
        report += f"- Proxy Contract: {'Yes' if rug_pull_data.get('is_proxy') == 1 else 'No' if rug_pull_data.get('is_proxy') == 0 else 'Unknown'}\n"
    else:
        report += "No rug pull security data available.\n"

    return report

def save_report(report, filename, current_date):
    """
    Save the report to a Markdown file with the given filename and current date.

    Args:
        report (str): The generated report.
        filename (str): The filename for the report.
        current_date (str): The current date.
    """
    # Create the "reports" folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Replace any special characters or spaces in the filename with underscores
    filename = re.sub(r'[^\w\-_\. ]', '_', filename)

    report_file = f"reports/{filename}_{current_date}.md"
    with open(report_file, "w") as file:
        file.write(report)
    print(f"Report saved as {report_file}")

def store_data_in_database(token_security_data, rug_pull_data, address, current_date):
    """
    Store the JSON data returned by each API in the SQLite database.

    Args:
        token_security_data (dict): The token security data.
        rug_pull_data (dict): The rug pull data.
        address (str): The contract address.
        current_date (str): The current date.
    """
    # Connect to the database (creates a new file if it doesn't exist)
    conn = sqlite3.connect("token_data.db")
    cursor = conn.cursor()

    # Create the "token_data" table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS token_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contract_address TEXT,
            token_security_data TEXT,
            rug_pull_data TEXT,
            date TEXT
        )
    """)

    # Insert the token data into the "token_data" table
    cursor.execute("""
        INSERT INTO token_data (contract_address, token_security_data, rug_pull_data, date)
        VALUES (?, ?, ?, ?)
    """, (address, str(token_security_data), str(rug_pull_data), current_date))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Token data stored in the database.")

def main():
    """
    Main function to run the Meng app.
    """
    # Get user input for token address
    address = input("Enter the token contract address: ")

    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Analyze the token
    result = analyze_token(address)

    if result:
        # Generate the Markdown report
        report = generate_report(result, current_date)
        print(report)

        # Determine the filename for the report
        token_data = list(result["token_security"]["result"].values())
        if token_data:
            token_symbol = token_data[0].get("token_symbol", "unknown")
        else:
            token_symbol = address

        # Save the report to a file
        save_report(report, token_symbol, current_date)

        # Store the JSON data in the database
        store_data_in_database(result["token_security"], result["rug_pull_security"], address, current_date)
    else:
        print("Failed to analyze the token.")

if __name__ == "__main__":
    main()