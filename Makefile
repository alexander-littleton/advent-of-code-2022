init:
	python -m venv venv

install: init
	python -m pip install -r requirements.txt
	