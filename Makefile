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


.PHONY: venv
venv: bin/python

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


BIN:=esp8266-20190529-v1.11.bin
.PHONY: micropython
micropython: esp8266-20190529-v1.11.bin
esp8266-20190529-v1.11.bin:
	wget http://micropython.org/resources/firmware/${BIN}

# You have to set it,
PORT:=/dev/ttyUSB9
.PHONY: flash
flash: micropython
	esptool.py --before default_reset --after hard_reset --baud 115200 --chip esp8266 --port ${PORT} write_flash 0x0 ${BIN}

.PHONY: erase
erase:
	bin/esptool.py --port ${PORT} erase_flash

homeassistant_config:
	mkdir -p ${@}

.PHONY: hass
hass: homeassistant_config
	bin/hass -c homeassistant_config

