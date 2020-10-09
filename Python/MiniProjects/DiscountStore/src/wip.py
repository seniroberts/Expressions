
class Inventory:

    _goods = {"Iphone XR": 20, "MacBook Air": 15,
              "HeadPhones": 25, "Monitor": 35}

    def __init__(self, _goods):
        self._goods = _goods

    def countTotalInventory(self) -> int:
        return sum(self._goods.values())

    def countInventoryByItem(self, item: str) -> int:
        return self._goods.get(item)

    def reduceInventory(self, item: str, quantity: int) -> dict:
        self._goods[item] -= quantity
        return self._goods

    def increaseInventory(self, item: str, quantity: int) -> dict:
        self._goods[item] += quantity
        return self._goods

    def isInventorySufficient(self, item: str, quantity: int):
        if self._goods.get(item) >= quantity:
            return True
        else:
            return False

    def updateInventory(self, newItem: dict) -> dict:
        self._goods.update(newItem)
        return self._goods

    def getItem(self, item: str) -> int:
        return self._goods.get(item)


class PriceList:

    _priceMap = {"Iphone XR": 900, "MacBook Air": 2500,
                 "HeadPhones": 370, "Monitor": 145}

    def __init__(self, _priceMap):
        self._priceMap = _priceMap

    def getPrice(self, item):
        return self._priceMap[item]

    def updatePrice(self, item, value):
        self._priceMap[item] = value
        return self._priceMap

    # def updateItem(self, newItem: dict) -> dict:
    #     self._priceMap.update(newItem)
    #     return self._priceMap

    def updateItem(self, item, value):
        newItem = {item: value}
        self._priceMap = self._priceMap
        self._priceMap = {** newItem, ** self._priceMap}
        return self._priceMap


class Customer:
    _id = 0

    __slots__ = ["customerName", "customerEmail", "id"]

    def __init__(self, customerName: str):
        self.customerName = customerName
        self.customerEmail = ""
        self.id = Customer._id
        Customer._id += 1


class PurchaseIntent:
    _id = 0

    __slots__ = ["id", "customerId", "customerName",
                 "customerEmail", "item", "quantity"]

    def __init__(self):
        self.id = None
        self.customerId = None
        self.customerName = None
        self.customerEmail = None
        self.item = ""
        self.quantity = 0

    @staticmethod
    def create():
        intent = PurchaseIntent()
        intent.id = PurchaseIntent._id
        PurchaseIntent._id += 1
        return intent


class PurchaseOrder:
    _id = 0

    __slots__ = ["id", "customerId", "customerName",
                 "customerEmail, ""item", "quantity", "totalPrice", "tax"]

    def __init__(self):

        self.id = None
        self.customerId = None
        self.customerName = None
        self.customerEmail = None
        self.item = ""
        self.quantity = 0
        self.totalPrice = 0.0
        self.tax = 0.0

    @staticmethod
    def create():
        order = PurchaseOrder()
        order.id = PurchaseOrder._id
        PurchaseOrder._id += 1
        return order


class CustomerBill:

    __slots__ = ["customerId", "customerName",
                 "customerEmail", "item", "quantity", "totalCost", "tax"]

    def __init__(self):
        self.customerId = None
        self.customerName = None
        self.customerEmail = None
        self.item = ""
        self.quantity = 0
        self.totalCost = 0.0
        self.tax = tax


class ShoppingMall:

    def __init__(self, storeInventroy: Inventory, prices: PriceList):
        self.storeInventory = storeInventory
        self.prices = prices
        self.totalPrice = 0
        self.itemsInCart = {}

    def startShopping(self, intent: PurchaseIntent) -> PurchaseOrder:
        shoppingActivity = PurchaseOrder.create()
        shoppingActivity.customerId = PurchaseOrder.customerId
        shoppingActivity.customerName = PurchaseOrder.customerName
        shoppingActivity.customerEmail = PurchaseOrder.customerEmail
        shoppingActivity.item = PurchaseOrder.item
        shoppingActivity.quantity = PurchaseOrder.quantity

        shoppingActivity = self._addItemsToCart(shoppingActivity)

    def _updateCart(self, value: dict) -> dict:
        self.itemsInCart.update(value)
        return self.itemsInCart

    def _addItemsToCart(self, item: str, quantity: int) -> dict:
        if self.storeInventory.getItem(item) and self.storeInventory.isInventorySufficient(item, quantity):
            itemPrice = self.prices.getPrice(item)
            self.totalPrice += itemPrice * quantity
            cartItems = {item: quantity}
            self.updateCart(cartItems)
            self.storeInventory.reduceInventory(item, quantity)
            return self.itemsInCart

        return None

    def _removeItemsFromCart(self, item, quantity):
        if item in self.itemsInCart:
            if quantity < self.itemsInCart[item] and quantity > 0:
                price = self.prices.getPrice(item)
                self.itemsInCart[item] -= quantity
                self.totalPrice -= quantity * price
                self.storeInventory.increaseInventory(item, quantity)
            elif quantity == self.itemsInCart[item]:
                price = self.prices.getPrice(item)
                self.totalPrice -= price * self.itemsInCart[item]
                self.itemsInCart.pop(item)
                self.storeInventory.increaseInventory(item, quantity)

        return self.itemsInCart
