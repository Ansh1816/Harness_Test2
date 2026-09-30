import unittest
from orderdesk.models import Line
from orderdesk.pricing import quote
from tests.helpers import service

class PricingTests(unittest.TestCase):
    def test_free_shipping_at_threshold(self):
        self.assertEqual(quote([Line("c", 1)], service().catalog)["shipping_cents"], 0)
    def test_tax_after_discount(self):
        self.assertEqual(quote([Line("a", 1)], service().catalog, 2000)["tax_cents"], 80)
    def test_ordinary_total(self):
        self.assertEqual(quote([Line("a", 1)], service().catalog)["total_cents"], 1600)
    def test_shipping_above_threshold(self):
        self.assertEqual(quote([Line("c", 2)], service().catalog)["shipping_cents"], 0)
    def test_negative_discount_rejected(self):
        with self.assertRaises(ValueError):
            quote([Line("a", 1)], service().catalog, -1)
