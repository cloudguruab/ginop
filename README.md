<h1 align="center">GINOP</h1>

<p align="center">Read <a href="https://usesource.app">here</a> for community information</p>

</p>

<h1 align="center">Blockchain based workflow identifier.</h1>

<div align="center">
A libaray that allows workflows to manage themselves
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
Managing workflows can be time consuming. Most managers find approving employee logs, times and pay a little more challenging to maintain over time. This solution is built to develop a web3 approach to a real world workflow problem. An idea inspired by <a href="https://github.com/usesource/">The Source Project</a> I was able to bring smart contract approval to a simple workflow environment. 

## 💅 Features

- 🚀 Dummy proof API for handling common workflows
- 🛡 Easily manage employee data
- 🚀 Equipped with an in memory on chain cryptographic verficiation system
- 🛡 Built-in protection for workflow duplication
- 🚀 Easy to set up and integrate
- 🛡 Written in Python, Javascript, and sprinkled with a little React


## 👨‍💻 Install

```bash
pipenv install .
```

```bash
cd main/static && npm install 
```

## 🔨 Usage

- Coming soon...

## On Chain Platform 
Ginop provides in memory blockchain for saftey and security. This decision is based on a cost effective approach to implementing smart contract verification. The onChain approach to employee workflow will allow self service check-in/check-out stations. This original idea is based on proof of concept and will expand deeper into other implementations such as geospatial, sms, and biometric based proof of concepts.

#### 📱 API (Coming Soon...)

- Our smart contracts will govern our endpoints allowing for new workflows to progress overtime.

```
#create transaction
clock-in/ 

#sign transaction
clock-out/ 
```

#### 👇 Smart Contract (Coming Soon...)

- Here is an example snippet of writing a smart contract using web3.py for more specific visual of our smart contract check the README under `main/README.md`

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

#### 🌈 Docs (Coming Soon...)

- WIP

## 🔗 Links
- [Home page](https://usesource.app/)
