# Ginop Blockchain

Here you can see an example snippet of our handler for provider types. This will take a different shape as more providers are added.

- Example snippet

```python
class Controller:
    
    def __init__(self, name:str, admin_level:str):
        """
        configuration of connector instance
        
        :param name: identifier of admin interface
        """
        self.name = name
        
    def __repr__(self):
        return f'<Admin: {self.name} >'
    
    def __str__(self):
        return f'<Admin: {self.name} >'
    
    def __bool__(self):        
        state = MetaFormat.HTTP_PROVIDER.value
        
        if state.isConnected(): 
            print(f'{http_provider} is connected...') #log something
            return True
        
        return False 
    
    def est_conf(self):
        """
        depending on admin level will delegate provider type,
        grab provider and check against admin level.
        
        :rtype profile: dict object for frontend meta data rendered to user
        """
        if Admin.__bool__(self) != False:
            return {"state": "connected..."} 
        
        return {"state": "no connection present"}
```


### Blockchain

Ginop uses a proof of work system for basic api navigation. The overall usecase for this implementation is to extend into a consesus form of validation for work. Our current api will support basic blockchain functionality from within its proof of work state but overtime will take shape to allowing access to your own personal private chain and also have connectivity to other platforms like etherium as well.

- Example snippet
```python
def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)
    
    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                        transactions=self.unconfirmed_transactions,
                        timestamp=time.time(),
                        previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index
```