from Restaurant import Customer, Kitchen, FoodOrderRequest, FoodOrder, CustomerBill, Outlet
import sys


def createRestaurant() -> Outlet:
    foodkitchen = Kitchen(
        {"Salad": 3, "Jollof-Rice": 4, "Steak": 5, "Combo": 6})
    diner = Outlet(foodkitchen)

    return diner


# Notifies customers of unsuccessful orders
def printFailedOrderMessage(processedOrder):
    print()
    print("--- Your order was not successful")


# Notifies customers of successful orders
def printSuccessfulOrderMessage(customerOrder):
    print()
    print("Your Order was successful")
    print("Your order details are as follows")
    print()
    print(f"-- Order Id: {customerOrder.id}")
    print(f"-- Name: {customerOrder.customerName}")
    print(f"-- Email: {customerOrder.customerEmailAddress}")
    print(f"-- Quantity: {customerOrder.quantity}")
    print(f"-- Price: ${customerOrder.pricePerMeal}")
    print(f"-- Dinning Option: {customerOrder.dinningOption}")


# Prints the customers final bill
def printCustomerBill(invoice: CustomerBill, customerOrderId):
    print()
    print(f"-- Dear {invoice.customerName}, your final bill is itemised below. A copy will be sent to your email address: {invoice.customerEmailAddress}\n")
    print(" "*10 + "--ORDER DETAILS--")
    print("-- ORDER-ID:" + " "*20 + f"{customerOrderId}")
    print("-- ITEM:" + " "*20 + f"{invoice.foodChoice}")
    print("-- QUANTITY:" + " "*20 + f"{invoice.quantity}")
    print("-- DINNING OPTION:" + " "*7 + f"{invoice.dinningOption}")
    print("-- PRICE(total):" + " "*14 + f"${invoice.pricePerMeal}")
    print("-- TAX(%):" + " "*20 + f"{invoice.tax}")
    print("-"*40)
    print(f"         TOTAL COST: ${invoice.totalCost}")
    print("-"*40)


def handleCustomerOrderCheckout(diner: Outlet, processedOrder):
    # if user specifies "yes", then commence checkout (generatebill and print message)
    # if order is successful, show order detail and ask to confirm
    printSuccessfulOrderMessage(processedOrder)
    startCheckout = input("Confirm Order: (yes / no):: ")
    if (startCheckout == "yes"):
        bill = diner.checkOut(processedOrder)
        printCustomerBill(bill, processedOrder.id)


# Main logic that manages routing the customer experience
def handleCustomerOrder(diner):
    print("What do you want to eat today?:: 1.-Salad, 2.-Jollof-Rice, 3.-Steak, 4.-Combo\n")
    foodSelection = input("Enter your choice of food:: \n")
    foodQuantity = int(input("Enter Quantity:: \n"))
    print("Enter your dinning option :|Eat-In, Pick-up or Delivery|")
    dineOption = input(":: ")
    name = input("Enter your name::: \n")
    emailAddress = input("Enter your Email Address:: \n")

    customer = Customer(name)  # Create the Customer

    # create the order
    orderRequest = FoodOrderRequest()
    orderRequest.customerId = customer.id
    orderRequest.customerName = name
    orderRequest.customerEmailAddress = emailAddress
    orderRequest.foodChoice = foodSelection
    orderRequest.quantity = foodQuantity
    orderRequest.dinningOption = dineOption

    # Attempt to place the Order
    processedOrder = diner.buyFood(orderRequest)

    # if order is not successful, show message and quit transaction
    if processedOrder is None:
        printFailedOrderMessage(processedOrder)
        return
    handleCustomerOrderCheckout(diner, processedOrder)


# Converts the food dictionary  to an array of dict keys
def listifyFoodNames(diner) -> list:
    nameList = diner.getMenuPriceMap()
    return list(nameList)


# Converts the food dictionary  to an array of dict values
def listifyFoodPrices(diner) -> list:
    foodPriceList = diner.getMenuPriceMap()
    return list(foodPriceList.values())


# Prints the available Menu options and the corresponding prices
def displayMenuOptions(diner) -> str:
    print("--- Welcome to Midas Diner.\n")

    print("---------- Our Menu ----------------")
    print("--|  Item" + " "*10 + "Price($)")
    print(f"--1. {listifyFoodNames(diner)[0]}" +
          " "*11 + f"${listifyFoodPrices(diner)[0]}")
    print(f"--2. {listifyFoodNames(diner)[1]}" +
          " "*5 + f"${listifyFoodPrices(diner)[1]}")
    print(f"--3. {listifyFoodNames(diner)[2]}" +
          " "*11 + f"${listifyFoodPrices(diner)[2]}")
    print(f"--4. {listifyFoodNames(diner)[3]}" +
          " "*11 + f"${listifyFoodPrices(diner)[3]}")
    print()

    try:
        toContinue = int(input("Enter 1 to continue or 2 to quit:: \n"))
        if toContinue == 1:
            handleCustomerOrder(diner)
        elif toContinue == 2:
            print("Thanks for visiting")
    except ValueError:
        print("Enter a Valid Input\n")
        toContinue = int(input("Enter 1 to continue or 2 to quit:: \n"))


def startShopping(diner: Outlet) -> str:
    print("\n <><><><><><><><> WELCOME <><><><><><><><> ")
    while True:
        print("\n")
        enterSite = input(
            "Would you like to see our Menu Options? [yes / no]:: ")
        if (enterSite == "yes"):
            displayMenuOptions(diner)
        elif (enterSite == "no"):
            print("Thank you for visiting. Please come again\n")
            sys.exit()
            break


# def main():
#     diner = createRestaurant()
#     startShopping(diner)


# main()

###############################################################################################################################

""" This function simulates an already pre-filled user input for De-bugging & Testing."""


def TestSpecialBugCase(diner):
    print("What do you want to eat today?:: 1.-Salad, 2.-Jollof-Rice, 3.-Steak, 4.-Combo")
    foodSelection = "Salad"
    foodQuantity = 2
    print("Enter your dinning option :|Eat-In, Pick-up or Delivery|")
    dineOption = "Delivery"
    name = "Olu"
    emailAddress = "tobe@gmail.com"

    customer = Customer(name)  # Create the Customer

    # create the order
    orderRequest = FoodOrderRequest()
    orderRequest.customerId = customer.id
    orderRequest.customerName = name
    orderRequest.customerEmailAddress = emailAddress
    orderRequest.foodChoice = foodSelection
    orderRequest.quantity = foodQuantity
    orderRequest.dinningOption = dineOption

    # Attempt to place the Order
    processedOrder = diner.buyFood(orderRequest)

    # if order is not successful, show message and quit transaction
    if processedOrder is None:
        printFailedOrderMessage(processedOrder)
        return
    handleCustomerOrderCheckout(diner, processedOrder)


""" Un-comment the below to make use call the special debugging function"""

# diner = createRestaurant()
# TestSpecialBugCase(diner)
