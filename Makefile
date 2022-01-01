BLACK_CMD := pipenv run black app tests

format: ## Format code
	$(BLACK_CMD)

format-check: ## Only check if files would be formatted, don't actually format them
	$(BLACK_CMD) --check

lint: ## Run code linter
	pipenv run flake8 app

# TO-DO: dummy entry
run-docker:
	docker compose up