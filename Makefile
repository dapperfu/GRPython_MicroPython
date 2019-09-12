IPYNB:=$(wildcard *.ipynb)
MD:=$(patsubst %.ipynb,markdown/%.md,${IPYNB})

.PHONY: markdowns
markdowns: bin/python ${MD}

.PHONY: clean
clean:
	git clean -xfd

.PHONY: debug
debug:
	$(info $${IPYNB}=${IPYNB})
	$(info $${MD}=${MD})

.PHONY: logger
logger: bin/python
	bin/flask run --host=0.0.0.0



bin/python:
	python3.7 -mvenv .
	bin/pip install --upgrade wheel setuptools pip
	bin/pip install -r requirements.txt

markdown:
	mkdir -p ${@}

markdown/%.md: %.ipynb markdown
	bin/jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to markdown --output=${@} ${<}

uPyLoader-linux:
	curl -OL https://github.com/BetaRavener/uPyLoader/releases/download/v0.1.4/uPyLoader-linux
