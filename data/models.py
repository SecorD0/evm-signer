import json

from data.config import SETTINGS_FILE


class ProgramActions:
    Generate = 1
    Retrieve = 2
    SignSendingTransaction = 3
    SendSignedTransaction = 4


class AutoRepr:
    """Contains a __repr__ function that automatically builds the output of a class using all its variables."""

    def __repr__(self) -> str:
        values = ('{}={!r}'.format(key, value) for key, value in vars(self).items())
        return '{}({})'.format(self.__class__.__name__, ', '.join(values))


class Singleton:
    """A class that implements the singleton pattern."""
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls)

        return cls._instances[cls]


class Settings(Singleton, AutoRepr):
    def __init__(self) -> None:
        json_dict = json.load(open(SETTINGS_FILE, encoding='utf-8'))

        self.rpc: str = json_dict['rpc']
        self.mnemonic_or_private_key: str = json_dict['mnemonic_or_private_key']
        self.chain_id: int = json_dict['chain_id']
        self.nonce: int = json_dict['nonce']
        self.token_contract_address: str = json_dict['token_contract_address']
        self.decimals: int = json_dict['decimals']
        self.float_amount: float = json_dict['float_amount']
        self.recipient: str = json_dict['recipient']
        self.maxFeePerGas: float = json_dict['gas_price']['maxFeePerGas']
        self.maxPriorityFeePerGas: float = json_dict['gas_price']['maxPriorityFeePerGas']
        self.gas_limit: int = json_dict['gas_limit']
