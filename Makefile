.PHONY: run test

run:
	python3 src/main.py $(ARGS)

test:
	python3 -m unittest discover -s src
