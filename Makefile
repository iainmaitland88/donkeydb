.PHONY: install test

requirements.txt:
	pip-compile requirements.in

install: requirements.txt
	pip install -r requirements.txt

test:
	pytest tests

format:
	black src tests
