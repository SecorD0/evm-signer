import qrcode
from eth_account.hdaccount import Mnemonic
from eth_account.signers.local import LocalAccount
from web3 import Web3

from data import config


def generate() -> None:
    w3 = Web3()
    w3.eth.account.enable_unaudited_hdwallet_features()
    mnemonic = Mnemonic().generate()
    account: LocalAccount = w3.eth.account.from_mnemonic(mnemonic)
    qrcode.make(account.address).save(config.QR_CODE_IMAGE)
    wallet = f'''Mnemonic\tPrivate key\tAddress
{mnemonic}\t{account.privateKey.hex()}\t{account.address}'''
    with open(config.WALLET_FILE, mode='w') as file:
        file.write(wallet)

    print(f'''Done!
QR code with the wallet address saved to the {config.LIGHTGREEN_EX}{config.QR_CODE_IMAGE}{config.RESET_ALL} file.
Save the mnemonic and private key from the {config.LIGHTGREEN_EX}{config.WALLET_FILE}{config.RESET_ALL} file to a password manager and {config.RED}DELETE THE FILE{config.RESET_ALL}!'''
          )
