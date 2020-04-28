class Blockchain:
    def __init__(self):
        self.ledger = []

    def deploy(self, smart_contract):
        self.ledger += smart_contract

    def get_contract(self, id):
        return self.ledger[id]

