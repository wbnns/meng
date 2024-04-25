
# Meng: Ethereum Token Risk Analyzer

Meng is an open-source tool designed to analyze Ethereum token contracts for potential risks using the GoPlus Token Risk Classification API. It evaluates a set of risk-indicating and safety attributes to determine the overall risk level of the token contract.

## Features

- **Token Risk Analysis**: Evaluates Ethereum contract addresses to identify attributes that indicate higher risks or safety.
- **Proxy Contract Support**: Handles proxy contracts by allowing further analysis on implementation contract addresses.
- **Command-Line Interface**: Provides a CLI for easy input of Ethereum contract addresses and displays analysis results.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine
- Access to the GoPlus Token Risk Classification API

### Installation

First, clone the repository to your local machine:

\```bash
git clone https://github.com/yourusername/meng.git
cd meng
\```

Install the required dependencies:

\```bash
pip install -r requirements.txt
\```

### Configuration

To run Meng, simply use the command below. Ensure you have set up any necessary API access configurations within your script:

\```bash
python main.py
\```

## Usage

Run the script from the command line:

\```bash
python main.py
\```

Enter the Ethereum contract address when prompted. The tool will perform the risk analysis and display the results in the command line.

## Contributing

Contributions to Meng are welcome! Please adhere to the following steps for contributing:

1. Fork the repository.
2. Create your feature branch (\`git checkout -b my-new-feature\`).
3. Commit your changes (\`git commit -am 'Add some feature'\`).
4. Push to the branch (\`git push origin my-new-feature\`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
