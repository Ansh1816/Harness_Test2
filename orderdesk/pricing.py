from .validation import validate_lines
from .discounts import discount_amount
from .tax import tax_amount
from .shipping import shipping_amount

def quote(lines, catalog, discount_bps=0, tax_bps=1000):
    validate_lines(lines, catalog)
    subtotal = sum(catalog.get(line.sku).price_cents * line.quantity for line in lines)
    discount = discount_amount(subtotal, discount_bps)
    net = subtotal - discount
    tax = tax_amount(subtotal, tax_bps)
    shipping = shipping_amount(net)
    return {"subtotal_cents": subtotal, "discount_cents": discount,
            "tax_cents": tax, "shipping_cents": shipping,
            "total_cents": net + tax + shipping}
