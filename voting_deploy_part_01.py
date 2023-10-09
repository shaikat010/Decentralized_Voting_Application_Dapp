import json
from web3 import Web3
from solcx import compile_standard, install_solc

with open("./Election.sol", "r") as file:
    election_list_file = file.read()

# We add these two lines that we forgot from the video!
# print("Installing...")
# install_solc("0.8.0")

# Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Election.sol": {"content": election_list_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled_code_election.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["Election.sol"]["Election"]["evm"]["bytecode"]["object"]

# get abi
abi = json.loads(compiled_sol["contracts"]["Election.sol"]["Election"]["metadata"])["output"]["abi"]

# w3 = Web3(Web3.HTTPProvider(os.getenv("SEPOLIA_RPC_URL")))
# chain_id = 4
# For connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337

# this is the ganache-cli public and private key
my_address = "0x9138a8378c821AF24ac6c68b1bd06e26963b615C"
private_key = "0x08d14efb1904243a50dfb8241d98ddcce93dd39ccaa511556c69332e08216843"


