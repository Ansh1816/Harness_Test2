from .money import portion
from .validation import validate_bps

def discount_amount(subtotal, basis_points):
    validate_bps(basis_points)
    return portion(subtotal, basis_points)
