from Restaurant import Kitchen, FoodOrderRequest, FoodOrder, CustomerBill, Outlet, Customer

""" To test the Kitchen class. """


def Kitchentest():
    kitchen1 = Kitchen({"Salad": 3, "Jollof-Rice": 4, "Steak": 5, "Combo": 6})
    testDishCount = kitchen1.countDishes()
    testAddDishes = kitchen1.increaseFoodQuantity("Salad", 2)
    testRemoveDishes = kitchen1.reduceFoodQuantity("Salad", 5)
    testisDishSufficient = kitchen1.isDishSufficient("Steak", 3)
    print()

    print("--Testing CountDish Method: Expected: 18, Result :::", testDishCount)
    print("--Testing AddDish Method: Expected: 5, Result :::", testAddDishes)
    print("--Testing RemoveDish Method: Expected: 1, Result::: ", testRemoveDishes)
    print("--Testing isDishSufficient Method: Expected: True, Result :::",
          testisDishSufficient)

# Kitchentest()


""" depicts placing an order request"""


def FoodOrderRequestTest():
    dummyRequest = FoodOrderRequest.create()
    print()

    print("--Request-ID test. |Expected = 0, Output :::", dummyRequest.id)
    print("--FoodQuantity.| Expected = 0, Output :::", dummyRequest.quantity)

    dummyRequest = FoodOrderRequest.create()
    print()
    print("--Request-ID test. |Expected = 1, Output :::", dummyRequest.id)
    print("--FoodQuantity.|Expected = 0, Output :::", dummyRequest.quantity)

# FoodOrderRequestTest()


""" Tests the oucome of a processed food order request """


def FoodOrderTest():
    dummyorder = FoodOrder.create()
    print()
    print("--Order-ID Test | Expected: 0| Output :::", dummyorder.id)
    print("--Order Price Test | Expected: 0.00| Output :::", dummyorder.price)

    dummyorder = FoodOrder.create()
    print()
    print("--Order-ID Test | Expected: 1| Output :::", dummyorder.id)
    print("--Order Price Test | Expected: 0.00| Output :::", dummyorder.price)

# FoodOrderTest()


def CustomerBillTest():
    dummyBill = CustomerBill()
    print("--Testing Total Cost| Expected: 0.00| Output::: ", dummyBill.totalCost)
    print("--Testing Bill Quantity| Expected: 0| Output::: ", dummyBill.quantity)


# CustomerBillTest()

def testOutletTransactions():
    def createRestaurant():
        kitchen1 = Kitchen(
            {"Salad": 3, "Jollof-Rice": 4, "Steak": 5, "Combo": 6})
        foodPlace = Outlet(kitchen1)
        return foodPlace

    KFC = createRestaurant()

    foodRequest = CustomerBill()
    foodRequest.customerName = "Tobeey"
    foodRequest.customerEmailAddress = "tobey@yahoomail.co.uk"
    foodRequest.quantity = 2
    foodRequest.dinningOption = "Delivery"
    foodRequest.foodChoice = "Salad"

    # result = KFC._getPrice(foodRequest)
    # result = KFC.checkOut(foodRequest)

    result = KFC.buyFood(foodRequest)
    # result = KFC._applyDeliveryRate(foodRequest)
    print()
    print("Testing CustomerName|Expected-> olu| ::", result.customerName)
    print("Testing CustomerName|Expected-> tobey@yahoomail.co.uk| ::",
          result.customerEmailAddress)
    print("Testing Order Dict| Expected-> Order dict Object Address| ::",
          KFC._allCustomerOrders)  # Returns a map of customer orders"""
    print("Testing dinning Option|Expected-> Delivery| ::", result.dinningOption)
    print("Testing food choice|Expected-> Salad| ::", result.foodChoice)
    print("Testing Food Quantity|Expected-> 3| ::", result.quantity)
    print("Testing Food Price|Expected-> 20| ::", result.pricePerMeal)
    print("Testing Tax Applied |Expected-> 0.10| ::", result.tax)
    print("Testing Total_Cost |Expected-> 22.0| ::", result.totalCost)


# testOutletTransactions()
