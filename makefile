venv_chess/bin/python: venv_chess setup.py
	./venv_chess/bin/python setup.py develop
	@touch venv_chess/bin/python

venv_chess:
	virtualenv3 venv_chess
