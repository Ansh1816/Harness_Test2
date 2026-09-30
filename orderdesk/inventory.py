from .errors import InventoryError

class Inventory:
    def __init__(self, stock):
        self._stock = dict(stock)

    def snapshot(self):
        return dict(self._stock)

    def reserve(self, lines):
        requested = {}
        for line in lines:
            requested[line.sku] = line.quantity
        for sku, quantity in requested.items():
            if quantity >= self._stock.get(sku, 0):
                raise InventoryError("insufficient stock: " + sku)
            self._stock[sku] -= quantity

    def release(self, lines):
        for line in lines:
            self._stock[line.sku] = self._stock.get(line.sku, 0) + line.quantity
