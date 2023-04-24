import logging
import os.path

import cv2
import numpy
from web3 import Web3

from data import config
from data.models import Settings


def send():
    try:
        settings = Settings()
        if not settings.rpc:
            print(f"{config.RED}You didn't specify an RPC!{config.RESET_ALL}")
            return

        if os.path.exists(config.QR_CODE_IMAGE):
            qr_code = cv2.imdecode(numpy.fromfile(config.QR_CODE_IMAGE, dtype=numpy.uint8), cv2.IMREAD_UNCHANGED)
            signed_tx, _, _ = cv2.QRCodeDetector().detectAndDecode(qr_code)
            print(f'\nQR code on the path {config.LIGHTGREEN_EX}{config.QR_CODE_IMAGE}{config.RESET_ALL} is found.\n')

        else:
            print(
                f"\nQR code on the path {config.LIGHTGREEN_EX}{config.QR_CODE_IMAGE}{config.RESET_ALL} isn't found, "
                f"so enter the hash of the signed transaction."
            )
            signed_tx = input('> ')
            print()

        if signed_tx:
            w3 = Web3(Web3.HTTPProvider(endpoint_uri=settings.rpc))
            tx_hash = w3.eth.send_raw_transaction(transaction=signed_tx)
            print(f'The transaction was successfully sent: {config.LIGHTGREEN_EX}{tx_hash.hex()}{config.RESET_ALL}')
            if os.path.exists(config.QR_CODE_IMAGE):
                os.remove(config.QR_CODE_IMAGE)

        else:
            print(f"{config.RED}You didn't enter the hash!{config.RESET_ALL}")

    except BaseException as e:
        logging.exception('send')
        print(f'{config.RED}Failed to send transaction: {e}{config.RESET_ALL}')
