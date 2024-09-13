from models.erc20eventsignature import Erc20EventSignature
from web3 import Web3
from xml.dom import NotFoundErr


class EtherumLogProvider:
    def __init__(self):
        API_KEY = "7f8e5798697e439081f97071e451aea1"
        INFURA_URL = f'https://mainnet.infura.io/v3/{API_KEY}'

        self.web3_client = Web3(Web3.HTTPProvider(INFURA_URL))

    def get_approvals(self, address: str):
        if not self.web3_client.is_address(address):
            raise NotFoundErr("This address was not found")

        logs = self.get_logs(address, Erc20EventSignature.APPROVE_EVENT)

        for log in logs:
            amount = self.web3_client.to_int(log["data"])
            coin_address = (log["address"])
            print(f"approved {amount} of {coin_address}")

        return logs

    def get_logs(self, address, event_type: Erc20EventSignature):
        payload = {
            "jsonrpc": "2.0",
            "id": 0,
            "method": "eth_getLogs",
            "params": {
                "fromBlock": "0",
                "toBlock": "latest",
                "address": address,
                "topics": []
            }}

        if event_type:
            payload["params"]["topics"].append(self.web3_client.to_hex(text=event_type.value))

        return self.web3_client.eth.get_logs(payload)
