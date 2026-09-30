# Order processing contract

All amounts are integer cents. A Line has sku and positive integer quantity
(booleans are invalid). Products have sku, price_cents, and weight_grams.
Unknown products, empty orders, invalid quantities, and invalid discounts
raise ValueError. Discounts and tax are integer basis points in [0, 10000].
InventoryError and ConflictError subclass ValueError.

Pricing: sum price × quantity; round the total discount half-up once; subtract
it; calculate tax on that discounted subtotal, rounding half-up once. Shipping
is zero when discounted subtotal >= 5000 cents, otherwise 500 cents. Shipping
is not taxable. Total = discounted subtotal + tax + shipping.

Reservations: aggregate all lines for each SKU; allow buying exactly available
stock; reject requests exceeding available stock. Validate the complete order
before deducting any stock. A failed order leaves stock, orders, and retry keys
unchanged. release(lines) restores each purchased unit.

OrderService(catalog, inventory, tax_bps=1000, clock=None) owns an OrderStore,
RetryKeys, and EventLog. The injected clock returns a string timestamp.
place(lines, key, discount_bps=0) requires a nonempty string key. A successful
first call reserves stock, stores an Order, records the key, emits one placed
event, and returns the Order. Same key and semantically identical request
returns the existing order without changing stock or emitting another event,
even if stock is now insufficient. Reordered or split duplicate SKU lines
are equivalent. Different quantities/SKUs/discount on a used key raise
ConflictError before any mutation. Failed requests never consume a key.

cancel(order_id) marks a placed order cancelled and returns stock once.
Repeating cancellation is a no-op; it must not release stock twice or emit
another cancelled event. Existing retry keys continue to identify the same
order, including after cancellation. Unknown IDs raise KeyError.

OrderStore.list_page(limit=20, cursor=None) returns (orders, next_cursor).
Limit must be a positive integer (not bool). Ordering is ascending by
(created_at, id). A cursor is the last emitted pair; the next page contains
strictly greater pairs. Do not drop records with equal timestamps. Emit
next_cursor only if there are more records. Lists and snapshots are detached
containers; callers must not mutate stored Order objects.

API helpers: quote(lines, catalog, discount_bps=0, tax_bps=1000) → dict;
receipt(order) → JSON-compatible dict; EventLog.snapshot() → detached list.
Demo products: notebook=1200 cents/200g, pen=250 cents/20g, bag=5000 cents/600g;
each starts with 20 units. CLI accepts {key, lines:[{sku,quantity}], discount_bps?}.
