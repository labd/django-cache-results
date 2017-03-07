.PHONY: install test upload docs


install:
	pip install -e .[docs,test]

test:
	py.test

retest:
	py.test -vvv --lf

coverage:
	py.test --cov=django_cache_results --cov-report=term-missing --cov-report=html

clean:
	rm -rf .tox
	find . -name '*.egg-info' -delete
	find . -name '__pycache__' -delete
	find . -name '*.pyc' -delete

docs:
	$(MAKE) -C docs html

release:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*
