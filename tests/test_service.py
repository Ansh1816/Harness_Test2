import unittest
from orderdesk.models import Line
from tests.helpers import service

class ServiceTests(unittest.TestCase):
    def test_retry_does_not_reserve_twice(self):
        app = service()
        first = app.place([Line("a", 2)], "same")
        again = app.place([Line("a", 2)], "same")
        self.assertEqual(first.id, again.id)
        self.assertEqual(app.inventory.snapshot()["a"], 18)
        self.assertEqual(len(app.events.snapshot()), 1)
    def test_cancel_twice_returns_stock_once(self):
        app = service()
        order = app.place([Line("a", 2)], "one")
        app.cancel(order.id)
        app.cancel(order.id)
        self.assertEqual(app.inventory.snapshot()["a"], 20)
        self.assertEqual(len(app.events.snapshot()), 2)
    def test_place_stores_order(self):
        app = service()
        order = app.place([Line("a", 2)], "one")
        self.assertEqual(app.store.get(order.id).status, "placed")
    def test_empty_order_rejected(self):
        with self.assertRaises(ValueError):
            service().place([], "empty")
    def test_boolean_quantity_rejected(self):
        with self.assertRaises(ValueError):
            service().place([Line("a", True)], "bad")
    def test_unknown_sku_rejected(self):
        with self.assertRaises(ValueError):
            service().place([Line("unknown", 1)], "bad")
    def test_empty_key_rejected(self):
        with self.assertRaises(ValueError):
            service().place([Line("a", 1)], " ")
    def test_cancel_missing_order(self):
        with self.assertRaises(KeyError):
            service().cancel("missing")
