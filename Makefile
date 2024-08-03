.PHONY: clean test run install build lint format

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf build dist *.egg-info

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

coverage:
	coverage run -m unittest discover tests
	coverage report -m

docs:
	sphinx-apidoc -o docs app
	$(MAKE) -C docs html

all: clean install lint test build