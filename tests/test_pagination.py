import unittest
from orderdesk.models import Line
from tests.helpers import service

class PaginationTests(unittest.TestCase):
    def test_equal_timestamp_orders_are_not_lost(self):
        app = service()
        expected = [app.place([Line("a", 1)], str(i)).id for i in range(3)]
        first, cursor = app.store.list_page(limit=2)
        second, end = app.store.list_page(limit=2, cursor=cursor)
        self.assertEqual([o.id for o in first + second], expected)
        self.assertIsNone(end)
    def test_empty_store(self):
        self.assertEqual(service().store.list_page(), ([], None))
    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            service().store.list_page(limit=0)
    def test_single_page(self):
        app = service()
        app.place([Line("a", 1)], "one")
        orders, cursor = app.store.list_page()
        self.assertEqual(len(orders), 1)
        self.assertIsNone(cursor)
