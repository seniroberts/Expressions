from CabService import Places, RideClient, InitiateBookingRequest, RideBookingOrder, CustomerBill, Drivers, CabService
import math
""" Testing Places class """


def pointDistance(coord1, coord2):
    distance = math.sqrt(
        (coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)
    return distance


def locationTest():
    coordinates = Places({"Los-Angeles": (5.3, 2.7),
                          "San-Jose": (3.9, 5.0),
                          "San-Francisco": (7, 5),
                          "Fremont": (10, 6.9),
                          "Santa-Clara": (16.7, 6.8)
                          })

    testgetLocation = coordinates.getLocation("Fremont")
    testIsLocationPresent = coordinates.isLocationPresent("Santa-Clara")
    testGetDistance = coordinates.getDistance("Los-Angeles", "San-Francisco")
    print()

    expectedLocation = (10, 6.9)
    assert(pointDistance(testgetLocation, expectedLocation) < 1e-4)
    print("locationTest:: Get Location Passed!")

    assert(testIsLocationPresent == True)
    print("locationTest:: IsLocation Present Passed")

    assert(testGetDistance == 3)
    print("locationTest ::Test Get Distance Passed")
    # print("-- Testing getLocation Method: Expected: Map of Coordinates: Result:: ", testgetLocation)
    # print("-- Tetsing isLocationPresent Method: Expected: True, Result:: ",
    #   testIsLocationPresent)
    # print("-- Testing getDistance Method: Expected: 3, Result:: ",
    #   testGetDistance, "miles")
    print()


locationTest()


def RideClientTest():
    """ Testing the customer creation class. The customer should be assigned unique IDs """

    dummyClient = RideClient("Olumide")
    print()

    print("-- Testing Customer ID. Expected 0, Result::", dummyClient.id)
    print("-- Testing CustomerEmail. Expected < >, Result:: ",
          dummyClient.customerEmail)
    print("-- Testing customer Name. Expected: Olumide, Result:: ",
          dummyClient.customerName)

    dummyClient = RideClient("Tobe")
    print()

    print("-- Testing Customer ID. Expected 1, Result::", dummyClient.id)
    print("-- Testing CustomerEmail. Expected < >, Result:: ",
          dummyClient.customerEmail)
    print("-- Testing customer Name. Expected: Tobe, Result:: ",
          dummyClient.customerName)
    print()


# RideClientTest()


def InitiateBookingRequestTest():
    """ Tests the creation of a booking request to be submitted by the customer."""
    dummyRequest = InitiateBookingRequest.create()
    print()

    print("-- Testing Request ID. Expected: 0, Result:: ", dummyRequest.id)
    print("-- Testing pickUpLocation Attribute. Expected "", Result:: ",
          dummyRequest.pickUpLocation)
    print("-- Testing Distance Attribute. Expected: 0.00, Result:: ",
          dummyRequest.distance)

    dummyRequest = InitiateBookingRequest.create()
    print()

    print("-- Testing Request ID. Expected: 1, Result:: ", dummyRequest.id)
    print("-- Testing pickUpLocation Attribute. Expected "", Result:: ",
          dummyRequest.pickUpLocation)
    print("-- Testing Distance Attribute. Expected: 0.00, Result:: ",
          dummyRequest.distance)


# InitiateBookingRequestTest()


def RideBookingOrderTest():
    """ Testng the creation of a vaid booking order"""

    dummyOrder = RideBookingOrder.create()
    print()

    print("-- Testing Order ID. Expected: 0, Result::", dummyOrder.id)
    print("-- Testing price attribute. Expected: 0, Result::", dummyOrder.price)
    print()

    dummyOrder = RideBookingOrder.create()
    print()

    print("-- Testing Order ID. Expected: 1, Result::", dummyOrder.id)
    print("-- Testing price attribute. Expected: 0, Result::", dummyOrder.price)
    print()


# RideBookingOrderTest()


def testDrivers():
    driversMap = {
        1: {"name": "Sean", "dedicatedRoutes": ["Los-Angeles", "San-Jose"], "Status": "Available", "CarModel": "Hyundai"},
        2: {"name": "Dan", "dedicatedRoutes": ["Santa-Clara", "Fremont"], "Status": "Available", "CarModel": "Honda"},
        3: {"name": "Pat", "dedicatedRoutes": ["Santa-Clara", "San-Diego"], "Status": "Available", "CarModel": "Mazda"},
        4: {"name": "Jenny", "dedicatedRoutes": ["Cupertino", "Fremont"], "Status": "Available", "CarModel": "Mercedes"},
        5: {"name": "Aladin", "dedicatedRoutes": ["San-Diego", "San-Francisco"], "Status": "Available", "CarModel": "Volvo"},
    }
    theDrivers = Drivers(driversMap)

    testGetEligibleDrivers = theDrivers.getEligibleDrivers("San-Diego")
    testAssignDriver = theDrivers.assignDriver("San-Diego")
    testGetAvailableDrivers = theDrivers.getAvailableDrivers()

    getAssignedDriverKey = list(testAssignDriver.keys())[0]
    getAssignedDriverName = testAssignDriver[getAssignedDriverKey]["name"]
    getCarModel = testAssignDriver[getAssignedDriverKey]["CarModel"]

    print("--Testing getEligibleDrivers. Expected: Pat & Aladin. Result:: ",
          testGetEligibleDrivers)
    print()
    print("--Testing Assigning Driver. Expected: Aladin, Result:: ", testAssignDriver)
    print()
    print("--Testing getAvailable Drivers. Expected: Drivers Map excluding Aladin, Result:: ",
          testGetAvailableDrivers)
    print()
    print(
        f"-- Dear Customer, Your Ride has been booked.\n The name of your driver is {getAssignedDriverName}, you will be picked up in a {getCarModel}.\n Thanks for your patronage ")
    print()


# testDrivers()


""" Testing the billing logic. This test will depict order creation, driver assignment and billing"""


def testCabServiceTransactions():
    driversMap = {
        1: {"name": "Sean", "dedicatedRoutes": ["Los-Angeles", "San-Jose"], "Status": "Available", "CarModel": "Hyundai"},
        2: {"name": "Dan", "dedicatedRoutes": ["Santa-Clara", "Fremont"], "Status": "Available", "CarModel": "Honda"},
        3: {"name": "Pat", "dedicatedRoutes": ["Santa-Clara", "San-Diego"], "Status": "Available", "CarModel": "Mazda"},
        4: {"name": "Jenny", "dedicatedRoutes": ["Cupertino", "Fremont"], "Status": "Available", "CarModel": "Mercedes"},
        5: {"name": "Aladin", "dedicatedRoutes": ["San-Diego", "San-Francisco"], "Status": "Available", "CarModel": "Volvo"},
    }

    locationMap = {"Los-Angeles": (5.3, 2.7),
                   "San-Jose": (3.9, 5.0),
                   "San-Francisco": (7, 5),
                   "Fremont": (10, 6.9),
                   "Santa-Clara": (16.7, 6.8)
                   }

    def createCabService():
        cabbies = Drivers(driversMap)
        coordinates = Places(locationMap)
        uber = CabService(cabbies, coordinates)
        return uber

    taxify = createCabService()
    costPerMile = 2.5
    tax = [0.05, 0.10, 0.15]

    riderOrder = CustomerBill()
    riderOrder.customerName = "Desola"
    riderOrder.customerEmail = "tobe@yahoo.com"
    riderOrder.pickUpLocation = "Los-Angeles"
    riderOrder.dropOffLocation = "San-Francisco"

    test1 = taxify._pairWithADriver(riderOrder)
    test2 = taxify._computeDistance(riderOrder)
    test3 = taxify._costEstimator(riderOrder)
    test4 = taxify._endRide(riderOrder)

    test5 = test1.assignedDriver[list(test1.assignedDriver.keys())[0]]['name']
    test6 = test1.assignedDriver[list(
        test1.assignedDriver.keys())[0]]['CarModel']
    # test5 = test1.assignedDriver[test5]['name']

    print()

    print("--Testing Customer Name: Expected: Desola, Result:: ", test1.customerName)
    print("--Testing Customer Email, Expected: tobe@yahoo.com, Result:: ",
          test1.customerEmail)
    print(
        f"--Testing Distance: Expected 3 miles, Result:: {test2.distance} miles")
    print(f"--Testing price Estimator: Expected 7.5, Result:: ${test3.price}")
    print(
        f"--Testing total cost Estimator: Expected 7.875, Result:: ${test4.totalCost}")
    print(f"--Testing % Tax Estimator: Expected 0.05, Result:: {test4.tax}")
    # print(test1.pickUpLocation)
    # print(test5)
    print()

    print(f"-- Dear {test1.customerName} your trip from {test1.pickUpLocation} to {test1.dropOffLocation} has been reserved. Your assigned driver {test5} will pick you up in a {test6}")
    print()
    # print(f"-- Dear {test1.customerName} please find your trip summary below:")


testCabServiceTransactions()
