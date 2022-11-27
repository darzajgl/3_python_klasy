import unittest
from task7 import StockItem, StockSorter, StockQuantitySorter


class TestStockSorters(unittest.TestCase):
    def test_default_case(self):
        self.assertIsInstance(StockQuantitySorter, type)
        self.assertTrue(issubclass(StockQuantitySorter, StockSorter))

    def test_stock_sorter(self):
        item_a = StockItem("a", 100)
        item_b = StockItem("b", 50)
        item_c = StockItem("c", 110)

        stock = [item_c, item_a, item_b]
        sorted_stock = [item_a, item_b, item_c]

        stock_sorter = StockSorter()

        self.assertEqual(sorted_stock, stock_sorter.sort(stock))

        quantity_sorted_stock = [item_b, item_a, item_c]
        stock_quantity_sorter = StockQuantitySorter()

        self.assertEqual(quantity_sorted_stock, stock_quantity_sorter.sort(stock))
