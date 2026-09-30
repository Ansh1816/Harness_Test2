import unittest
from orderdesk.inventory import Inventory
from orderdesk.models import Line
from orderdesk.errors import InventoryError

class InventoryTests(unittest.TestCase):
    def test_duplicate_sku_quantities_are_summed(self):
        inventory = Inventory({"a": 10})
        inventory.reserve([Line("a", 2), Line("a", 3)])
        self.assertEqual(inventory.snapshot(), {"a": 5})
    def test_exact_stock_can_be_reserved(self):
        inventory = Inventory({"a": 3})
        inventory.reserve([Line("a", 3)])
        self.assertEqual(inventory.snapshot(), {"a": 0})
    def test_failed_multi_item_reservation_is_atomic(self):
        inventory = Inventory({"a": 10, "b": 0})
        with self.assertRaises(InventoryError):
            inventory.reserve([Line("a", 1), Line("b", 1)])
        self.assertEqual(inventory.snapshot(), {"a": 10, "b": 0})
    def test_simple_reservation(self):
        inventory = Inventory({"a": 10})
        inventory.reserve([Line("a", 2)])
        self.assertEqual(inventory.snapshot(), {"a": 8})
    def test_snapshot_detached(self):
        inventory = Inventory({"a": 10})
        inventory.snapshot()["a"] = 0
        self.assertEqual(inventory.snapshot()["a"], 10)
