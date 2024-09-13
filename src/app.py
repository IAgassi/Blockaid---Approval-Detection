import argparse
from providers.etherum_provider import EtherumLogProvider


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


if __name__ == '__main__':
    log_provider = EtherumLogProvider()

    parser = argparse.ArgumentParser(description="Fetch all approvals for a given Ethereum address")
    parser.add_argument("--address", type=str, required=True, help="Ethereum address to check approvals for")

    args = parser.parse_args()
    address = args.address

    address = "0x005e20fCf757B55D6E27dEA9BA4f90C0B03ef852"

    approvals = log_provider.get_approvals(address)
