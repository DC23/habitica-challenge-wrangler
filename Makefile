SHELL=/bin/sh
PACKAGE_NAME=habitica-challenge-wrangler

.SILENT:
.IGNORE:

.PHONY: help
help:
	echo
	echo 'Utility Makefile'
	echo '============================'
	echo
	echo 'Targets supported are:'
	echo
	echo '  * clean: removes the build and directories, as well as __pycache__ and *.pyc files. Note that a clean also removes the generated documentation (as this is placed into build/docs).'
	echo '  * install-deps: installs development and test dependencies into your virtual environment.'
	echo '  * develop: installs scriptabit in development mode.'
	echo '  * uninstall: removes the development package from pip.'
	echo '  * lint: runs pylint.'
	echo '  * sdist: builds a source distribution.'
	echo '  * upload: uploads a package to PiPY.'

.PHONY: clean
clean:
	echo Cleaning ...
	rm -rf build/ .tox/ ./setuptools-* .cache/
	find . -name "__pycache__" -nowarn -exec rm -rf {} \;
	find . -name "*.pyc" -nowarn -exec rm -rf {} \;
	find . -name "scriptabit.log" -nowarn -exec rm -rf {} \;
	echo ... done

.PHONY: install-deps
install-deps:
	pip install --upgrade pip setuptools
	pip install -e.[dev,test]

.PHONY: develop
develop: install-deps
	python setup.py develop

.PHONY: uninstall
uninstall:
	pip uninstall --yes $(PACKAGE_NAME)
	rm -rf *.egg-info/

.PHONY: lint
lint:
	pylint -rn ./$(PACKAGE_NAME)/

.PHONY: sdist
sdist:
	python setup.py sdist

.PHONY: upload
upload: clean
	#python setup.py bdist_egg upload
	python setup.py sdist upload
