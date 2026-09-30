from .money import portion
from .validation import validate_bps

def tax_amount(taxable_cents, basis_points):
    validate_bps(basis_points)
    return portion(taxable_cents, basis_points)
