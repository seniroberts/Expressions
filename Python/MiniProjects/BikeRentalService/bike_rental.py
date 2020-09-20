import datetime


class BikeInventory:
    def __init__(self, numOfBikesInInventory):
        self._numOfBikesInInventory = numOfBikesInInventory

    def count(self) -> int:
        return self._numOfBikesInInventory

    def canSatisfy(self, num) -> bool:
        return self._numOfBikesInInventory >= num

    def decrement(self, num):
        self._numOfBikesInInventory -= num

    def increment(self, num):
        self._numOfBikesInInventory += num


class Customer:
    _idCounts = 0

    def __init__(self, name: str):
        # customer id
        self.id = Customer._idCounts
        Customer._idCounts += 1
        # Money
        self.money = 10000000
        # name
        self.name = name


class BikeRentalOrderRequest:
    """ Represents an order request made by a customer """
    _orderIds = 0

    def __init__(self):
        self.id = BikeRentalOrderRequest.createId()
        self.customerId = None
        self.customerName = None
        self.numberOfBikes = 0
        self.rentalOption = ""

    @staticmethod
    def createId() -> int:
        newId = BikeRentalOrderRequest._orderIds
        BikeRentalOrderRequest._orderIds += 1
        return newId


class BikeRentalOrder:
    """ Represents an order that was successfully placed.  """
    _orderIds = 0

    def __init__(self):
        # customer id associated with order.
        self.id = None
        self.customerId = None
        self.customerName = None
        self.numberOfBikes = 0
        self.rentalOption = ""
        self.rentalTime = None
        self.pricePerDay = 0.0

    @staticmethod
    def create():  # -> BikeRentalOrder:
        order = BikeRentalOrder()
        order.id = BikeRentalOrder._orderIds
        BikeRentalOrder._orderIds += 1
        return order


class RentalBill:
    """ Rental Bill associated with a successfully placed order """

    def __init__(self):
        self.totalCost = 0.0
        self.customerName = None
        self.numberOfBikes = 0
        self.rentalOption = ""
        self.rentalTime = None
        self.returnTime = None
        self.pricePerDay = 0.0


class RentalShop:
    _PRICE_MAP = {"hourly": 5,
                  "daily": 15,
                  "weekly": 60}

    def __init__(self, inventory: BikeInventory):
        self.inventory = inventory
        self._rentalOrdersPlaced = {}  # key(orderId) -> BikeRentalOrder

    # ################

    def rentBike(self, orderRequest: BikeRentalOrderRequest) -> BikeRentalOrder:
        """ returns an instance of BikeRentalOrder if order was successfully placed, None otherwise """

        # create an order
        placedOrder = BikeRentalOrder.create()
        placedOrder.customerName = orderRequest.customerName
        placedOrder.customerId = orderRequest.customerId
        placedOrder.numberOfBikes = orderRequest.numberOfBikes
        placedOrder.rentalOption = orderRequest.rentalOption
        placedOrder.rentalTime = datetime.datetime.now()

        placedOrder = self._applyRentalOption(placedOrder)
        if (placedOrder != None):
            self._rentalOrdersPlaced[placedOrder.id] = placedOrder
        return placedOrder

    def getRentalOrderById(self, orderId: int) -> BikeRentalOrder:
        return self._rentalOrdersPlaced.get(orderId, None)

    def returnRental(self, order: BikeRentalOrder) -> RentalBill:
        if (order.id not in self._rentalOrdersPlaced):
            return None
        #
        returnTime = datetime.datetime.now()
        duration = returnTime - order.rentalTime
        print("Duration", duration)
        totalCost = duration.days * order.pricePerDay
        print("Total cost claciulated is ", totalCost)
        # create bill
        bill = RentalBill()
        bill.totalCost = totalCost
        bill.returnTime = returnTime
        bill.customerName = order.customerName
        bill.numberOfBikes = order.numberOfBikes
        bill.rentalOption = order.rentalOption
        bill.rentalTime = order.rentalTime
        bill.pricePerDay = order.pricePerDay
        return bill

    # ########################
    def _applyRentalOption(self, placedOrder: BikeRentalOrder) -> BikeRentalOrder:
        if (placedOrder.rentalOption == "hourly"):
            return self._applyHourlyRental(placedOrder)
        elif (placedOrder.rentalOption == "daily"):
            return self._applyDailyRental(placedOrder)
        elif (placedOrder.rentalOption == "weekly"):
            return self._applyWeeklyRental(placedOrder)
        return None

    def _applyHourlyRental(self, order: BikeRentalOrder) -> BikeRentalOrder:
        if self.inventory.canSatisfy(order.numberOfBikes):
            self.inventory.decrement(order.numberOfBikes)
            # set the price on the order
            order.pricePerDay = self._PRICE_MAP[order.rentalOption] * \
                order.numberOfBikes
            return order
        return None

    def _applyDailyRental(self, order: BikeRentalOrder) -> BikeRentalOrder:
        if self.inventory.canSatisfy(order.numberOfBikes):
            self.inventory.decrement(order.numberOfBikes)
            # set the price on the order
            order.pricePerDay = self._PRICE_MAP[order.rentalOption] * \
                order.numberOfBikes
            return order
        return None

    def _applyWeeklyRental(self, order: BikeRentalOrder) -> BikeRentalOrder:
        if self.inventory.canSatisfy(order.numberOfBikes):
            self.inventory.decrement(order.numberOfBikes)
            # set the price on the order
            order.pricePerDay = self._PRICE_MAP[order.rentalOption] * \
                order.numberOfBikes
            return order
        return None
