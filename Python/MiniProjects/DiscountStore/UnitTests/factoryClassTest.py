from src.shoppingMall import TheStore, Customer, CustomerBill, PurchaseIntent, PurchaseOrder, Inventory, PriceList

"This will test the creation of an nintent to purchase as soon as a customer logs on to the store."


def PurchaseIntentTest():
    dummyInteraction = PurchaseIntent.createIntent()
    print()

    print("-- Intent ID Test. Expected = 0:: Output::", dummyInteraction.id)
    print("-- Intent Item Test. Expected : , Output:: ", dummyInteraction.item)

    dummyInteraction = PurchaseIntent.createIntent()
    print()
    print("-- Intent ID Test. Expected = 1:: Output::", dummyInteraction.id)

    print("---------------------------------------------------------------------------------------")


PurchaseIntentTest()


def PurchaseOrderTest():
    dummyRequest = PurchaseOrder.createOrder()
    print()

    print("-- Testing Order ID creation. Expected:0, Outcome:: ", dummyRequest.id)

    dummyRequest = PurchaseOrder.createOrder()
    print()

    print("-- Testing Order ID creation. Expected:1, Outcome:: ", dummyRequest.id)

    print("---------------------------------------------------------------------------------------")
    print()


PurchaseOrderTest()


def CustomerBillTest():
    dummyBill = CustomerBill()
    print()
    print("-- Testing Quantity. Expected:: 0, Outcome::  ", dummyBill.quantity)
    print("-- Testing TotalCost. Expected:: 0.0, Outcome::  ", dummyBill.totalCost)
    print("-- Testing Tax. Expected:: 0.0, Outcome::  ", dummyBill.tax)

    print("---------------------------------------------------------------------------------------")
    print()


CustomerBillTest()
