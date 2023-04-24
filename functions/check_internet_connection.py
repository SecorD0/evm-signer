from urllib.request import urlopen

from data import config


def check_internet_connection() -> None:
    try:
        urlopen('http://google.com', timeout=5)
        print(f'\n{config.RED}You connected to the Internet!{config.RESET_ALL}\n')

    except:
        pass
