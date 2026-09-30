from .catalog import Catalog
from .inventory import Inventory
from .models import Product
from .service import OrderService

def demo_service():
    products = [Product("notebook", 1200, 200), Product("pen", 250, 20), Product("bag", 5000, 600)]
    return OrderService(Catalog(products), Inventory({p.sku: 20 for p in products}))
