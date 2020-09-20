import datetime


class CarInventory:
    def __init__(self, numOfCarsInInventory):
        self._numOfCarsInInventory = numOfCarsInInventory

    def countInventory(self):
        return self._numOfCarsInInventory

    def addToInventory(self, numToAdd):
        self._numOfCarsInInventory += numToAdd

    def removeFromInventory(self, numToRemove):
        self._numOfCarsInInventory -= numToRemove

    def canFufillOrder(self, valueToCheck):
        return self._numOfCarsInInventory >= valueToCheck


class Customer:
    _idCounter = 0

    def __init__(self):
        self.id = Customer._idCounter
        Customer._idCounter += 1
        self.name = name
        self.emailAddress = emailAddress


class CarReservationRequest:
    """ Represnts a reservation request made by the customer"""
    _requestID = 0

    def __init__(self):
        self.id = CarReservationRequest.createID()
        self.customerID = None
        self.customerName = None
        self.customerEmailAddress = None
        self.numOfCars = 0
        self.bookingOption = ""

    @staticmethod
    def createID() -> int:
        newRequestID = CarReservationRequest._requestID
        CarReservationRequest._requestID += 1
        return newRequestID


class CarReservationOrder:
    """ Represents that an order was successfully placed"""
    _orderID = 0

    def __init__(self):
        self.id = None
        self.customerID = None
        self.customerName = None
        self.customerEmailAddress = None
        self.numOfCars = 0
        self.bookingOption = ""
        self.bookingPrice = 0.00
        self.bookingTime = None

    @staticmethod
    def createReservationOrder():
        reservationOrder = CarReservationOrder()
        reservationOrder.id = CarReservationOrder._orderID
        CarReservationOrder._orderID += 1
        return reservationOrder


class RentalBill:
    """ Rental Bill associated with a successfully placed order """

    def __init__(self):
        self.totalCost = 0.0
        self.customerName = None
        self.customerEmailAddress = None
        self.numOfCars = 0
        self.bookingOption = ""
        self.bookingTime = None
        self.returnTime = None
        self.bookingPrice = 0.0


class RentalOffice:
    _BOOKING_PRICE_MAP = {"hourly": 5, "daily": 15, "weekly": 60}

    def __init__(self, carInventory: CarInventory):
        self.carInventory = carInventory
        self._carReservationRecord = {}  # key(orderID) Val: CarRentalOrder

    def rentCar(self, reservationRequest: CarReservationRequest):
        """ Returns an instance of carRentalOrder if an order was successfully placed. Returns None Otherwise """

        # Create an Order
        processedReservation = CarReservationOrder.createReservationOrder()
        processedReservation.customerID = reservationRequest.customerID
        processedReservation.customerName = reservationRequest.customerName
        processedReservation.customerEmailAddress = reservationRequest.customerEmailAddress
        processedReservation.numOfCars = reservationRequest.numOfCars
        processedReservation.bookingOption = reservationRequest.bookingOption
        processedReservation.bookingTime = datetime.datetime.now()

        processedReservation = self._applyBookingOption(processedReservation)
        print("#################################I got here", processedReservation)

        if processedReservation != None:
            self._carReservationRecord[processedReservation.id] = processedReservation
        return processedReservation

    def _applyBookingOption(self, processedReservation: CarReservationOrder):
        if processedReservation.bookingOption == "hourly":
            return self._applyHourlyBookingRate(processedReservation)
        elif processedReservation.bookingOption == "daily":
            return self._applyDailyBookingRate(processedReservation)
        elif processedReservation.bookingOption == "weekly":
            return self._applyWeeklyBookingRate(processedReservation)
        return None

    def _applyHourlyBookingRate(self, reservationOrder: CarReservationOrder) -> CarReservationOrder:
        if self.carInventory.canFufillOrder(reservationOrder.numOfCars):
            self.carInventory.removeFromInventory(reservationOrder.numOfCars)
            # set price on the reservation
            reservationOrder.bookingPrice = self._BOOKING_PRICE_MAP.get(
                reservationOrder.bookingOption) * reservationOrder.numOfCars
            return reservationOrder
        return None

    def _applyDailyBookingRate(self, reservationOrder: CarReservationOrder) -> CarReservationOrder:
        if self.carInventory.canFufillOrder(reservationOrder.numOfCars):
            self.carInventory.removeFromInventory(reservationOrder.numOfCars)
            reservationOrder.bookingPrice = self._BOOKING_PRICE_MAP.get(
                reservationOrder.bookingOption) * reservationOrder.numOfCars
            return reservationOrder
        return None

    def _applyWeeklyBookingRate(self, reservationOrder: CarReservationOrder) -> CarReservationOrder:
        if self.carInventory.canFufillOrder(reservationOrder.numOfCars):
            self.carInventory.removeFromInventory(reservationOrder.numOfCars)
            reservationOrder.bookingPrice = self._BOOKING_PRICE_MAP[
                reservationOrder.bookingOption] * reservationOrder.numOfCars
            return reservationOrder
        return None

    def _getTotalCost(self, reservationOrder: CarReservationOrder):
        if reservationOrder.id not in self._carReservationRecord:
            return None

        returnTime = datetime.datetime.now()
        duration = returnTime - reservationOrder.bookingTime

        if reservationOrder.bookingOption == "hourly":
            totalCost = round(duration.seconds/3600) * \
                reservationOrder.bookingPrice
        elif reservationOrder.bookingOption == "daily":
            totalCost = round(duration.seconds/86400) * \
                reservationOrder.bookingPrice
            print("Daily Cost", totalCost)
        elif reservationOrder.bookingOption == "weekly":
            totalCost = round(duration.days/7) * reservationOrder.bookingPrice
            print("Total cost", totalCost, reservationOrder.bookingPrice)
        return totalCost, returnTime

    def returnRentalCar(self, reservationOrder):
        if reservationOrder.id not in self._carReservationRecord:
            return None

        totalCost, returnTime = self._getTotalCost(reservationOrder)

        finalBill = RentalBill()
        finalBill.totalCost = totalCost
        finalBill.returnTime = returnTime
        finalBill.customerName = reservationOrder.customerName
        finalBill.customerEmailAddress = reservationOrder.customerEmailAddress
        finalBill.numOfCars = reservationOrder.numOfCars
        finalBill.bookingOption = reservationOrder.bookingOption
        finalBill.bookingTime = reservationOrder.bookingTime
        finalBill.bookingPrice = reservationOrder.bookingPrice
        return finalBill


def createShop():
    inventory = CarInventory(10)
    rentalShop = RentalOffice(inventory)
    return rentalShop


office = createShop()


reservationRequest = CarReservationRequest()
reservationRequest.customerName = "Tobe"
reservationRequest.numOfCars = 5
reservationRequest.bookingOption = "daily"
reservationRequest.customerEmailAddress = "mmm@gmail.com"
result = office.rentCar(reservationRequest)


reservationOrder = CarReservationOrder()
reservationOrder.customerName = "Tobe"
reservationOrder.customerEmailAddress = "mmm@gmail.com"
reservationOrder.bookingOption = "daily"
reservationOrder.numOfCars = 5
reservationOrder.bookingTime = datetime.datetime.utcnow()
# result = office._applyHourlyBookingRate(reservationOrder)
cost = office.returnRentalCar(reservationOrder)


print(result.customerName)
print(result.bookingOption)
print(result.customerEmailAddress)
print("Reservation ID", result.id)
print(office._carReservationRecord)


print("Customer Name", cost.customerName)
print("Booking Options", cost.bookingOption)
print("Rental Time", cost.bookingTime)
print("Num of cars booked", cost.numOfCars)
print("Price$", cost.bookingPrice)
print("Email-Address", cost.customerEmailAddress)
# print(office._carReservationRecord)
