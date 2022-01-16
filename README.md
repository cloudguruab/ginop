<h1 align="center">GINOP</h1>

<p align="center">Read <a href="https://usesource.app">here</a> for community information</p>

</p>

<h1 align="center">Blockchain based service wrapper</h1>

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


## 🔨 Usage (Coming soon...)

- Coming soon...

## On Chain Platform 
Ginop provides in memory blockchain for saftey and security. This decision is based on a cost effective approach to implementing smart contract verification. The onChain approach to web3 workflow will allow self service into your own private chain. This original idea is based on proof of work and will expand deeper into other implementations such as geospatial, sms, and biometric based proof of concepts.

#### 📱 API (Coming Soon...)

- Our smart contracts will govern our endpoints allowing for new workflows to progress overtime.

```python
class UserView(viewsets.ModelViewSet):
    """
    Endpoint that allows users to be viewed or edisted
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
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

#### 👇 Smart Contract (Coming Soon...)

```python
WIP
```

#### 🌈 Docs (Coming Soon...)

- WIP

## 🔗 Links
- [Home page](https://usesource.app/)
- [What is the blockchain](https://kauri.io/#communities/Getting%20started%20with%20dapp%20development/blockchain-explained/)
- [What is a smart contract](https://kauri.io/#collections/Ethereum%20101/ethereum-101-part-5-the-smart-contract/)

