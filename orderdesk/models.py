from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Product:
    sku: str
    price_cents: int
    weight_grams: int = 0

@dataclass(frozen=True)
class Line:
    sku: str
    quantity: int

@dataclass
class Order:
    id: str
    lines: List[Line]
    quote: dict
    created_at: str
    status: str = "placed"
