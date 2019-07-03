ACTIVATE=venv/bin/activate

.PHONY: clean
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -delete

.PHONY: lint
lint:
	./venv/bin/flake8

venv: $(ACTIVATE)
$(ACTIVATE): requirements.txt requirements_dev.txt requirements_test.txt
	test -d venv || virtualenv venv
	. $(ACTIVATE); pip install -r requirements_dev.txt -r requirements.txt
