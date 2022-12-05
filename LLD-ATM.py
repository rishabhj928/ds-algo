
from enum import Enum
from abc import ABC, abstractmethod

class ATM:
    def __init__(self):
        self.atmId = 0
        self.location = Address()
        self.cashDispenser = CashDispenser()
        self.screen = Screen()
        self.cardReader = CardReader()
        self.keyPad = KeyPad()
        self.cashDeposit = CashDeposit()
        self.chequeDeposit = ChequeDeposit()
        self.bankService = BankService()

class Address:
    def __init__(self):
        self.pinCode = 0
        self.street = ""
        self.city = ""
        self.state = ""
        self.country = ""

class CashType(Enum):
    FIFTY = 0
    HUNDRED = 1
    FIVE_HUNDRED = 2

class CashDispenser:
    def __init__(self):
        self.cashAvailable = CashType()

    def dispenseCash(self, amount: int):
        pass

class Cash:
    def __init__(self):
        self.cashType = CashType()
        self.serialNumber = ""

class Screen:
    def display(message: str):
        pass

class CardReader:
    def fetchDetails() -> CardInfo:
        pass

class CardInfo:
    def __init__(self):
        self.cardType = Enum("CardType", "CREDIT, DEBIT")
        self.bank = Bank()
        self.cardNum = ""
        self.expiry = ""
        self.cvv = 0
        self.withdrawLimit = 0

class KeyPad:
    def getInput(self) -> str:
        pass

class Bank:
    def __init__(self):
        self.name = ""
        self.location = Address()
        self.atmList = []

class BankService(ABC):
    @abstractmethod
    def isValidUser(self, pin: str, card: CardInfo) -> bool:
        pass

    @abstractmethod
    def getCustomerDetails(self, card: CardInfo) -> Customer:
        pass

    @abstractmethod
    def excuteTxn(self, txn: Txn) -> TxnDetail:
        pass

class BankA(BankService):
    def isValidUser(self, pin: str, card: CardInfo) -> bool:
        pass
    
    def getCustomerDetails(self, card: CardInfo) -> Customer:
        pass
    
    def excuteTxn(self, txn: Txn) -> TxnDetail:
        pass

class BankB(BankService):
    def isValidUser(self, pin: str, card: CardInfo) -> bool:
        pass
    
    def getCustomerDetails(self, card: CardInfo) -> Customer:
        pass

    def excuteTxn(self, txn: Txn) -> TxnDetail:
        pass

class BankServiceFactory:
    def getBankServiceObj(self, card: CardInfo) -> BankService:
        # returns BankA / BankB based on card info
        pass

class Customer:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.cardInfo = CardInfo()
        self.account = Account()
        self.bankService = BankService()
        self.customerStatus = Enum("CustomerStatus", "BLOCKED, ACTIVE, CLOSED")

class Account:
    def __init__(self):
        self.accountNumber = ""
        self.availableBalance = 0

class Txn:
    def __init__(self):
        self.txnId = 0
        self.sourceAccount = Account()
        self.txnDate = ""

class Deposit(Txn):
    def __init__(self):
        self.amount = 0

class ChequeDeposit(Deposit):
    def getCheque(self):
        pass

class CashDeposit(Deposit):
    def getCash(self) -> List[Cash]:
        pass

class WithDraw(Txn):
    def __init__(self):
        self.amount = 0

class Transfer(Txn):
    def __init__(self):
        self.amount = 0
        self.destinationAccount = Account()

class TxnDetail:
    def __init__(self):
        self.txnStatus = Enum("TxnStatus", "PENDING, CANCELLED, SUCCESS, ERROR")
        self.sourceAccount = ""
        self.txnDate = ""
        self.txnType = Enum("TxnType", "WITHDRAW, DEPOSIT, TRANSFER")
        self.txnId = 0
