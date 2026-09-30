class Catalog:
    def __init__(self, products):
        self._products = {p.sku: p for p in products}

    def get(self, sku):
        try:
            return self._products[sku]
        except KeyError:
            raise ValueError("unknown SKU: " + str(sku)) from None
