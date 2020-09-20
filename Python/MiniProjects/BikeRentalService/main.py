from bike_rental import BikeInventory, Customer, BikeRentalOrderRequest, BikeRentalOrder, RentalBill, RentalShop
import datetime


def createShop() -> RentalShop:
    inventory = BikeInventory(10)
    shop = RentalShop(inventory)
    return shop


def printReturnOrderFailed(orderId):
    print(f"No Order exists with the id: {orderId}")


def printReturnBill(bill: RentalBill, orderId):
    print("Return was Successful. You bill is Below")
    print("Bike Rental Bill: ")
    print(f"-- Total Cost: ${bill.totalCost}")
    print(f"-- Order Id: {orderId}")
    print(f"-- Name: {bill.customerName}")
    print(f"-- Number of bikes: {bill.numberOfBikes}")
    print(f"-- price per day: ${bill.pricePerDay}")
    print(f"-- rental time: {bill.rentalTime}")
    print(f"-- return Time: {bill.returnTime}")


def handleReturnOption(shop: RentalShop):
    orderId = int(input("Enter Your Rental order id:: "))
    # get the order and ask user to verify transaction
    rentalOrder = shop.getRentalOrderById(orderId)
    if (rentalOrder is None):
        printReturnOrderFailed(orderId)
    else:
        print("Here is Your Rental Order detail")
        print(f"-- Order Id: {rentalOrder.id}")
        print(f"-- Name: {rentalOrder.customerName}")
        print(f"-- Number of bikes: {rentalOrder.numberOfBikes}")
        print(f"-- price per day: ${rentalOrder.pricePerDay}")
        print(f"-- rental time: {rentalOrder.rentalTime}")
        decision = str(input("Confirm Order Return (yes/no): "))
        if (decision == "yes"):
            bill = shop.returnRental(rentalOrder)
            printReturnBill(bill, orderId)


def printSuccessfulRentOrder(order: BikeRentalOrder):
    print()
    print("Your Order was successful")
    print("Your Order Details are as follows")
    print(f"-- Order Id: {order.id}")
    print(f"-- Name: {order.customerName}")
    print(f"-- Number of bikes: {order.numberOfBikes}")
    print(f"-- price per day: ${order.pricePerDay}")
    print(f"-- rental time: {order.rentalTime}")


def printFailedRentOrder(order: BikeRentalOrderRequest):
    print()
    print("The below Order Could not be placed. Kindly try again at a alater time ")
    print(f"-- Name: {order.customerName}")
    print(f"-- Number of bikes: {order.numberOfBikes}")


def handleRentOption(shop: RentalShop):
    rentalOption = str(
        input("Enter Rental Option: (hourly, daily, weekly) :: "))
    numOfBikes = int(input("Enter number of bikes :: "))
    name = str(input("Enter your name :: "))
    # perform the request
    customer = Customer(name)
    # create the order
    orderRequest = BikeRentalOrderRequest()
    orderRequest.customerId = customer.id
    orderRequest.customerName = customer.name
    orderRequest.rentalOption = rentalOption
    orderRequest.numberOfBikes = numOfBikes
    # attempt to place the order
    placedOrder = shop.rentBike(orderRequest)
    if (placedOrder is None):
        printFailedRentOrder(orderRequest)
    else:
        printSuccessfulRentOrder(placedOrder)


def startShoppingTransactions(shop: RentalShop):
    while True:
        print("\n\n")
        request = input("What do you want to do (return / rent) or quit:: ")
        if (request == "return"):
            handleReturnOption(shop)
        elif (request == "rent"):
            handleRentOption(shop)
        elif (request == "quit"):
            break


def main():
    shop = createShop()
    startShoppingTransactions(shop)


main()
