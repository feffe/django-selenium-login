ACTIVATE=venv/bin/activate

venv: $(ACTIVATE)
$(ACTIVATE): requirements.txt requirements_test.txt
	test -d venv || virtualenv venv
	. $(ACTIVATE); pip install -r requirements.txt -r requirements_test.txt
