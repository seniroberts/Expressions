from src.shoppingMall import PriceList
import unittest


class TestPriceList(unittest.TestCase):

    priceMap = {"Iphone XR": 900, "MacBook Air": 2500,
                "HeadPhones": 370, "Monitor": 145}

    PriceList(priceMap)

    def test_getPrice(self):
        self.assertEqual(PriceList.getPrice(
            self, "Iphone XR"), 900, "Price should be 900")

    def test_updatePrice(self):
        self.assertEqual(PriceList.updatePrice(
            self, "HeadPhones", 400), {"Iphone XR": 900, "MacBook Air": 2500,
                                       "HeadPhones": 400, "Monitor": 145, })

    def test_addNewItem(self):
        self.assertEqual(PriceList.addNewItem(self, "Iwatch", 299.99), {
                         "Iphone XR": 900, "MacBook Air": 2500, "HeadPhones": 370, "Monitor": 145, "Iwatch": 299.99}, "Iwatch Added to the priceList")


if __name__ == "__main__":
    unittest.main()
