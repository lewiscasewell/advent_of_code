# Variables
PYTHON := uv run python
YEAR := 2024
DAY := 01  # Default to day 01

# Scaffolding a new day
setup-day:
	@echo "Scaffolding day $(DAY) for year $(YEAR)..."
	@mkdir -p $(YEAR)/day$(DAY)
	@touch $(YEAR)/day$(DAY)/input.txt
	@touch $(YEAR)/day$(DAY)/example.txt
	@touch $(YEAR)/day$(DAY)/__init__.py
	@echo "from utils.input import read_input\n\ndef solve_part1(data):\n    return \"Not implemented\"\n\ndef solve_part2(data):\n    return \"Not implemented\"\n\nif __name__ == \"__main__\":\n    data = read_input(day=$(DAY), year=$(YEAR))\n    print(f\"Part 1: {{solve_part1(data)}}\")\n    print(f\"Part 2: {{solve_part2(data)}}\")" > $(YEAR)/day$(DAY)/main.py
	@echo "Scaffolded day $(DAY) for year $(YEAR)."

# Running a specific day
run-day:
	@echo "Running day $(DAY) for year $(YEAR)..."
	$(PYTHON) -m $(YEAR).day$(DAY).main
