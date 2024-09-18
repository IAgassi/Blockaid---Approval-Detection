import argparse
from providers.etherum_provider import EtherumLogProvider


if __name__ == '__main__':
    log_provider = EtherumLogProvider()
    parser = argparse.ArgumentParser(description="Fetch all approvals for a given Ethereum address")
    parser.add_argument("--address", type=str, required=False, help="Ethereum address to check approvals for")

    args = parser.parse_args()
    address = args.address

    approvals = log_provider.get_approvals(address)
