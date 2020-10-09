from src.backend import TheStore, Customer, CustomerBill, PurchaseIntent, PurchaseOrder, Inventory, PriceList


def testShoppingTransaction():
    def createStore():
        stock = Inventory({"Iphone XR": 20, "MacBook Air": 15,
                           "HeadPhones": 25, "Monitor": 35})

        prices = PriceList({"Iphone XR": 900, "MacBook Air": 2500,
                            "HeadPhones": 370, "Monitor": 145})

        store = TheStore(stock, prices)
        return store

    BestBuy = createStore()

    shoppingItems = CustomerBill()
    shoppingItems.customerName = "Tolani"
    shoppingItems.customerEmail = "Tolani@gmail.com"
    shoppingItems.item = "Iphone XR"
    shoppingItems.quantity = 5

    customer1 = BestBuy._startShopping(shoppingItems)
    customer1 = BestBuy._addItemsToCart(shoppingItems)
    customer1 = BestBuy._removeItemsFromCart2("Iphone XR", 1)
    customer1 = BestBuy._getCostOfCartItems(shoppingItems)
    customer1 = BestBuy._checkOut(shoppingItems)
    # customer1 = BestBuy._showCart()

    print()
    print("-- Testing CustomerName. Expected:: Tolani, Outcome:: ",
          customer1.customerName)
    print("-- Testing CustomerName. Expected:: Tolani@gmail.com, Outcome:: ",
          customer1.customerEmail)
    print("-- Testing Item. Expected:: IphoneXR, Outcome:: ",
          customer1.item)
    print("-- Testing Quantity Expected:: 5, Outcome:: ",
          customer1.quantity)
    print("-- Testing Cost. Expected:: 3600, Outcome:: ", customer1.price)
    print("-- Testing TotalCost. Expected:: 4140, Outcome:: ", customer1.totalCost)
    print("-- Testing Tax Applied. Expected:: 0.15, Outcome:: ", customer1.tax)

    print("----------------------------------------------------------------------------------")
    print()


testShoppingTransaction()
