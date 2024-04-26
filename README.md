# Meng

![Alt](https://repobeats.axiom.co/api/embed/42b94a1c432bc7812ecee4afdefcc26c5a51f6df.svg "Repobeats analytics image")

## Overview

Meng is a Python application that analyzes the security and potential risks of Ethereum tokens using the GoPlus Token Security API and Rug Pull Detection API. It generates a detailed report in Markdown format and stores the analysis data in an SQLite database. The results should not be considered financial/investment advice and are for informational purposes only. Users should perform their own due diligence and [DYOR](https://hackmd.io/@wbnns/dyor-do-your-own-research).

## Features

- Retrieves token security and rug pull risk data from the GoPlus API
- Generates a comprehensive Markdown report with the analysis results
- Saves the report to a file named after the token symbol and current date
- Stores the JSON data returned by each API, along with the contract address and the current date, in an SQLite database

## Prerequisites

- Python 3.x
- `goplus` library

## Installation

1. Clone the repository:
   `git clone https://github.com/your-username/meng.git`

2. Install the required dependencies:
   `pip install goplus`

## Usage

1. Run the script:
   `python main.py`

2. Enter the token contract address when prompted.

3. The script will analyze the token and generate a report. The report will be displayed in the console and saved as a Markdown file in the `reports` folder with the filename format `<token_symbol>_<current_date>.md`.

4. The JSON data returned by each API, along with the contract address and the current date, will be stored in an SQLite database named `token_data.db`.

## Report Format

The generated report includes the following sections:

- Token Analysis Report
- Date
- Report date
- Token Security Analysis
- Raw JSON data from the token security API
- Token Security Analysis Breakdown
- Open Source
- Proxy Contract
- Mint Function
- Owner Address
- Can Take Back Ownership
- Owner Can Change Balance
- Hidden Owner
- Selfdestruct
- External Call
- In DEX
- Buy Tax
- Sell Tax
- Can't Buy
- Can't Sell All
- Slippage Modifiable
- Honeypot
- Transfer Pausable
- Blacklist
- Whitelist
- Anti Whale
- Anti Whale Modifiable
- Trading Cooldown
- Personal Slippage Modifiable
- Token Name
- Token Symbol
- Holder Count
- Total Supply
- Creator Address
- Creator Balance
- Creator Percent
- LP Holder Count
- LP Total Supply
- Is True Token
- Is Airdrop Scam
- Is In Trust List
- Other Potential Risks
- Note
- Fake Token
- Rug Pull Security Analysis
- Raw JSON data from the rug pull security API
- Rug Pull Security Analysis Breakdown
- Owner Name
- Owner Address
- Owner Type
- Privilege Withdraw
- Cannot Withdraw
- Contract Verified
- Blacklist Function
- Contract Name
- Self-Destruct
- Potential Approval Abuse
- Proxy Contract

## Database Schema

The SQLite database `token_data.db` contains a table named `token_data` with the following schema:

- `id` (INTEGER): Primary key
- `contract_address` (TEXT): The token contract address
- `token_security_data` (TEXT): The JSON data returned by the token security API
- `rug_pull_data` (TEXT): The JSON data returned by the rug pull security API
- `date` (TEXT): The date when the analysis was performed

## License

This project is licensed under the [MIT License](LICENSE.md).
