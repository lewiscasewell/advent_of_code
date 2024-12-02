# Variables
PYTHON := uv run python
YEAR := 2024
DAY := 1

# Scaffolding a new day
setup-day:
	@echo "Scaffolding day $(DAY) for year $(YEAR)..."
	$(PYTHON) setup_day.py --day=$(DAY) --year=$(YEAR)
	@echo "Scaffolded day $(DAY) for year $(YEAR)."

# Running a specific day
run-day:
	@echo "Running day $(DAY) for year $(YEAR)..."
	$(PYTHON) -m $(YEAR).day$(DAY).main
