import re

import qrcode
from eth_account.signers.local import LocalAccount
from web3 import Web3

from data import config
from data.models import Settings


def retrieve() -> None:
    w3 = Web3()
    w3.eth.account.enable_unaudited_hdwallet_features()
    settings = Settings()
    text = 'Mnemonic\tPrivate key\tAddress'
    mnemonic_or_private_key = settings.mnemonic_or_private_key
    if re.match((r'\w+ ' * 12)[:-1], mnemonic_or_private_key):
        account: LocalAccount = w3.eth.account.from_mnemonic(mnemonic_or_private_key)
        text += f'\n{mnemonic_or_private_key}\t{account.privateKey.hex()}\t{account.address}'
        qrcode.make(account.address).save(config.QR_CODE_IMAGE)

    elif re.match(r'\w' * 64, mnemonic_or_private_key):
        account: LocalAccount = w3.eth.account.from_key(mnemonic_or_private_key)
        text += f'\n\t{account.privateKey.hex()}\t{account.address}'
        qrcode.make(account.address).save(config.QR_CODE_IMAGE)

    else:
        text += '\n' + mnemonic_or_private_key

    with open(config.WALLET_FILE, mode='w') as file:
        file.write(text)

    print(f'''Done!
QR code with the wallet address saved to the {config.LIGHTGREEN_EX}{config.QR_CODE_IMAGE}{config.RESET_ALL} file.
Save the mnemonic and private key from the {config.LIGHTGREEN_EX}{config.WALLET_FILE}{config.RESET_ALL} file to a password manager and {config.RED}DELETE THE FILE{config.RESET_ALL}!'''
          )
