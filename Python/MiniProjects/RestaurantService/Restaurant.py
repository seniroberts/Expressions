

class Kitchen:
    _foodBank = {"Salad": 3, "Jollof-Rice": 4, "Steak": 5, "Combo": 6}

    def __init__(self, _foodBank):
        self._foodBank = _foodBank  # _foodBank

    def countDishes(self) -> int:
        return sum(self._foodBank.values())

    def reduceFoodQuantity(self, key, quantity) -> dict:
        self._foodBank[key] -= quantity
        return self._foodBank

    def isDishSufficient(self, key, quantity) -> bool:
        if self._foodBank.get(key) >= quantity:
            return True
        else:
            return False

    def increaseFoodQuantity(self, key, quantity) -> dict:
        self._foodBank[key] += quantity
        return self._foodBank


class Customer:
    _id = 0

    __slots__ = ["customerName", "customerEmailAddress", "id"]

    def __init__(self, customerName: str):
        self.customerName = customerName
        self.customerEmailAddress = ""
        self.id = Customer._id
        Customer._id += 1


class FoodOrderRequest:
    _id = 0

    __slots__ = ["id",
                 "customerId",
                 "customerName",
                 "customerEmailAddress",
                 "foodChoice",
                 "quantity",
                 "dinningOption"]

    def __init__(self):
        self.id = None
        self.customerId = None
        self.customerName = None
        self.customerEmailAddress = ""
        self.foodChoice = ""
        self.quantity = 0
        self.dinningOption = ""

    @staticmethod
    def create():  # Creates a FoodOrderRequest for Processing
        orderRequest = FoodOrderRequest()
        orderRequest.id = FoodOrderRequest._id
        FoodOrderRequest._id += 1
        return orderRequest


class FoodOrder:
    """ This is the promise that is generated when an order is sucessfully placed """
    _id = 0

    __slots__ = ["id",
                 "customerId",
                 "customerName",
                 "customerEmailAddress",
                 "foodChoice",
                 "quantity",
                 "dinningOption",
                 "pricePerMeal",
                 "tax"]

    def __init__(self):
        self.id = None
        self.customerId = None
        self.customerName = None
        self.customerEmailAddress = None
        self.foodChoice = ""
        self.quantity = 0
        self.dinningOption = ""
        self.pricePerMeal = 0.00
        self.tax = 0.00

    @staticmethod
    def create():
        order = FoodOrder()
        order.id = FoodOrder._id
        FoodOrder._id += 1
        return order


class CustomerBill:

    __slots__ = ["totalCost", "customerId", "customerName", "customerEmailAddress", "foodChoice", "quantity",
                 "dinningOption", "pricePerMeal", "tax"]

    def __init__(self):
        self.totalCost = 0.00
        self.customerId = None
        self.customerName = None
        self.customerEmailAddress = None
        self.foodChoice = ""
        self.quantity = 0
        self.dinningOption = ""
        self.pricePerMeal = 0.00
        self.tax = 0.00


class Outlet:
    _dinningOptions = {"Eat-In": 0, "Pick-up": 1, "Delivery": 5}
    _menuPriceMap = {"Salad": 5, "Jollof-Rice": 10, "Steak": 15, "Combo": 20}
    _tax = [0.05, 0.10]

    def __init__(self, foodKitchen: Kitchen):
        self.foodKitchen = foodKitchen
        self._allCustomerOrders = {}

    def getMenuPriceMap(self):
        return self._menuPriceMap

    def buyFood(self, orderRequest: FoodOrderRequest) -> FoodOrder:
        customerOrder = FoodOrder.create()
        customerOrder.customerId = orderRequest.customerId
        customerOrder.customerName = orderRequest.customerName
        customerOrder.customerEmailAddress = orderRequest.customerEmailAddress
        customerOrder.foodChoice = orderRequest.foodChoice
        customerOrder.quantity = orderRequest.quantity
        customerOrder.dinningOption = orderRequest.dinningOption

        customerOrder = self._applyDinningOption(customerOrder)

        if customerOrder != None:
            self._allCustomerOrders[customerOrder.id] = customerOrder
        return customerOrder

    def _applyDinningOption(self, customerOrder: FoodOrder) -> FoodOrder:
        if (customerOrder.dinningOption == "Eat-In"):
            return self._applyEatInRate(customerOrder)
        elif (customerOrder.dinningOption == "Pick-up"):
            return self._applyPickUpRate(customerOrder)
        elif (customerOrder.dinningOption == "Delivery"):
            return self._applyDeliveryRate(customerOrder)
        return None

    def _applyEatInRate(self, customerOrder: FoodOrder) -> FoodOrder:
        if self.foodKitchen.isDishSufficient(customerOrder.foodChoice, customerOrder.quantity):
            self.foodKitchen.reduceFoodQuantity(
                customerOrder.foodChoice, customerOrder.quantity)
            # set the price on the order
            getDinningOption = self._dinningOptions[customerOrder.dinningOption]
            customerOrder.pricePerMeal = (
                self._menuPriceMap[customerOrder.foodChoice] * customerOrder.quantity) + getDinningOption
            return customerOrder
        return None

    def _applyPickUpRate(self, customerOrder: FoodOrder) -> FoodOrder:
        if self.foodKitchen.isDishSufficient(customerOrder.foodChoice, customerOrder.quantity):
            self.foodKitchen.reduceFoodQuantity(
                customerOrder.foodChoice, customerOrder.quantity)
            # set the price on the order
            getDinningOption = self._dinningOptions[customerOrder.dinningOption]
            customerOrder.pricePerMeal = (
                self._menuPriceMap[customerOrder.foodChoice] * customerOrder.quantity) + getDinningOption
            return customerOrder
        return None

    def _applyDeliveryRate(self, customerOrder: FoodOrder) -> FoodOrder:

        if self.foodKitchen.isDishSufficient(customerOrder.foodChoice, customerOrder.quantity):
            self.foodKitchen.reduceFoodQuantity(
                customerOrder.foodChoice, customerOrder.quantity)
            # set the price on the order
            getDinningOption = self._dinningOptions[customerOrder.dinningOption]
            customerOrder.pricePerMeal = (
                self._menuPriceMap[customerOrder.foodChoice] * customerOrder.quantity) + getDinningOption
            return customerOrder
        return None

    def _getPrice(self, customerOrder: FoodOrder) -> FoodOrder:
        getDinningOption = self._dinningOptions[customerOrder.dinningOption]
        customerOrder.pricePerMeal = (
            self._menuPriceMap[customerOrder.foodChoice] * customerOrder.quantity) + getDinningOption

        return customerOrder

    def checkOut(self, customerOrder: FoodOrder) -> CustomerBill:

        invoice = CustomerBill()

        if customerOrder.pricePerMeal <= 5:
            totalCost = customerOrder.pricePerMeal * \
                self._tax[0] + customerOrder.pricePerMeal
        else:
            totalCost = customerOrder.pricePerMeal * \
                self._tax[1] + customerOrder.pricePerMeal
        totalCost = totalCost
        invoice.totalCost = totalCost
        invoice.customerId = customerOrder.customerId
        invoice.customerName = customerOrder.customerName
        invoice.customerEmailAddress = customerOrder.customerEmailAddress
        invoice.foodChoice = customerOrder.foodChoice
        invoice.quantity = customerOrder.quantity
        invoice.dinningOption = customerOrder.dinningOption
        invoice.pricePerMeal = customerOrder.pricePerMeal

        if customerOrder.pricePerMeal <= 5:
            tax = self._tax[0]
        else:
            tax = self._tax[1]
        tax_applied = tax
        invoice.tax = tax_applied
        return invoice

    def getFoodOrderById(self, customerOrderId: int) -> FoodOrder:
        return self._allCustomerOrders.get(customerOrderId, None)
