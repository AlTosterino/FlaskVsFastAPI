PROJ_PTH=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PYTHON_EXEC?=python
COMPOSE_EXEC?=docker-compose

compile-deps:
	$(PYTHON_EXEC) -m piptools compile --no-header  "${PROJ_PTH}fastapi/deployment/requirements/dev.in"
	$(PYTHON_EXEC) -m piptools compile --no-header  "${PROJ_PTH}fastapi/deployment/requirements/prod.in"
	$(PYTHON_EXEC) -m piptools compile --no-header  "${PROJ_PTH}flask/deployment/requirements/dev.in"
	$(PYTHON_EXEC) -m piptools compile --no-header  "${PROJ_PTH}flask/deployment/requirements/prod.in"


recompile-deps:
	$(PYTHON_EXEC) -m piptools compile --no-header --upgrade "${PROJ_PTH}fastapi/deployment/requirements/dev.in"
	$(PYTHON_EXEC) -m piptools compile --no-header --upgrade "${PROJ_PTH}fastapi/deployment/requirements/prod.in"
	$(PYTHON_EXEC) -m piptools compile --no-header --upgrade "${PROJ_PTH}flask/deployment/requirements/dev.in"
	$(PYTHON_EXEC) -m piptools compile --no-header --upgrade "${PROJ_PTH}flask/deployment/requirements/prod.in"


sync-deps:
	$(PYTHON_EXEC) -m piptools sync "${PROJ_PTH}fastapi/deployment/requirements/dev.txt"
	$(PYTHON_EXEC) -m piptools sync "${PROJ_PTH}flask/deployment/requirements/dev.txt"
	$(PYTHON_EXEC) -m pip install -e fastapi
	$(PYTHON_EXEC) -m pip install -e flask


sync-deps-prod:
	$(PYTHON_EXEC) -m piptools sync "${PROJ_PTH}fastapi/deployment/requirements/prod.txt"
	$(PYTHON_EXEC) -m piptools sync "${PROJ_PTH}flask/deployment/requirements/prod.txt"