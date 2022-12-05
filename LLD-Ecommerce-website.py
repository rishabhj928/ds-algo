
from enum import Enum
from typing import List
from abc import ABC, abstractmethod

class Customer:
    def __init__(self, cart: 'ShoppingCart', search: 'Search', customerId: int):
        self.cart = cart
        self.search = search
        self.customerId = customerId
    
    def getShoppingCart(self, customerId: int) -> 'ShoppingCart':
        pass
    
    def addItemToCart(self, item: 'Item'):
        pass

    def updateItemToCart(self, item: 'Item'):
        pass
    
    def removeItemFromCart(self, item: 'Item'):
        pass

class Guest(Customer):
    def createNewAccount(self) -> 'Account':
        pass

class User(Customer):
    def __init__(self, account: 'Account'):
        self.account = account
    
    def getAccount(self) -> 'Account':
        return self.account

class Seller(User):
    def addProduct(product: 'Product'):
        pass

class Buyer(User):
    def __init__(self, order: 'Order'):
        self.order = order
    
    def addReview(review: 'Review'):
        pass

    def placeOrder(cart: 'Cart'):
        pass

class Account:
    def __init__(self, name: str, email: str, phone: str, userName: str, password: str, address: List['Address'], status: 'AccountStatus'):
        self.name = name
        self.email = email
        self.phone = phone
        self.userName = userName
        self.password = password
        self.address = address
        self.status = status
    
    def getEmail(self) -> str:
        return self.email
    
    def getPhone(self) -> str:
        return self.phone

class Address:
    def __init__(self, pinCode: int, street: str, city: str, state: str, country: str):
        self.pinCode = pinCode
        self.street = street
        self.city = city
        self.state = state
        self.country = country

class AccountStatus(Enum):
    ACTIVE = 1
    BLOCKED = 2
    INACTIVE = 3

class ShoppingCart:
    def __init__(self, items: List['Item'], cartValue: float):
        self.items = items
        self.cartValue = cartValue
    
    def addItem(item: 'Item'):
        pass

    def updateItem(item: 'Item'):
        pass
    
    def deleteItem(item: 'Item'):
        pass
    
    def checkoutItems():
        pass

    def getItems() -> List['Item']:
        pass

    def getCartValue() -> float:
        pass

class Item:
    def __init__(self, product: 'Product', qty: int):
        self.product = product
        self.qty = qty

class Product:
    def __init__(self, pid: int, name: str, price: float, desc: str, cat: 'Category', seller: 'Seller', reviews: List['Reviews']):
        self.productId = pid
        self.productName = name
        self.price = price
        self.desc = desc
        self.cat = cat
        self.seller = seller
        self.reviews = reviews

class Category(Enum):
    ELECTRONICS = 1
    FURNITURE = 2
    GROCERY = 3

class Review:
    def __init__(self, details: str, reviewer: 'Buyer', rating: int):
        self.details = details
        self.reviewer = reviewer
        self.rating = rating

class Search:
    def searchByName(name: str) -> List['Product']:
        pass

    def searchByCategory(cat: 'Category') -> List['Product']:
        pass

class Order:
    def __init__(self, orderId, orderItems: List['Item'], orderValue: float, buyer: 'Buyer', date: str, notify: 'NotifyService', logs: List['Log']):
        self.orderId = orderId
        self.orderItems = orderItems
        self.orderValue = orderValue
        self.buyer = buyer
        self.date = date
        self.notify = notify
        self.logs = logs
    
    def placeOrder() -> 'OrderStatus':
        pass

    def trackOrder() -> 'OrderStatus':
        pass

    def addOrderLogs():
        pass

    def makePayment(type: 'PaymentType') -> 'PaymentStatus':
        pass

class OrderStatus(Enum):
    PACKED = 1
    SHIPPED = 2
    IN_TRANSIT = 3
    OUT_FOR_DELIVERY = 4
    DELIVERED = 5
    RTO = 6

class PaymentStatus(Enum):
    SUCCESS = 1
    ERROR = 2
    CANCELLED = 3
    REFUND_INITIATE = 4
    REFUNDED = 5

class PaymentType(Enum):
    CREDIT_CARD = 1
    DEBIT_CARD = 2
    NET_BANKING = 3
    UPI = 4

class Log:
    def __init__(self, desc: str, date: str, status: 'OrderStatus'):
        self.desc = desc
        self.date = date
        self.status = status


class NotificationService:
    def sendNotification(domain: 'NotificationDomain') -> bool:
        notification = None
        message = None

        type = domain.getNotificationType()

        if type == 'EMAIL':
            notification = EmailNotification()
            message = Message("orders@amazon.com", domain.getUser().getAccount().getEmail(), "Your Order is ...")
        elif type == "WHATSAPP":
            notification = WhatsappNotification()
            message = Message("9876543210", domain.getUser().getAccount().getPhone(), "Your Order is ...")
        else:
            notification = SMSNotification()
            message = Message("9876543210", domain.getUser().getAccount().getPhone(), "Your Order is ...")
        
        return notification.sendNotification(message)

class NotificationDomain:
    def __init__(self, nid: "str", type: 'NotificationType', user: 'User'):
        self.nid = nid
        self.type = type
        self.user = user
    
    def getUser(self) -> 'User':
        return self.user
    
    def getNotificationType(nid: str) -> str:
        pass

class Message:
    def __init__(self, fromUser, toUser, message):
        self.fromUser = fromUser
        self.toUser = toUser
        self.message = message

class Notification(ABC):
    @abstractmethod
    def sendNotification(message: 'Message') -> bool:
        pass

class EmailNotification(Notification):
    def sendNotification(message: 'Message') -> bool:
        pass

class WhatsappNotification(Notification):
    def sendNotification(message: 'Message') -> bool:
        pass

class SMSNotification(Notification):
    def sendNotification(message: 'Message') -> bool:
        pass

