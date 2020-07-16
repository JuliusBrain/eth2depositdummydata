# Deposit dummy data generation
This script generates dummy data for Deposit Contract found on Goerli network. Script is based off oficial testing setup for deposit contract found here: https://github.com/ethereum/eth2.0-specs/tree/dev/deposit_contract

1. Run `python3 -m venv venv`
2. `source venv/bin/activate` to activate venv
3. `pip3 install -r requirements.txt` to install all dependencies
4. `python3 generate.py 32` to generate dummy deposit data with amount for deposit of 32 Eth
5. `deactivate` to exit venv.