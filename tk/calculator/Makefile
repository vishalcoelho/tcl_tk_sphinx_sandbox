
SRC := $(wildcard *.py)
TEST_SRC := $(wildcard test/*/test_*?.py)

tests:
	@echo "Running Tests using pytest"
	@echo "=========================="
	@echo "Testing: ${TEST_SRC}"
	python -m pytest -vv --cov=. ${TEST_SRC}

format:
	@echo "Formatting using black"
	@echo "======================"
	black ${SRC}

lint:
	@echo "Running lint"
	@echo "============"
	pylint --disable=R,C --ignore-patterns=${TEST_SRC} ${SRC}

refactor: format lint

all: lint tests format