import logging

from data import config
from data.models import ProgramActions
from functions.check_internet_connection import check_internet_connection
from functions.create_files import create_files
from functions.generate import generate
from functions.retrieve import retrieve
from functions.send import send
from functions.sign import sign

if __name__ == '__main__':
    create_files()
    while True:
        check_internet_connection()
        action = None
        print('''Select the action:
1) Generate a mnemonic;
2) Retrieve a private key and an address from a mnemonic or a private key;
3) Sign a sending transaction;
4) Send a signed transaction;
5) Exit.''')

        try:
            action = int(input('> '))
            print()
            if action == ProgramActions.Generate:
                generate()

            elif action == ProgramActions.Retrieve:
                retrieve()

            elif action == ProgramActions.SignSendingTransaction:
                sign()

            elif action == ProgramActions.SendSignedTransaction:
                send()

            else:
                break

        except ValueError:
            print(f"{config.RED}You didn't enter a number!{config.RESET_ALL}")

        except BaseException as e:
            logging.exception('main')
            print(f'\n{config.RED}Something went wrong: {e}{config.RESET_ALL}\n')

        if action:
            input(f'\nPress {config.LIGHTGREEN_EX}Enter{config.RESET_ALL} to exit.\n')
            break
