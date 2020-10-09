class Inventory:
    _goods = {"Iphone XR": 20, "MacBook Air": 15,
              "HeadPhones": 25, "Monitor": 35}

    def __init__(self, _goods):
        self._goods = _goods

    def countTotalInventory(self):
        return sum(self._goods.values())

    def countInventoryByItem(self, item: str) -> int:
        return self._goods.get(item)

    def reduceInventory(self, item: str, quantity: int) -> dict:
        self._goods[item] -= quantity
        return self._goods

    def increaseInventory(self, item: str, quantity: int) -> dict:
        self._goods[item] += quantity
        return self._goods

    def isInventorySufficient(self, item: str, quantity: int) -> bool:
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
    priceMap = {"Iphone XR": 900, "MacBook Air": 2500,
                "HeadPhones": 370, "Monitor": 145}

    def __init__(self, priceMap):
        self.priceMap = priceMap

    def getPrice(self, item: str) -> int:
        return self.priceMap.get(item)

    def updatePrice(self, item: str, newPrice: int) -> dict:
        self.priceMap[item] = newPrice
        return self.priceMap

    def addNewItem(self, item: str, itemPrice: int) -> dict:
        newItem = {item: itemPrice}
        self.priceMap = self.priceMap
        self.priceMap = {**newItem, **self.priceMap}
        return self.priceMap


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
        self.customerEmail = ""
        self.item = ""
        self.quantity = 0

    @staticmethod
    def createIntent():
        intent = PurchaseIntent()
        intent.id = PurchaseIntent._id
        PurchaseIntent._id += 1
        return intent


class PurchaseOrder:
    _id = 0

    __slots__ = ["id", "customerId", "customerName",
                 "customerEmail", "item", "quantity", "pricePerItem", "tax"]

    def __init__(self):
        self.id = None
        self.customerId = None
        self.customerName = None
        self.customerEmail = None
        self.item = ""
        self.quantity = 0
        self.pricePerItem = 0.0
        self.tax = 0.0

    @staticmethod
    def createOrder():
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
        self.tax = 0.0


class TheStore:

    def __init__(self, storeInventory: Inventory, prices: PriceList):
        self.storeInventory = storeInventory
        self.prices = prices
        self.itemsInCart = {}
        self.costOfCartItems = 0

    def showCart(self):
        return self.itemsInCart

    def updateCart(self, itemsToUpdate: dict) -> dict:
        self.itemsInCart = {item: self.itemsInCart.get(
            item, 0) + itemsToUpdate.get(item, 0) for item in set(self.itemsInCart) | set(itemsToUpdate)}
        return self.itemsInCart

    def startShopping(self, intent: PurchaseIntent) -> PurchaseOrder:
        shoppingActivity = PurchaseOrder.createOrder()
        shoppingActivity.customerId = PurchaseOrder.customerId
        shoppingActivity.customerName = PurchaseOrder.customerName
        shoppingActivity.customerEmail = PurchaseOrder.customerEmail
        shoppingActivity.item = PurchaseOrder.item
        shoppingActivity.quantity = PurchaseOrder.quantity

        shoppingActivity = self.addItemsToCart(shoppingActivity)
        if shoppingActivity != None:
            return shoppingActivity

    def addItemsToCart(self, shoppingActivity: PurchaseOrder) -> PurchaseOrder:
        if self.storeInventory.getItem(shoppingActivity.item) and self.storeInventory.isInventorySufficient(shoppingActivity.item, shoppingActivity.quantity):
            cartItems = {shoppingActivity.item: shoppingActivity.quantity}
            self.updateCart(cartItems)
            self.storeInventory.reduceInventory(
                shoppingActivity.item, shoppingActivity.quantity)
            return shoppingActivity
        return None

    def removeItemsFromCart(self, shoppingActivity: PurchaseOrder) -> PurchaseOrder:
        if shoppingActivity.item in self.itemsInCart:
            if shoppingActivity.quantity < self.itemsInCart[shoppingActivity.item] and shoppingActivity.quantity > 0:
                self.itemsInCart[shoppingActivity.item] -= shoppingActivity.quantity
            elif shoppingActivity.quantity == self.itemsInCart[shoppingActivity.item]:
                self.itemsInCart.pop(shoppingActivity.item)
            self.storeInventory.increaseInventory(
                shoppingActivity.item, shoppingActivity.quantity)
        return shoppingActivity

    def getCostOfCartItems(self, itemsInCart) -> PurchaseOrder:
        price = self.prices.priceMap
        itemsInCart = self.itemsInCart
        costGenerator = {item: self.itemsInCart.get(
            item, 0) * price.get(item, 0) for item in set(itemsInCart) & set(price)}
        costOfItemsInCart = sum(costGenerator.values())
        return self.costOfCartItems
