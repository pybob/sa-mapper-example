.PHONY: venv
venv:
	python3.9 -m venv venv && source venv/bin/activate

.PHONY: install
install:
	pip install -r requirements/dev.txt

.PHONY: lint
lint:
	flake8 cars tests

.PHONY: test
test:
	pytest

.PHONY: coverage
coverage:
	pytest --cov=cars --cov-report term-missing

.PHONY: ci
ci: lint coverage
