def validate_bps(value):
    if type(value) is not int or not 0 <= value <= 10000:
        raise ValueError("basis points must be an integer in [0, 10000]")

def validate_lines(lines, catalog):
    if not lines:
        raise ValueError("order must contain lines")
    for line in lines:
        catalog.get(line.sku)
        if type(line.quantity) is not int or line.quantity <= 0:
            raise ValueError("quantity must be a positive integer")
