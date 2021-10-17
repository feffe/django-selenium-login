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
	test -d venv || virtualenv venv -p python3.8
	. $(ACTIVATE); pip install -r requirements_dev.txt -r requirements.txt

.PHONY: docker-setup
docker-setup:
	docker-compose pull
	docker-compose up -d
	./wait-for-selenium-server.sh

.PHONY: docker-teardown
docker-teardown:
	docker-compose down

.PHONY: run-tests-in-docker
run-tests-in-docker: docker-setup
	docker exec test sh -c "pytest . --driver=Remote --capability browserName chrome --host=testchrome --liveserver=0.0.0.0 --base-url=http://test"


