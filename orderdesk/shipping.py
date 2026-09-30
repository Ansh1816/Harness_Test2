FREE_SHIPPING_CENTS = 5000
STANDARD_SHIPPING_CENTS = 500

def shipping_amount(discounted_subtotal):
    return 0 if discounted_subtotal > FREE_SHIPPING_CENTS else STANDARD_SHIPPING_CENTS
