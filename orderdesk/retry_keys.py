from .errors import ConflictError

class RetryKeys:
    def __init__(self):
        self._keys = {}

    def lookup(self, key, fingerprint):
        if key not in self._keys:
            return None
        previous, order_id = self._keys[key]
        if previous != fingerprint:
            raise ConflictError("key already used for another request")
        return order_id

    def remember(self, key, fingerprint, order_id):
        self._keys[key] = (fingerprint, order_id)
