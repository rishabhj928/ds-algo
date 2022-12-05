
class ParkingLot:
    def __init__(self):
        self.parkingFloors = [ParkingFloor(), ParkingFloor()]
        self.entrances = [Entrance(), Entrance(), Entrance()]
        self.exits = [Exit(), Exit(), Exit()]
        self.address = Address()
        self.parkingLotName = ""
    
    def isParkingAvailable(self, vehicle: Vehicle) -> bool:
        pass

    def updateParkingAttendant(self, parkingAttendant: ParkingAttendant, gateId: int) -> bool:
        pass

class ParkingFloor:
    def __init__(self):
        self.levelId = 0
        self.isFull = False
        self.parkingSpaces = [ParkingSpace(), ParkingSpace()]
        self.displayBoard = [DisplayBoard(), DisplayBoard()]

class Gate:
    def __init__(self):
        self.gateId = 0
        self.parkingAttendant = ParkingAttendant()

class Entrance(Gate):
    def getParkingTicket(self, vehicle: Vehicle) -> ParkingTicket:
        pass

class Exit(Gate):
    def payForParking(self, ticket: ParkingTicket, paymentType: PaymentType) -> ParkingTicket:
        pass

class Address:
    def __init__(self):
        self.pinCode = 0
        self.street = ""
        self.city = ""
        self.state = ""
        self.country = ""

class ParkingSpace:
    def __init__(self):
        self.spaceId = 0
        self.isFree = False
        self.costPerHour = 0
        self.vehicle = Vehicle()
        self.parkingSpaceType = Enum("ParkingSpaceType", "BIKE_PARKING, CAR_PARKING, TRUCK_PARKING")

class ParkingDisplayBoard:
    def __init__(self):
        self.freeSpotAvailable = {ParkingSpaceType(): 0,}
    
    def updateFreeSpotsAvailable(self, parkingSpaceType: ParkingSpaceType, spaces: int):
        pass

class Account:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.empId = 0
        self.address = Address()

class Admin(Account):
    def addFloor(self, parkingLot: ParkingLot, floor: ParkingFloor) -> bool:
        pass

    def addParkingSpace(self, floor: ParkingFloor, space: ParkingSpace) -> bool:
        pass

    def addDisplayBoard(self, floor: ParkingFloor, displayBoard: ParkingDisplayBoard) -> bool:
        pass

class ParkingAttendant(Account):
    def __init__(self):
        self.paymentService = PaymentService()
    
    def processVehicleEntry(self, vehicle: Vehicle) -> bool:
        pass

    def processPayment(self, ticket: ParkingTicket, paymentType: PaymentType) -> PaymentInfo:
        pass

class Vehicle:
    def __init__(self):
        self.licenseNumber = ""
        self.vehicleType = Enum("VehicleType", "BIKE, CAR, TRUCK")
        self.parkingTicket = ParkingTicket()
        self.paymentInfo = PaymentInfo()

class ParkingTicket:
    def __init__(self):
        self.ticketId = 0
        self.levelId = 0
        self.spaceId = 0
        self.entryDateTime = ""
        self.exitDateTime = ""
        self.parkingSpaceType = Enum("ParkingSpaceType", "BIKE_PARKING, CAR_PARKING, TRUCK_PARKING")
        self.totalCost = 0
        self.parkingTicketStatus = Enum("ParkingTicketStatus", "PAID, ACTIVE")
    
    def updateTotalCost(self):
        pass

    def updateVehicleExitTime(self, time: str):
        pass

class PaymentType(Enum):
    CASH, CREDIT_CARD, DEBIT_CARD, UPI = 0, 1, 2, 3

class Payment:
    def makePayment(self, ticket: ParkingTicket, paymentType: PaymentType) -> PaymentInfo:
        pass

class PaymentInfo:
    def __init__(self):
        self.amount = 0
        self.paymentDate = ""
        self.txnId = 0
        self.ticket = ParkingTicket()
        self.status = Enum("PaymentStatus", "UNPAID, PENDING, COMPLETED, DECLINED, CANCELLED, REFUNDED")

