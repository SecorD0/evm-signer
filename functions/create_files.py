import json
import os
from typing import Optional

from data import config


def create_files() -> None:
    if not os.path.isdir(config.FILES_DIR):
        os.mkdir(config.FILES_DIR)

    try:
        current_settings: Optional[dict] = json.load(open(config.SETTINGS_FILE, encoding='utf-8'))

    except FileNotFoundError:
        current_settings = {}

    settings = {
        'rpc': '',
        'mnemonic_or_private_key': '',
        'chain_id': 0,
        'nonce': 0,
        'token_contract_address': '',
        'decimals': 18,
        'float_amount': 0.0,
        'recipient': '',
        'gas_price': {'maxFeePerGas': 0.0, 'maxPriorityFeePerGas': 0.0},
        'gas_limit': 21000
    }

    for key, value in settings.items():
        if key not in current_settings:
            current_settings.update({key: value})

    with open(config.SETTINGS_FILE, mode='w', encoding='utf-8') as f:
        json.dump(current_settings, f, indent=2)
