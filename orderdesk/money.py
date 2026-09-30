def portion(cents, basis_points):
    """Round a nonnegative basis-point portion half-up using integer math."""
    return (cents * basis_points + 5000) // 10000
