<h1><p align="center">evm-signer</p></h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [DISCLAIMER](#DISCLAIMER)
- [Description](#Description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Docker (image)](#Docker-image)
    - [Docker (building)](#Docker-building)
    - [Source code](#Source-code)
- [Sample settings](#Sample-settings)
- [Updating](#Updating)
  - [Windows](#Windows-1)
  - [GitHub image](#GitHub-image)
  - [Self-built image](#Self-built-image)
  - [Source code](#Source-code-1)
- [Useful commands](#Useful-commands)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">DISCLAIMER</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program has no injections — you can make the code review to make sure. Any cases of third parties gaining access to your wallets aren't the fault of the developer, but of you or another person. Keep your sensitive data in a safe place.

⠀By using this program you have agreed to the above and have no and won't have claims against its developer.



<h1><p align="center">Description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program allows you to:
- Generate a mnemonic (offline).
- Retrieve a private key and an address from a mnemonic or a private key (offline).
- Sign a sending transaction (offline).
- Send a signed transaction.



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[evm-signer](https://github.com/SecorD0/evm-signer)



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `files` — a user files directory:
  - `qr_code.png` — a QR code with an address or a signed transaction;
  - `settings.json` — a JSON file for program setup;
  - `wallet.txt` — a text file with a generated mnemonic or an inserted mnemonic or private key.
- `evm-signer.exe` / `app.py` — an executable file that runs the program.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/evm-signer/releases).
2. Create a folder and put the EXE file in it.
3. Disconnect from the Internet.
4. Run the program to create necessary files.
5. Generate a wallet, if necessary, and exit the program.
6. Configure the `settings.json`:
   - `rpc` — an RPC URL of the network in which you want to send tokens (used when sending a signed transaction).
   - `mnemonic_or_private_key` — a mnemonic or a private key of a wallet that which will sign the transaction.
   - `chain_id` — the chain ID in which the transaction will be sent. This can be found on the [Chainlist](https://chainlist.org) website.
   - `nonce` — the wallet nonce. This can be found on the address page in Blockscan explorer.
   - `token_contract_address` — a token contract address or an empty string to send coin.
   - `decimals` — the coin or token decimals. This can be found on the token page in Blockscan explorer.
   - `float_amount` — the amount of coin or token to send.
   - `recipient` — the coin or token recipient.
   - `gas_price` — several gas price parameters that determine the type of transaction (`type-2` if `maxPriorityFeePerGas` is specified, otherwise `type-0`):
     - `maxFeePerGas` — the bare minimum you will be charged to send a transaction on the network. This value can be found in Blockscan explorer.
     - `maxPriorityFeePerGas` — the tip to a miner.
   - `gas_limit` — the gas limit.
7. Run the program again and enter `3` to sign the transaction.
8. Send a hash of the signed transaction on a device that has internet access and send it to network. You can make it via this program (you need to provide a QR-code or a hash).
9. Delete `qr_code.png` and clear the value of `mnemonic_or_private_key` in the settings.
10. Connect to the Internet.
11. In addition, there are other functions:
    - Generate a mnemonic.
    - Retrieve a private key and an address from a mnemonic or a private key.
    - Send a signed transaction.


<h2><p align="center">Docker (image)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/evm-signer/files:/program/files --name evm-signer ghcr.io/secord0/evm-signer:main
```
3. Generate a wallet, if necessary, and exit the program.
4. Configure the `settings.json`:
   - `rpc` — an RPC URL of the network in which you want to send tokens (used when sending a signed transaction).
   - `mnemonic_or_private_key` — a mnemonic or a private key of a wallet that which will sign the transaction.
   - `chain_id` — the chain ID in which the transaction will be sent. This can be found on the [Chainlist](https://chainlist.org) website.
   - `nonce` — the wallet nonce. This can be found on the address page in Blockscan explorer.
   - `token_contract_address` — a token contract address or an empty string to send coin.
   - `decimals` — the coin or token decimals. This can be found on the token page in Blockscan explorer.
   - `float_amount` — the amount of coin or token to send.
   - `recipient` — the coin or token recipient.
   - `gas_price` — several gas price parameters that determine the type of transaction (`type-2` if `maxPriorityFeePerGas` is specified, otherwise `type-0`):
     - `maxFeePerGas` — the bare minimum you will be charged to send a transaction on the network. This value can be found in Blockscan explorer.
     - `maxPriorityFeePerGas` — the tip to a miner.
   - `gas_limit` — the gas limit.
5. Run the program again and enter `3` to sign the transaction:
```sh
docker run -it --rm -v $HOME/evm-signer/files:/program/files --name evm-signer ghcr.io/secord0/evm-signer:main
```
6. Send a hash of the signed transaction on a device that has internet access and send it to network. You can make it via this program (you need to provide a QR-code or a hash).
7. Delete `qr_code.png` and clear the value of `mnemonic_or_private_key` in the settings.
8. Connect to the Internet.
9. In addition, there are other functions:
    - Generate a mnemonic.
    - Retrieve a private key and an address from a mnemonic or a private key.
    - Send a signed transaction.


<h2><p align="center">Docker (building)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/evm-signer
```
3. Go to the repository:
```sh
cd evm-signer
```
4. Build an image:
```sh
docker build -t evm-signer .
```
5. Disconnect from the Internet.
6. Run the program to create necessary files:
```sh
docker run -it --rm -v $HOME/evm-signer/:/program --name evm-signer evm-signer
```
7. Generate a wallet, if necessary, and exit the program.
8. Configure the `settings.json`:
   - `rpc` — an RPC URL of the network in which you want to send tokens (used when sending a signed transaction).
   - `mnemonic_or_private_key` — a mnemonic or a private key of a wallet that which will sign the transaction.
   - `chain_id` — the chain ID in which the transaction will be sent. This can be found on the [Chainlist](https://chainlist.org) website.
   - `nonce` — the wallet nonce. This can be found on the address page in Blockscan explorer.
   - `token_contract_address` — a token contract address or an empty string to send coin.
   - `decimals` — the coin or token decimals. This can be found on the token page in Blockscan explorer.
   - `float_amount` — the amount of coin or token to send.
   - `recipient` — the coin or token recipient.
   - `gas_price` — several gas price parameters that determine the type of transaction (`type-2` if `maxPriorityFeePerGas` is specified, otherwise `type-0`):
     - `maxFeePerGas` — the bare minimum you will be charged to send a transaction on the network. This value can be found in Blockscan explorer.
     - `maxPriorityFeePerGas` — the tip to a miner.
   - `gas_limit` — the gas limit.
9. Run the program again and enter `3` to sign the transaction:
```sh
docker run -it --rm -v $HOME/evm-signer/:/program --name evm-signer evm-signer
```
10. Send a hash of the signed transaction on a device that has internet access and send it to network. You can make it via this program (you need to provide a QR-code or a hash).
11. Delete `qr_code.png` and clear the value of `mnemonic_or_private_key` in the settings.
12. Connect to the Internet.
13. In addition, there are other functions:
    - Generate a mnemonic.
    - Retrieve a private key and an address from a mnemonic or a private key.
    - Send a signed transaction.


<h2><p align="center">Source code</p></h2>

1. Install [Python 3.8](https://www.python.org/downloads/).
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/evm-signer
```
3. Go to the repository:
```sh
cd evm-signer
```
4. Set up an environment.
5. Install requirements:
```sh
pip install -r requirements.txt
```
6. Disconnect from the Internet.
7. Run the `app.py` to create necessary files.
8. Generate a wallet, if necessary, and exit the program.
9. Configure the `settings.json`:
   - `rpc` — an RPC URL of the network in which you want to send tokens (used when sending a signed transaction).
   - `mnemonic_or_private_key` — a mnemonic or a private key of a wallet that which will sign the transaction.
   - `chain_id` — the chain ID in which the transaction will be sent. This can be found on the [Chainlist](https://chainlist.org) website.
   - `nonce` — the wallet nonce. This can be found on the address page in Blockscan explorer.
   - `token_contract_address` — a token contract address or an empty string to send coin.
   - `decimals` — the coin or token decimals. This can be found on the token page in Blockscan explorer.
   - `float_amount` — the amount of coin or token to send.
   - `recipient` — the coin or token recipient.
   - `gas_price` — several gas price parameters that determine the type of transaction (`type-2` if `maxPriorityFeePerGas` is specified, otherwise `type-0`):
     - `maxFeePerGas` — the bare minimum you will be charged to send a transaction on the network. This value can be found in Blockscan explorer.
     - `maxPriorityFeePerGas` — the tip to a miner.
   - `gas_limit` — the gas limit.
10. Run the `app.py` again and enter `3` to sign the transaction.
11. Send a hash of the signed transaction on a device that has internet access and send it to network. You can make it via this program (you need to provide a QR-code or a hash).
12. Delete `qr_code.png` and clear the value of `mnemonic_or_private_key` in the settings.
13. Connect to the Internet.
14. In addition, there are other functions:
    - Generate a mnemonic.
    - Retrieve a private key and an address from a mnemonic or a private key.
    - Send a signed transaction.


⠀If you want to build the EXE file by yourself:
- Install `pyinstaller`:
```sh
pip install pyinstaller
```
- Build the EXE file:
```sh
pyinstaller app.py -Fn evm-signer -i images/icons/app.ico --add-binary "images/icons;images/icons" --add-binary "data\wordlist;eth_account\hdaccount\wordlist"
```



<h1><p align="center">Sample settings</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀Ethereum USDC
```json
{
  "rpc": "https://rpc.ankr.com/eth/",
  "mnemonic_or_private_key": "YOUR_PRIVATE_KEY",
  "chain_id": 1,
  "nonce": 0,
  "token_contract_address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
  "decimals": 6,
  "float_amount": 100.5,
  "recipient": "YOUR_ADDRESS",
  "gas_price": {
    "maxFeePerGas": 24.5,
    "maxPriorityFeePerGas": 0.1
  },
  "gas_limit": 65000
}
```

⠀Arbitrum ETH
```json
{
  "rpc": "https://rpc.ankr.com/arbitrum/",
  "mnemonic_or_private_key": "YOUR_PRIVATE_KEY",
  "chain_id": 42161,
  "nonce": 5,
  "token_contract_address": "",
  "decimals": 18,
  "float_amount": 0.205815,
  "recipient": "YOUR_ADDRESS",
  "gas_price": {
    "maxFeePerGas": 0.1,
    "maxPriorityFeePerGas": 0.0
  },
  "gas_limit": 630000
}
```

⠀Arbitrum USDT
```json
{
  "rpc": "https://rpc.ankr.com/arbitrum/",
  "mnemonic_or_private_key": "YOUR_PRIVATE_KEY",
  "chain_id": 42161,
  "nonce": 6,
  "token_contract_address": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
  "decimals": 6,
  "float_amount": 64.1047,
  "recipient": "YOUR_ADDRESS",
  "gas_price": {
    "maxFeePerGas": 0.1,
    "maxPriorityFeePerGas": 0.0
  },
  "gas_limit": 3000000
}
```

⠀Optimism ETH
```json
{
  "rpc": "https://rpc.ankr.com/optimism/",
  "mnemonic_or_private_key": "YOUR_PRIVATE_KEY",
  "chain_id": 10,
  "nonce": 3,
  "token_contract_address": "",
  "decimals": 18,
  "float_amount": 0.01518,
  "recipient": "YOUR_ADDRESS",
  "gas_price": {
    "maxFeePerGas": 0.001,
    "maxPriorityFeePerGas": 0.0
  },
  "gas_limit": 21000
}
```

⠀Optimism USDC
```json
{
  "rpc": "https://rpc.ankr.com/optimism/",
  "mnemonic_or_private_key": "YOUR_PRIVATE_KEY",
  "chain_id": 10,
  "nonce": 4,
  "token_contract_address": "0x7F5c764cBc14f9669B88837ca1490cCa17c31607",
  "decimals": 6,
  "float_amount": 38.25,
  "recipient": "YOUR_ADDRESS",
  "gas_price": {
    "maxFeePerGas": 0.001,
    "maxPriorityFeePerGas": 0.0
  },
  "gas_limit": 52000
}
```

⠀Polygon USDC
```json
{
  "rpc": "https://polygon-rpc.com/",
  "mnemonic_or_private_key": "YOUR_PRIVATE_KEY",
  "chain_id": 137,
  "nonce": 15,
  "token_contract_address": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
  "decimals": 6,
  "float_amount": 30.4147,
  "recipient": "YOUR_ADDRESS",
  "gas_price": {
    "maxFeePerGas": 315.22,
    "maxPriorityFeePerGas": 15.65
  },
  "gas_limit": 100000
}
```



<h1><p align="center">Updating</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file of the new version from the [releases page](https://github.com/SecorD0/evm-signer/releases) and replace the old one with it.


<h2><p align="center">GitHub image</p></h2>

1. Stop the container:
```sh
docker stop evm-signer
```
2. Remove the container:
```sh
docker rm evm-signer
```
3. Update the image:
```sh
docker pull ghcr.io/secord0/evm-signer:main
```


<h2><p align="center">Self-built image</p></h2>

1. Stop the container:
```sh
docker stop evm-signer
```
2. Remove the container:
```sh
docker rm evm-signer
```
3. Go to the repository:
```sh
cd evm-signer
```
4. Update the local files:
```sh
git pull
```
5. Rebuild the image:
```sh
docker build -t evm-signer .
```


<h2><p align="center">Source code</p></h2>

1. Go to the repository:
```sh
cd evm-signer
```
2. Update the local files:
```sh
git pull
```



<h1><p align="center">Useful commands</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀To run the program (GitHub image):
```sh
docker run -it --rm -v $HOME/evm-signer/files:/program/files --name evm-signer ghcr.io/secord0/evm-signer:main
```

⠀To run the program (self-built image):
```sh
docker run -it --rm -v $HOME/evm-signer/:/program --name evm-signer evm-signer
```

⠀To remove the container:
```sh
docker stop evm-signer; docker rm evm-signer
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/evm-signer/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Address of EVM networks (Ethereum, Polygon, BSC, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`
