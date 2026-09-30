PYTHON ?= python3
.PHONY: setup test demo
setup:
	@$(PYTHON) -c "import sys; assert sys.version_info >= (3, 9)"
test:
	@$(PYTHON) -m unittest discover -s tests -t . -v
demo:
	@$(PYTHON) -m orderdesk --demo
