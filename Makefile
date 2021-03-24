PROJ_PTH=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
FLAKE_APP_PATH = flask/src/
FASTAPI_APP_PATH = fastapi/src/
PYTHON_EXEC?=python
COMPOSE_EXEC?=docker-compose

LINT_PATHS = \
$(FLAKE_APP_PATH) \
$(FASTAPI_APP_PATH)

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
	$(PYTHON_EXEC) -m piptools sync "${PROJ_PTH}fastapi/deployment/requirements/dev.txt" "${PROJ_PTH}flask/deployment/requirements/dev.txt" "${PROJ_PTH}fastapi/deployment/requirements/prod.txt" "${PROJ_PTH}flask/deployment/requirements/prod.txt"
	$(PYTHON_EXEC) -m pip install -e fastapi
	$(PYTHON_EXEC) -m pip install -e flask


sync-deps-prod:
	$(PYTHON_EXEC) -m piptools sync "${PROJ_PTH}fastapi/deployment/requirements/prod.txt"
	$(PYTHON_EXEC) -m piptools sync "${PROJ_PTH}flask/deployment/requirements/prod.txt"

lint:
	$(PYTHON_EXEC) -m autoflake --in-place --recursive --ignore-init-module-imports --remove-duplicate-keys --remove-unused-variables --remove-all-unused-imports $(LINT_PATHS)
	$(PYTHON_EXEC) -m black $(LINT_PATHS)
	$(PYTHON_EXEC) -m isort $(LINT_PATHS)
	$(PYTHON_EXEC) -m mypy $(FLAKE_APP_PATH) --ignore-missing-imports
	$(PYTHON_EXEC) -m mypy $(FASTAPI_APP_PATH) --ignore-missing-imports

run-fastapi:
	uvicorn fastapi_app.web_app.app:app --reload

run-flask:
	$(PYTHON_EXEC) $(FLAKE_APP_PATH)flask_app/web_app/app.py