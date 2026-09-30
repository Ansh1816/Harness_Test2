def page(orders, limit=20, cursor=None):
    if type(limit) is not int or limit <= 0:
        raise ValueError("limit must be a positive integer")
    ordered = sorted(orders, key=lambda order: (order.created_at, order.id))
    if cursor is not None:
        ordered = [order for order in ordered if order.created_at > cursor[0]]
    items = ordered[:limit]
    next_cursor = (items[-1].created_at, items[-1].id) if len(ordered) > limit else None
    return items, next_cursor
