from .clock import utc_now
from .events import EventLog
from .identity import fingerprint
from .models import Order
from .pricing import quote
from .retry_keys import RetryKeys
from .store import OrderStore

class OrderService:
    def __init__(self, catalog, inventory, tax_bps=1000, clock=None):
        self.catalog = catalog
        self.inventory = inventory
        self.tax_bps = tax_bps
        self.clock = clock or utc_now
        self.store = OrderStore()
        self.keys = RetryKeys()
        self.events = EventLog()

    def place(self, lines, key, discount_bps=0):
        lines = list(lines)
        if not isinstance(key, str) or not key.strip():
            raise ValueError("key is required")
        amounts = quote(lines, self.catalog, discount_bps, self.tax_bps)
        signature = fingerprint(lines, discount_bps)
        self.inventory.reserve(lines)
        previous = self.keys.lookup(key, signature)
        if previous is not None:
            return self.store.get(previous)
        order = Order(self.store.next_id(), lines, amounts, self.clock())
        self.store.add(order)
        self.keys.remember(key, signature, order.id)
        self.events.emit("placed", order.id)
        return order

    def cancel(self, order_id):
        order = self.store.get(order_id)
        self.inventory.release(order.lines)
        if order.status == "cancelled":
            return order
        order.status = "cancelled"
        self.events.emit("cancelled", order.id)
        return order
