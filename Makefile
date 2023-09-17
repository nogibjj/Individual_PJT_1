install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --nbval --cov=script --cov=mylib test_*.py *.ipynb

format:
	black *.py

lint:
	ruff check *.py lib/*.py
		
all: install lint format test
