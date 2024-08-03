.PHONY: clean test run

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

test:
	python -m unittest discover tests

run:
	python main.py

install:
	pip install -r requirements.txt

build:
	python setup.py sdist bdist_wheel

lint:
	pylint app tests

format:
	black app tests