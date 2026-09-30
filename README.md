# OrderDesk

An in-memory order-processing service with a JSON CLI. It handles catalog
prices, discounts, tax, shipping, stock reservations, cancellation, retry
keys, and cursor pagination. Python 3.9+; standard library only.

```sh
make setup
make demo
make test
python3 -m orderdesk examples/order.json
```

Entry points: `orderdesk.cli.main`, `orderdesk.service.OrderService`.
Flow: request → validation → pricing → inventory → order store → receipt.
State is per service instance, in memory; a new CLI invocation starts fresh.
See [docs/behavior.md](docs/behavior.md) for the required behavior and public APIs.

This debugging exercise includes initially failing tests. Fix the application
according to the contract and preserve the regression suite.
