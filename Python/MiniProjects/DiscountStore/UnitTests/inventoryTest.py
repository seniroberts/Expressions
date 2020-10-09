from src.shoppingMall import Inventory, PriceList, Customer, PurchaseIntent, PurchaseOrder, TheStore, CustomerBill


import unittest


class TestInventory(unittest.TestCase):

    _goods = {"Iphone XR": 20, "MacBook Air": 15,
              "HeadPhones": 25, "Monitor": 35}

    Inventory(_goods)

    def test_countTotalInventory(self):
        self.assertEqual(Inventory.countTotalInventory(self),
                         95, "Output should be 95")

    def test_countInventoryByItem(self):
        self.assertEqual(Inventory.countInventoryByItem(self,
                                                        "MacBook Air"), 15, "Output should be 15")

    def test_increaseInventory(self):
        self.assertEqual(Inventory.increaseInventory(self, "MacBook Air", 5), {"Iphone XR": 20, "MacBook Air": 20,
                                                                               "HeadPhones": 25, "Monitor": 35}, "MacBook should be 20")

    def test_reduceInventory(self):
        self.assertEqual(Inventory.reduceInventory(
            self, "MacBook Air", 2), {'Iphone XR': 20, 'MacBook Air': 18, 'HeadPhones': 25, 'Monitor': 35}, ":: Quantity of MacBook Air should be 18")

    def test_isInventorySufficient(self):
        self.assertEqual(Inventory.isInventorySufficient(
            self, "MacBook Air", 500), False, "Output should be False")

    def test_updateInventory(self):
        self.assertEqual(Inventory.updateInventory(self, {"Apple Watch": 30}), {"Iphone XR": 20, "MacBook Air": 18,
                                                                                "HeadPhones": 25, "Monitor": 35, "Apple Watch": 30}, "Apple watch should be added to the goods")

    def test_getItem(self):
        self.assertEqual(Inventory.getItem(self, "Monitor"), 35)


if __name__ == '__main__':
    unittest.main()
