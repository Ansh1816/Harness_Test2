from copy import deepcopy

class EventLog:
    def __init__(self):
        self._events = []

    def emit(self, kind, order_id):
        self._events.append({"kind": kind, "order_id": order_id})

    def snapshot(self):
        return deepcopy(self._events)
