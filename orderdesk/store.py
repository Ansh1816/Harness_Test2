from .identity import order_id
from .pagination import page

class OrderStore:
    def __init__(self):
        self._orders = {}

    def next_id(self):
        return order_id(len(self._orders) + 1)

    def add(self, order):
        self._orders[order.id] = order

    def get(self, order_id):
        return self._orders[order_id]

    def list_page(self, limit=20, cursor=None):
        return page(self._orders.values(), limit, cursor)
