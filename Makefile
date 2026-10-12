# ============================================================================
# DELTA-ATRAX-V2 - Makefile
# ============================================================================

.PHONY: help install install-dev check run test clean build docker-build docker-run docker-stop docker-logs docker-clean deploy lint format security docs

# ==================== VARIABLES ====================
PYTHON := python3
PIP := pip3
VENV := venv
VENV_BIN := $(VENV)/bin
APP_NAME := delta_atrax_v2
DOCKER_IMAGE := delta-atrax-v2
DOCKER_TAG := latest
DOCKER_COMPOSE := docker-compose

# Colors
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
CYAN := \033[0;36m
NC := \033[0m

# ==================== HELP ====================
help:
	@echo "$(CYAN)🦀 DELTA-ATRAX-V2 - Makefile Commands$(NC)"
	@echo "=============================================="
	@echo ""
	@echo "$(GREEN)Installation:$(NC)"
	@echo "  make install        Install production dependencies"
	@echo "  make install-dev    Install development dependencies"
	@echo "  make venv           Create virtual environment"
	@echo "  make check          Check dependencies"
	@echo ""
	@echo "$(GREEN)Running:$(NC)"
	@echo "  make run            Run the application"
	@echo "  make run-interactive Run in interactive mode"
	@echo "  make run-web        Run with web dashboard only"
	@echo ""
	@echo "$(GREEN)Testing:$(NC)"
	@echo "  make test           Run all tests"
	@echo "  make test-cov       Run tests with coverage"
	@echo "  make lint           Run linters"
	@echo "  make format         Format code"
	@echo "  make security       Run security checks"
	@echo ""
	@echo "$(GREEN)Docker:$(NC)"
	@echo "  make docker-build   Build Docker image"
	@echo "  make docker-run     Run Docker container"
	@echo "  make docker-stop    Stop Docker containers"
	@echo "  make docker-logs    View Docker logs"
	@echo "  make docker-clean   Clean Docker resources"
	@echo "  make docker-compose-up   Start all services"
	@echo "  make docker-compose-down Stop all services"
	@echo ""
	@echo "$(GREEN)Maintenance:$(NC)"
	@echo "  make clean          Clean temporary files"
	@echo "  make clean-all      Clean everything including venv"
	@echo "  make backup         Backup configuration and data"
	@echo "  make docs           Generate documentation"
	@echo ""

# ==================== VIRTUAL ENVIRONMENT ====================
venv:
	@echo "$(CYAN)Creating virtual environment...$(NC)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✅ Virtual environment created$(NC)"

$(VENV_BIN)/activate: venv

# ==================== INSTALLATION ====================
install: venv
	@echo "$(CYAN)Installing production dependencies...$(NC)"
	$(VENV_BIN)/pip install --upgrade pip setuptools wheel
	$(VENV_BIN)/pip install -r requirements.txt
	@echo "$(GREEN)✅ Installation complete$(NC)"

install-dev: install
	@echo "$(CYAN)Installing development dependencies...$(NC)"
	$(VENV_BIN)/pip install pytest pytest-cov pytest-asyncio pytest-mock
	$(VENV_BIN)/pip install black flake8 isort mypy pylint
	$(VENV_BIN)/pip install sphinx mkdocs mkdocs-material
	@echo "$(GREEN)✅ Development installation complete$(NC)"

check:
	@echo "$(CYAN)Checking dependencies...$(NC)"
	$(PYTHON) requirement-check.py

# ==================== RUNNING ====================
run:
	@echo "$(CYAN)🦀 Starting DELTA-ATRAX-V2...$(NC)"
	$(PYTHON) $(APP_NAME).py

run-interactive:
	@echo "$(CYAN)🦀 Starting DELTA-ATRAX-V2 (Interactive)...$(NC)"
	$(PYTHON) $(APP_NAME).py --interactive

run-web:
	@echo "$(CYAN)🦀 Starting DELTA-ATRAX-V2 (Web Dashboard)...$(NC)"
	$(PYTHON) $(APP_NAME).py --web --port 5000

run-daemon:
	@echo "$(CYAN)🦀 Starting DELTA-ATRAX-V2 (Daemon)...$(NC)"
	nohup $(PYTHON) $(APP_NAME).py > /dev/null 2>&1 &
	@echo "$(GREEN)✅ Running in background$(NC)"

# ==================== TESTING ====================
test:
	@echo "$(CYAN)Running tests...$(NC)"
	$(VENV_BIN)/pytest tests/ -v --tb=short

test-cov:
	@echo "$(CYAN)Running tests with coverage...$(NC)"
	$(VENV_BIN)/pytest tests/ -v --cov=. --cov-report=html --cov-report=term

test-specific:
	@echo "$(CYAN)Running specific test...$(NC)"
	$(VENV_BIN)/pytest tests/$(TEST) -v

# ==================== CODE QUALITY ====================
lint:
	@echo "$(CYAN)Running linters...$(NC)"
	$(VENV_BIN)/flake8 $(APP_NAME).py --max-line-length=120 --ignore=E501,W503
	$(VENV_BIN)/mypy $(APP_NAME).py --ignore-missing-imports
	$(VENV_BIN)/pylint $(APP_NAME).py --disable=C0111,C0103,R0903
	@echo "$(GREEN)✅ Linting complete$(NC)"

format:
	@echo "$(CYAN)Formatting code...$(NC)"
	$(VENV_BIN)/black $(APP_NAME).py --line-length 120
	$(VENV_BIN)/isort $(APP_NAME).py --profile black
	@echo "$(GREEN)✅ Formatting complete$(NC)"

security:
	@echo "$(CYAN)Running security checks...$(NC)"
	$(VENV_BIN)/pip install safety bandit
	$(VENV_BIN)/safety check -r requirements.txt
	$(VENV_BIN)/bandit -r . -f json -o security-report.json
	@echo "$(GREEN)✅ Security check complete$(NC)"

# ==================== DOCKER ====================
docker-build:
	@echo "$(CYAN)Building Docker image...$(NC)"
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .
	@echo "$(GREEN)✅ Docker image built$(NC)"

docker-build-no-cache:
	@echo "$(CYAN)Building Docker image (no cache)...$(NC)"
	docker build --no-cache -t $(DOCKER_IMAGE):$(DOCKER_TAG) .
	@echo "$(GREEN)✅ Docker image built$(NC)"

docker-run:
	@echo "$(CYAN)Running Docker container...$(NC)"
	docker run -it --rm \
		--name $(DOCKER_IMAGE) \
		-p 5000:5000 \
		-p 8080:8080 \
		-p 4444:4444 \
		--cap-add NET_ADMIN \
		--cap-add NET_RAW \
		-v $(PWD)/.delta_atrax_v2:/app/.delta_atrax_v2 \
		-v $(PWD)/delta_atrax_reports:/app/delta_atrax_reports \
		$(DOCKER_IMAGE):$(DOCKER_TAG)

docker-run-daemon:
	@echo "$(CYAN)Running Docker container (daemon)...$(NC)"
	docker run -d \
		--name $(DOCKER_IMAGE) \
		-p 5000:5000 \
		-p 8080:8080 \
		-p 4444:4444 \
		--cap-add NET_ADMIN \
		--cap-add NET_RAW \
		-v $(PWD)/.delta_atrax_v2:/app/.delta_atrax_v2 \
		-v $(PWD)/delta_atrax_reports:/app/delta_atrax_reports \
		--restart unless-stopped \
		$(DOCKER_IMAGE):$(DOCKER_TAG)

docker-stop:
	@echo "$(CYAN)Stopping Docker containers...$(NC)"
	docker stop $(DOCKER_IMAGE) || true
	docker rm $(DOCKER_IMAGE) || true
	@echo "$(GREEN)✅ Containers stopped$(NC)"

docker-logs:
	@echo "$(CYAN)Viewing Docker logs...$(NC)"
	docker logs -f $(DOCKER_IMAGE)

docker-shell:
	@echo "$(CYAN)Opening shell in container...$(NC)"
	docker exec -it $(DOCKER_IMAGE) /bin/bash

docker-clean:
	@echo "$(CYAN)Cleaning Docker resources...$(NC)"
	docker stop $(DOCKER_IMAGE) || true
	docker rm $(DOCKER_IMAGE) || true
	docker rmi $(DOCKER_IMAGE):$(DOCKER_TAG) || true
	docker system prune -f
	@echo "$(GREEN)✅ Docker cleanup complete$(NC)"

# ==================== DOCKER COMPOSE ====================
docker-compose-up:
	@echo "$(CYAN)Starting all services with Docker Compose...$(NC)"
	$(DOCKER_COMPOSE) up -d
	@echo "$(GREEN)✅ Services started$(NC)"

docker-compose-down:
	@echo "$(CYAN)Stopping all services...$(NC)"
	$(DOCKER_COMPOSE) down
	@echo "$(GREEN)✅ Services stopped$(NC)"

docker-compose-logs:
	@echo "$(CYAN)Viewing Compose logs...$(NC)"
	$(DOCKER_COMPOSE) logs -f

docker-compose-build:
	@echo "$(CYAN)Building with Docker Compose...$(NC)"
	$(DOCKER_COMPOSE) build

docker-compose-restart:
	@echo "$(CYAN)Restarting services...$(NC)"
	$(DOCKER_COMPOSE) restart

# ==================== CLEANUP ====================
clean:
	@echo "$(CYAN)Cleaning temporary files...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	find . -type d -name ".mypy_cache" -delete
	find . -type f -name "*.log" -delete
	rm -rf .coverage htmlcov/ .tox/ dist/ build/ *.egg-info/
	rm -rf .delta_atrax_v2/temp/*
	@echo "$(GREEN)✅ Cleanup complete$(NC)"

clean-all: clean
	@echo "$(CYAN)Cleaning everything...$(NC)"
	rm -rf $(VENV)
	rm -rf .delta_atrax_v2/
	rm -rf delta_atrax_reports/
	rm -rf __pycache__/
	@echo "$(GREEN)✅ Full cleanup complete$(NC)"

# ==================== BACKUP ====================
backup:
	@echo "$(CYAN)Creating backup...$(NC)"
	@mkdir -p backups
	tar -czvf backups/delta-atrax-backup-$$(date +%Y%m%d-%H%M%S).tar.gz \
		.delta_atrax_v2/ \
		delta_atrax_reports/ \
		config/ \
		--exclude='*.log' \
		--exclude='temp/*'
	@echo "$(GREEN)✅ Backup created$(NC)"

restore:
	@echo "$(CYAN)Available backups:$(NC)"
	@ls -la backups/
	@echo "Usage: make restore BACKUP=backups/backup-file.tar.gz"

# ==================== DOCUMENTATION ====================
docs:
	@echo "$(CYAN)Generating documentation...$(NC)"
	$(VENV_BIN)/mkdocs build
	@echo "$(GREEN)✅ Documentation generated$(NC)"

docs-serve:
	@echo "$(CYAN)Serving documentation...$(NC)"
	$(VENV_BIN)/mkdocs serve

# ==================== DATABASE ====================
db-backup:
	@echo "$(CYAN)Backing up database...$(NC)"
	cp .delta_atrax_v2/delta_atrax_v2.db backups/db-$$(date +%Y%m%d-%H%M%S).db
	@echo "$(GREEN)✅ Database backed up$(NC)"

db-migrate:
	@echo "$(CYAN)Running database migrations...$(NC)"
	$(PYTHON) -c "from delta_atrax_v2 import DatabaseManager; DatabaseManager()"
	@echo "$(GREEN)✅ Database migrated$(NC)"

# ==================== MONITORING ====================
status:
	@echo "$(CYAN)🦀 DELTA-ATRAX-V2 Status$(NC)"
	@echo "=============================="
	@docker ps --filter "name=delta" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" || true
	@echo ""
	@echo "Disk Usage:"
	@du -sh .delta_atrax_v2/ 2>/dev/null || echo "No data directory"
	@du -sh delta_atrax_reports/ 2>/dev/null || echo "No reports directory"

health:
	@echo "$(CYAN)Health Check$(NC)"
	@curl -s http://localhost:5000/health || echo "Web dashboard not running"
