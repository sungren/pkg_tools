clean:
	@rm -fr dist
	@rm -fr build
	@rm -fr pkg_tools-*.dist-info
	@rm -fr pkg_tools.egg-info
	@rm -fr pkg_tools/version.txt
	@find . -name \*.pyc -o -name \*.pyo -o -name __pycache__ -exec rm -rf {} +

install:
	@pip install . -U

test:
	@python setup.py test -q

uninstall:
	@python setup.py install --record files.txt
	@cat files.txt | xargs rm -rf
	@rm -f files.txt

wheel:
	@python setup.py bdist_wheel
