def fingerprint(lines, discount_bps):
    totals = {}
    for line in lines:
        totals[line.sku] = totals.get(line.sku, 0) + line.quantity
    return (tuple(sorted(totals.items())), discount_bps)

def order_id(sequence):
    return "ord-" + str(sequence).zfill(6)
