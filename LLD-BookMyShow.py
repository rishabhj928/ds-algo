
from typing import List
from enum import Enum

class BMSService:
    def __init__(self):
        self.cinemas = []
    
    def getMovies(self, date: str, city: str) -> List[Movie]:
        pass

    def getCinemaHalls(self, city: str) -> List[CinemaHall]:
        pass

class CinemaHall:
    def __init__(self):
        self.cinemaHallId = 0
        self.cinemaHallName = ""
        self.address = Address()
        self.audiList = [Audi]
    
    def getMovies(self, dateList: List[str]) -> List[Movie]:
        pass

    def getShows(self, dateList: List[str]) -> List[Show]:
        pass

class Address:
    def __init__(self):
        self.pinCode = 0
        self.street = ""
        self.city = ""
        self.state = ""
        self.country = ""

class Audi:
    def __init__(self):
        self.audiId = 0
        self.audiName = ""
        self.totalSeats = 0

class Show:
    def __init__(self):
        self.ShowId = 0
        self.movie = Movie()
        self.startTime = ""
        self.endTime = ""
        self.cinemaPlayedAt = CinemaHall()
        self.seats = [Seat()]

class Seat:
    def __init__(self):
        self.seatId = 0
        self.seatType = Enum("SeatType", "DELUX, VIP, ECONOMY, OTHER")
        self.seatStatus = Enum("SeatStatus", "BOOKED, AVAILABLE, RESERVED, NOT_AVAILABLE")
        self.price = 0

class Genre(Enum):
    SCI_FI, DRAMA, COMEDY, FANTASY, HORROR = 0, 1, 2, 3, 4

class Movie:
    def __init__(self):
        self.movieName = ""
        self.movieId = 0
        self.durationInMinutes = 0
        self.langauge = ""
        self.genre = Genre()
        self.releaseDate = ""
        self.cityShowMap = {"city1": ["show1", "show2"], "city2": ["show3", "show2"]}

class Search:
    def searchByName(self, name: str) -> List[Movie]:
        pass

    def searchByGenre(self, genre: Genre) -> List[Movie]:
        pass

    def searchByLanguage(self, language: str) -> List[Movie]:
        pass

    def searchByDate(self, releaseDate: str) -> List[Movie]:
        pass

class User:
    def __init__(self):
        self.userId = 0
        self.searchObj = Search()

class SystemMember(User):
    def __init__(self):
        self.account = Account()
        self.name = ""
        self.email = ""
        self.address = Address()

class Member(SystemMember):
    def makeBooking(self, booking: Booking) -> Booking:
        pass

    def getBooking(self) -> List[str]:
        pass

class Admin(SystemMember):
    def addMovie(self, movie: Movie) -> bool:
        pass

    def addShow(self, show: Show) -> bool:
        pass

class Account:
    def __init__(self):
        self.userName = ""
        self.password = ""

class Booking:
    def __init__(self):
        self.bookingId = 0
        self.bookingDate = ""
        self.member = Member()
        self.show = Show()
        self.audi = Audi()
        self.bookingStatus = Enum("BookingStatus", "REQUESTED, CONFIRMED, PENDING, CANCELLED")
        self.seats = [Seat]
        self.paymentObj = Payment()
    
    def makePayment(self, payment: Payment) -> bool:
        pass

class Payment:
    def __init__(self):
        self.amount = 0
        self.paymentDate = ""
        self.txnId = 0
        self.paymentStatus = Enum("PaymentStatus", "UNPAID, PENDING, COMPLETED, DECLINED, CANCELLED, REFUNDED")
    
