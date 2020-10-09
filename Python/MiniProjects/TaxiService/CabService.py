import math


class Places:
    _locationsMap = {"Los-Angeles": (5.3, 2.7),
                     "San-Jose": (3.9, 5.0),
                     "San-Francisco": (7, 5),
                     "Fremont": (10, 6.9),
                     "Santa-Clara": (16.7, 6.8)
                     }

    def __init__(self, _locationsMap):
        self._locationsMap = _locationsMap

    def getLocation(self, locationName: str) -> tuple:
        return self._locationsMap[locationName]

    def isLocationPresent(self, locationName: str) -> bool:
        return locationName in self._locationsMap

    def getDistance(self, location1: tuple, location2: tuple) -> int:
        location1 = self._locationsMap[location1]
        location2 = self._locationsMap[location2]

        distance = math.sqrt(
            (location1[0] - location2[0])**2 + (location1[1] - location2[1])**2)
        return math.ceil(distance)


class RideClient:
    _id = 0

    __slots__ = ["customerName", "customerEmail", "id"]

    def __init__(self, customerName):
        self.customerName = customerName
        self.customerEmail = ""
        self.id = RideClient._id
        RideClient._id += 1


class InitiateBookingRequest:
    _id = 0

    __slots__ = ["id", "customerId", "customerName",
                 "customerEmail", "pickUpLocation", "dropOffLocation", "distance", "assignedDriver"]

    def __init__(self):
        self.id = None
        self.customerId = None
        self.customerName = None
        self.customerEmail = None
        self.pickUpLocation = ""
        self.dropOffLocation = ""
        self.distance = 0
        self.assignedDriver = None

    @staticmethod
    def create():
        bookingRequest = InitiateBookingRequest()
        bookingRequest.id = InitiateBookingRequest._id
        InitiateBookingRequest._id += 1
        return bookingRequest


class RideBookingOrder:
    _id = 0

    __slots__ = ["id", "customerId", "customerName",
                 "customerEmail", "pickUpLocation", "dropOffLocation", "distance", "price", "tax", "assignedDriver"]

    def __init__(self):
        self.id = None
        self.customerId = None
        self.customerName = None
        self.customerEmail = None
        self.pickUpLocation = ""
        self.dropOffLocation = ""
        self.distance = 0
        self.price = 0.00
        self.tax = 0.00
        self.assignedDriver = None

    @staticmethod
    def create():
        bookingOrder = RideBookingOrder()
        bookingOrder.id = RideBookingOrder._id
        RideBookingOrder._id += 1
        return bookingOrder


class CustomerBill:

    __slots__ = ["id", "customerId", "customerName",
                 "customerEmail", "pickUpLocation", "dropOffLocation", "distance", "assignedDriver", "price", "tax", "totalCost"]

    def __init__(self):
        self.customerId = None
        self.customerName = None
        self.customerEmail = None
        self.pickUpLocation = ""
        self.dropOffLocation = ""
        self.distance = 0
        self.assignedDriver = None
        self.price = 0.00
        self.tax = 0.00
        self.totalCost = 0.00


class Drivers:
    _drivers = {
        1: {"name": "Sean", "dedicatedRoutes": ["Los-Angeles", "San-Jose"], "Status": "Available", "CarModel": "Hyundai"},
        2: {"name": "Dan", "dedicatedRoutes": ["Santa-Clara", "Fremont"], "Status": "Available", "CarModel": "Honda"},
        3: {"name": "Pat", "dedicatedRoutes": ["Santa-Clara", "San-Diego"], "Status": "Available", "CarModel": "Mazda"},
        4: {"name": "Jenny", "dedicatedRoutes": ["Cupertino", "Fremont"], "Status": "Available", "CarModel": "Mercedes"},
        5: {"name": "Aladin", "dedicatedRoutes": ["San-Diego", "San-Francisco"], "Status": "Available", "CarModel": "Volvo"},
    }

    def __init__(self, _drivers):
        self._drivers = _drivers

    def getEligibleDrivers(self, locationName):
        eligible_drivers = {key: value for key, value in self._drivers.items(
        ) if locationName in value["dedicatedRoutes"]}
        return eligible_drivers

    def assignDriver(self, locationName):
        availableDriverKeys = self.getEligibleDrivers(locationName).keys()
        if not availableDriverKeys:
            return None
        availableDriver = list(availableDriverKeys)[-1]
        self._drivers[availableDriver]["Status"] = "Booked"
        driverToRemove = {key: value for key,
                          value in self._drivers.items() if key == availableDriver}
        assignedDriver = driverToRemove, self._drivers.pop(availableDriver)
        return assignedDriver[0]

    def getAvailableDrivers(self):
        return self._drivers


class CabService:
    _costPerMile = 2.5
    _tax = [0.05, 0.10, 0.15]

    def __init__(self, chaffeur: Drivers, route: Places):
        self.chaffeur = chaffeur
        self.route = route
        self._patronageRecord = {}

    def getTax(self):
        return self._tax

    def bookARide(self, bookingRequest: InitiateBookingRequest) -> RideBookingOrder:
        rideOrder = RideBookingOrder.create()
        rideOrder.customerId = bookingRequest.customerId
        rideOrder.customerName = bookingRequest.customerName
        rideOrder.customerEmail = bookingRequest.customerEmail
        rideOrder.pickUpLocation = bookingRequest.pickUpLocation
        rideOrder.dropOffLocation = bookingRequest.dropOffLocation
        rideOrder.distance = bookingRequest.distance
        rideOrder.assignedDriver = bookingRequest.assignedDriver

        rideOrder = self._pairWithADriver(rideOrder)

        if rideOrder != None:
            self._patronageRecord[rideOrder.id] = rideOrder
            return rideOrder

    def _pairWithADriver(self, rideOrder: RideBookingOrder) -> RideBookingOrder:
        if rideOrder.pickUpLocation not in self.route._locationsMap:
            return None

        rideOrder.assignedDriver = self.chaffeur.assignDriver(
            rideOrder.pickUpLocation)

        return rideOrder

    def _computeDistance(self, rideOrder: RideBookingOrder) -> RideBookingOrder:
        rideOrder.distance = self.route.getDistance(rideOrder.pickUpLocation,
                                                    rideOrder.dropOffLocation)
        return rideOrder

    def _costEstimator(self, rideOrder: RideBookingOrder) -> RideBookingOrder:
        totalDistance = self.route.getDistance(
            rideOrder.pickUpLocation, rideOrder.dropOffLocation)
        rideOrder.price = self._costPerMile * totalDistance
        return rideOrder

    def _endRide(self, rideOrder: RideBookingOrder) -> CustomerBill:
        invoice = CustomerBill()

        if rideOrder.price <= 10:
            totalCost = rideOrder.price * self._tax[0] + rideOrder.price
        elif rideOrder.price > 10 and rideOrder.price < 20:
            totalCost = rideOrder.price * self._tax[1] + rideOrder.price
        else:
            totalCost = rideOrder.price * self._tax[2] + rideOrder.price

        totalCost = totalCost

        invoice.totalCost = totalCost
        invoice.customerId = rideOrder.customerId
        invoice.customerName = rideOrder.customerName
        invoice.customerEmail = rideOrder.customerEmail
        invoice.pickUpLocation = rideOrder.pickUpLocation
        invoice.dropOffLocation = rideOrder.dropOffLocation
        invoice.distance = rideOrder.distance
        invoice.price = rideOrder.price
        invoice.assignedDriver = rideOrder.assignedDriver

        if rideOrder.price <= 10:
            taxApplied = self._tax[0]
        elif rideOrder.price > 10 and rideOrder.price < 20:
            taxApplied = self._tax[1]
        elif rideOrder.price >= 20:
            taxApplied = self._tax[2]
        invoice.tax = taxApplied
        return invoice
