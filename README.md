<h1 align="center">GINOP</h1>

<p align="center">Read <a href="https://usesource.app">here</a> for community information</p>

</p>

<div align="center">
A wrapper built around django. 
</div>

  <p align="center">
    <br />
    <a href="https://github.com/cloudguruab/ginop"><strong>Docs coming soon »</strong></a>
    <br />
  <br/>
    <a href="https://github.com/cloudguruab/ginop/issues">Report Bug</a>
    ·
    <a href="https://github.com/cloudguruab/ginop/discussions">Request Feature</a>
    ·
    <a href="https://github.com/cloudguruab/ginop/">Blog coming soon</a>
  </p>
  
## 📦 Why
Ginop provides a wrapper around a proof of work chain and public-chain connector to allow for your own custom service implementations on the blockchain in django. An idea inspired by <a href="https://github.com/usesource/">The Source Project</a> I was able to bring private chain and public chain connectors together. 

## 💅 Features

- 🚀 API built on top of a blockchain.
- 🛡 Easily manage your service provider, chain events or api.
- 🚀 Equipped with an proof of work chain and public chain connector.
- 🚀 Easy to set up and integrate. 
- 🛡 Written in Python.


## 👨‍💻 Install

```bash
pipenv install .
```

## 🕹️ Running test

```python
pipenv run pytest tests/
```

## 🧃 Starting api

```python
python3 manage.py runserver
```

## 📵 Making migrations

```python
python3 manage.py makemigrations && python3 manage.py migrate
```


## 🔨 Usage

- The ginop API is a service built on top of a proof of work blockchain. This is still in development but will serve as a platform for building services over your own private chain, or over well-known public chains like etherium and more. To use the public chain connectors you need to install [Ganache](https://trufflesuite.com/docs/ganache/overview) provided by the truffle framework. Here you can connect directly to the truffle framework and write smart contracts, manage blocks and create transactions. 

## On Chain Platform 
Ginop provides in memory blockchain for saftey and security. This decision is based on a cost effective approach to implementing smart contract verification. The onChain approach to web3 workflow will allow self service into your own private chain. This original idea is based on proof of work and will expand deeper into other implementations such as geospatial, sms, and biometric based proof of concepts.

#### 📱 API

- The API's will be available soon to review as working examples to build off of.

```python
class PrivateChainView(APIView):
    """
    Example endpoint for handling actions on the private chain.
    """
        
    def get(self, request, format=None, *args, **kwargs):
        chain_data = []
        
        for block in blockchain.chain:
            chain_data.append(block.__dict__)
        
        context = json.dumps({"length": len(chain_data),
                        "chain": chain_data})
        
        return Response(context, status=status.HTTP_200_OK)
```

#### 🦄 Blocks

Here is a snippet of the blocks.

```python
class Block:
    
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index: BlockTypes.index = index
        self.transactions: BlockTypes.transactions = transactions
        self.timestamp: BlockTypes.timestamp = timestamp
        self.previous_hash: BlockTypes.previous_hash = previous_hash
        self.nonce: BlockTypes.nonce = nonce
    
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
```

### 🧠 Providers

- Public providers exist using the truffle framework to connect to in-memory chains like Ganache, or public chains like etherium or others.

```python
class MetaFormat(Enum):
    HTTP_PROVIDER = Web3(Web3.HTTPProvider(os.environ.get('ON_CHAIN_URL')))

    #add your own providers below.
  
```

#### 👇 Smart Contract (Coming Soon...)

- `dev/` folder is comprised of working scripts for the private chain, public chain providers, and on chain action handlers like writing smart contracts, governing transactions and more. The smart contracts will be written using `web3.py`.

```python
import json
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Set a default account to sign transactions - this account is unlocked with Ganache
web3.eth.defaultAccount = web3.eth.accounts[0]

# Greeter contract ABI
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

# Greeter contract address - convert to checksum address
address = web3.toChecksumAddress('') # FILL ME IN

# Initialize contract
contract = web3.eth.contract(address=address, abi=abi)\

# Read the default greeting
print(contract.functions.greet().call())

# Set a new greeting
tx_hash = contract.functions.setGreeting('HEELLLLOOOOOO!!!').transact()

# Wait for transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)

# Display the new greeting value
print('Updated contract greeting: {}'.format(
    contract.functions.greet().call()
))
```

#### 🌈 Docs

[Docs coming soon...](usesource.app/)

## 🔗 Links
- [Home page](https://usesource.app/)
- [What is the blockchain](https://kauri.io/#communities/Getting%20started%20with%20dapp%20development/blockchain-explained/)
- [What is a smart contract](https://kauri.io/#collections/Ethereum%20101/ethereum-101-part-5-the-smart-contract/)

