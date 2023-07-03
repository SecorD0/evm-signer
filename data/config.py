import os
import platform
import sys
from pathlib import Path

from colorama import Fore, Style

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()

else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

if platform.system() == 'Windows':
    LIGHTGREEN_EX = ''
    RED = ''
    RESET_ALL = ''

else:
    LIGHTGREEN_EX = Fore.LIGHTGREEN_EX
    RED = Fore.RED
    RESET_ALL = Style.RESET_ALL

FILES_DIR = os.path.join(ROOT_DIR, 'files')

WALLET_FILE = os.path.join(FILES_DIR, 'wallet.txt')
SETTINGS_FILE = os.path.join(FILES_DIR, 'settings.json')

QR_CODE_IMAGE = os.path.join(FILES_DIR, 'qr_code.png')
