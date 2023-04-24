import re

import qrcode
from eth_account.signers.local import LocalAccount
from eth_utils import to_wei, to_checksum_address
from web3 import Web3

from data import config
from data.models import Settings


def sign() -> None:
    settings = Settings()
    if not all((
            settings.mnemonic_or_private_key, settings.chain_id, settings.decimals, settings.float_amount,
            settings.recipient, settings.maxFeePerGas, settings.gas_limit
    )):
        print(f'{config.RED}Set all mandatory settings!{config.RESET_ALL}')
        return

    tx_params = {
        'chainId': settings.chain_id,
        'nonce': settings.nonce,
        'gas': settings.gas_limit
    }
    str_tx_params = f'''chainId: {config.LIGHTGREEN_EX}{settings.chain_id}{config.RESET_ALL}
nonce: {config.LIGHTGREEN_EX}{settings.nonce}{config.RESET_ALL}
gas: {config.LIGHTGREEN_EX}{settings.gas_limit}{config.RESET_ALL}
'''
    if settings.maxPriorityFeePerGas or settings.chain_id in (42161,):
        tx_params.update({
            'maxFeePerGas': to_wei(number=settings.maxFeePerGas, unit='gwei'),
            'maxPriorityFeePerGas': to_wei(number=settings.maxPriorityFeePerGas, unit='gwei')
        })
        str_tx_params += f'''maxFeePerGas: {config.LIGHTGREEN_EX}{settings.maxFeePerGas}{config.RESET_ALL} GWei
maxPriorityFeePerGas: {config.LIGHTGREEN_EX}{settings.maxPriorityFeePerGas}{config.RESET_ALL} GWei
'''

    else:
        tx_params.update({
            'gasPrice': to_wei(number=settings.maxFeePerGas, unit='gwei')
        })
        str_tx_params += f'gasPrice: {config.LIGHTGREEN_EX}{settings.maxFeePerGas}{config.RESET_ALL} GWei\n'

    w3 = Web3()
    w3.eth.account.enable_unaudited_hdwallet_features()
    recipient = to_checksum_address(settings.recipient)
    amount = int(settings.float_amount * 10 ** settings.decimals)
    if settings.token_contract_address:
        contract = w3.eth.contract(
            address=to_checksum_address(settings.token_contract_address),
            abi=[
                {
                    'constant': False,
                    'inputs': [{'name': '_to', 'type': 'address'}, {'name': '_value', 'type': 'uint256'}],
                    'name': 'transfer',
                    'outputs': [], 'payable': False,
                    'stateMutability': 'nonpayable',
                    'type': 'function'
                }
            ]
        )
        tx_params.update({
            'to': contract.address,
            'data': contract.encodeABI('transfer', args=(recipient, amount)),
        })
        str_tx_params += f'token: {config.LIGHTGREEN_EX}{settings.token_contract_address}{config.RESET_ALL}\n'

    else:
        tx_params.update({
            'to': recipient,
            'value': amount
        })
        str_tx_params += f'token: {config.LIGHTGREEN_EX}coin{config.RESET_ALL}\n'

    str_tx_params += f'''decimals: {config.LIGHTGREEN_EX}{settings.decimals}{config.RESET_ALL}
amount: {config.LIGHTGREEN_EX}{settings.float_amount}{config.RESET_ALL}
recipient: {config.LIGHTGREEN_EX}{recipient}{config.RESET_ALL}'''
    mnemonic_or_private_key = settings.mnemonic_or_private_key
    if re.match((r'\w+ ' * 12)[:-1], mnemonic_or_private_key):
        account: LocalAccount = w3.eth.account.from_mnemonic(mnemonic_or_private_key)

    elif re.match(r'\w' * 64, mnemonic_or_private_key):
        account: LocalAccount = w3.eth.account.from_key(mnemonic_or_private_key)

    else:
        print(f'{config.RED}Wrong mnemonic or private key!{config.RESET_ALL}')
        return

    signed_transaction = w3.eth.account.sign_transaction(
        transaction_dict=tx_params, private_key=account.key
    ).rawTransaction.hex()
    qrcode.make(signed_transaction).save(config.QR_CODE_IMAGE)
    print(f'''{str_tx_params}

Signed data: {config.LIGHTGREEN_EX}{signed_transaction}{config.RESET_ALL}.
QR code saved to the {config.LIGHTGREEN_EX}{config.QR_CODE_IMAGE}{config.RESET_ALL} file.''')
