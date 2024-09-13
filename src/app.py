from eth_typing import HexStr

from models.erc20eventsignature import Erc20EventSignature
import argparse
from xml.dom import NotFoundErr
from web3 import Web3

API_KEY = "7f8e5798697e439081f97071e451aea1"
INFURA_URL = f'https://mainnet.infura.io/v3/{API_KEY}'

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

ERC20_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "owner", "type": "address"},
            {"indexed": True, "name": "spender", "type": "address"},
            {"indexed": False, "name": "value", "type": "uint256"}
        ],
        "name": "Approval",
        "type": "event"
    }
]


def convert_to_hex(event_name: str) -> HexStr:
    converted = web3.to_hex(text=event_name)
    return converted


def get_approvals(address: str):
    if not web3.is_address(address):
        raise NotFoundErr("This address was not found")

    contract = web3.eth.contract(address=address, abi=ERC20_ABI)

    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "eth_getLogs",
        "params": {
            "fromBlock": "0",
            "toBlock": "latest",
            "address": address,
            "topics": [convert_to_hex(Erc20EventSignature.APPROVE_EVENT.value)]
        }}

    logs = web3.eth.get_logs(payload)

    for log in logs:
        amount = web3.to_int(log["data"])
        coin_address = (log["address"])
        print(f"approved {amount} of {coin_address}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fetch all approvals for a given Ethereum address")
    # TODO: required must be true when sending in the code
    parser.add_argument("--address", type=str, required=False, help="Ethereum address to check approvals for")

    args = parser.parse_args()
    address = args.address

    address = "0x005e20fCf757B55D6E27dEA9BA4f90C0B03ef852"

    # filter_events(address)
    get_approvals(address)
