from orderdesk.catalog import Catalog
from orderdesk.inventory import Inventory
from orderdesk.models import Product
from orderdesk.service import OrderService

def service(stock=None):
    catalog = Catalog([Product("a", 1000), Product("b", 250), Product("c", 5000)])
    return OrderService(catalog, Inventory(stock if stock is not None else {"a": 20, "b": 20, "c": 20}),
                        clock=lambda: "2026-09-30T12:00:00Z")
