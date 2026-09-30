import argparse
import json
from pathlib import Path
from .demo import demo_service
from .models import Line
from .receipts import receipt

def main():
    parser = argparse.ArgumentParser(description="Place an in-memory order")
    parser.add_argument("file", nargs="?")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    path = Path(__file__).resolve().parent.parent / "examples/order.json" if args.demo else args.file
    if not path:
        parser.error("provide JSON or --demo")
    request = json.loads(Path(path).read_text(encoding="utf-8"))
    service = demo_service()
    order = service.place([Line(**line) for line in request["lines"]],
                          request["key"], request.get("discount_bps", 0))
    print(json.dumps(receipt(order), sort_keys=True))
