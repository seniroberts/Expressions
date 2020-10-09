from backend import TheStore, Customer, CustomerBill, PurchaseIntent, PurchaseOrder, Inventory, PriceList
import sys


def createShoppingMall() -> TheStore:
    stock = Inventory({"Iphone XR": 20, "MacBook Air": 15,
                       "HeadPhones": 25, "Monitor": 35})

    prices = PriceList({"Iphone XR": 900, "MacBook Air": 2500,
                        "HeadPhones": 370, "Monitor": 145})

    store = TheStore(stock, prices)
    return store


# Starts the Store Object


def startStore(store: TheStore) -> str:
    print()
    print("<*><*><*><*><*><*><*> Welcome to SuperBuy Online Market Place. <*><*><*><*><*><*><*>")
    while True:
        print()
        print("Do you want to proceed to the marketplace?")
        enterSite = input("Enter YES to proceed or EXIT to discontinue.>>> ")
        if (enterSite.lower() == "yes"):
            displayMenuOptions(store)
        elif (enterSite.lower() == "exit"):
            print()
            print("Thank you for Visiting SuperBuy. Please come again\n")
            sys.exit()
        else:
            print("Invalid Input, Please Try Again!!!!!.")
            break


# displays Menu Options:


def displayMenuOptions(store):
    print()
    print("---- Special Haloween Discounts Available. Start Shopping Today!!\n")

    print("-------------------- Products --------------------")
    print("--|    Item" + " "*10 + "   Price($)")
    print(f"--1. {listifyInventory(store)[0]}" + " " *
          11 + f"${listifyInventoryPrices(store)[0]}")
    print(f"--2. {listifyInventory(store)[1]}" + " " *
          9 + f"${listifyInventoryPrices(store)[1]}")
    print(f"--3. {listifyInventory(store)[2]}" + " " *
          10 + f"${listifyInventoryPrices(store)[2]}")
    print(f"--4. {listifyInventory(store)[3]}" + " " *
          13 + f"${listifyInventoryPrices(store)[3]}")

    try:
        toContinue = int(input("Enter 1 to continue or 2 to quit:: \n"))
        if toContinue == 1:
            handleCustomerShoppingActivity(store)
        elif toContinue == 2:
            print("Exiting Marketplace")
            confirmCustomerExit(store)
    except ValueError:
        print("Enter a valid input\n")


# Converts the food dictionary to an array of dict keys
def listifyInventory(store):
    productList = store.getPriceList()
    return list(productList)


# Converts the food dictionary to an array of dict values
def listifyInventoryPrices(store):
    shelfPrice = store.getPriceList()
    return list(shelfPrice.values())


# confirms customer wants to exit market place


def confirmCustomerExit(store):

    print()
    print("-- Do you want to return to the market place?")
    enterSite = input("Enter YES to proceed or EXIT to discontinue.>>> ")
    if (enterSite.lower() == "yes"):
        displayMenuOptions(store)
    elif (enterSite.lower() == "exit"):
        print("Thank you for Visiting SuperBuy. Please come again\n")
        sys.exit()


# Logic to handle item purchase and other transactions.


def handleCustomerShoppingActivity(store):
    print("What are you shopping for today?:: 1. IphoneXR, 2. MacBook Air, 3. HeadPhones, 4. Monitor")
    customerInput = handleItemSelection(store)
    itemSelection = customerInput[0]
    numOfItems = customerInput[1]
    name = input("Enter your name:: ")
    emailAddress = input("Enter your Email Address:: ")

    # create the customer
    customer = Customer(name)

    # create the purchase order
    purchaseRequest = PurchaseIntent()
    purchaseRequest.customerId = customer.id
    purchaseRequest.customerName = name
    purchaseRequest.customerEmail = emailAddress
    purchaseRequest.item = itemSelection
    purchaseRequest.quantity = numOfItems

    print(purchaseRequest.item)

    # attempt to purchase the items
    purchasedItems = store._startShopping(purchaseRequest)
    print(purchasedItems)

    # if purchase is not successful, show message and quit transaction.
    if purchasedItems is None:
        printFailedTranscationMessage(purchasedItems)
        return
    handleCheckOut(store, purchasedItems)


def handleItemSelection(store):
    while True:
        itemSelection = input("Enter the name of the item:: ")
        itemNames = listifyInventory(store)
        if itemSelection not in itemNames:
            print("*** Item not found, please try again!!!!\n")
        else:
            numOfItems = int(input("How many do you need?:: "))
            break
        print("-- Enter item Name to  begin purchase. ")
    return itemSelection, numOfItems

# Handles the checkout process


def handleCheckOut(store, purchasedItems):
    # if user specifies "yes", then commence checkout (generatebill and print message)
    # if order is successful, show order detail and ask to confirm
    printSuccessfulTransactionMessage(purchasedItems)
    startCheckOut = input("Confirm your purchase items: (yes / no):: ")
    if startCheckOut.lower() == "yes":
        bill = store._checkOut(purchasedItems)
        printCustomerBill(bill, purchasedItems.id)


def printSuccessfulTransactionMessage(shoppingActivity):
    print()
    print("Your transaction was successful")
    print("Your purchase details are as follows: ")
    print()
    print(f"-- Order Id: {shoppingActivity.id}")
    print(f"-- Name: {shoppingActivity.customerName}")
    print(f"-- Email: {shoppingActivity.customerEmail}")
    print(f"-- Item(s): {shoppingActivity.item}")
    print(f"-- Quantity {shoppingActivity.quantity}")
    print(f"-- Price ${shoppingActivity.price}")


def printCustomerBill(invoice: CustomerBill, customerOrderId):
    pass


# Notifies Customer of Unsuccessful Transactions
def printFailedTranscationMessage(purchasedItems):
    print()
    print("-- Transaction declined. Your order was not successful")


def main():
    store = createShoppingMall()
    startStore(store)


main()
