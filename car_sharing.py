from blockchain import Blockchain
from contract import SmartContract, BookingDetails

blockchain = Blockchain()


# TODO: remove id from Owner deploy, owner shouldn't be responsible for contract id
# TODO: add checking everything like in contract.py

class Owner:
    def __init__(self, balance):
        self.contract = SmartContract
        self.details = BookingDetails
        self.balance = balance

    def add_car_to_rent(self, day_price, car_info):
        car = Car(car_info)
        self.details = BookingDetails(car, day_price)

    def deploy(self, ether, contract_id):
        global blockchain
        self.contract = SmartContract(contract_id)
        self.contract.owner_deposit(ether)
        blockchain.deploy(self.contract)

    def withdraw_earnings(self):
        self.balance += self.contract.withdraw_earnings()

    def allow_car_usage(self):
        self.contract.allow_car_usage()


class Customer:
    def __init__(self, balance):
        self.balance = balance
        self.contract = SmartContract

    def request_book(self, ether, contract_id):
        self.contract = blockchain.get_contract(contract_id)
        if not self.contract:
            return
        self.contract.client_deposit(ether)

    def retrieve_balance(self):
        self.balance += self.contract.retrieve_balance()

    def end_car_rental(self):
        self.contract.end_car_rental()

    def access_car(self):
        self.contract.get_car()


class Car:
    def __init__(self, car_info, **kwargs):
        self.car_info = car_info
        self.additional = kwargs
        self.is_rented = False
        self.allowed_to_use = False

    def access(self):
        print("Car have been accessed")
        self.is_rented = True

    def end_rental(self):
        self.is_rented = False

    def allow_to_use(self):
        self.allowed_to_use = True





