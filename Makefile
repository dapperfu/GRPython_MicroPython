.PHONY: clean
clean:
	git clean -xfd
	
.PHONY: venv
venv: bin/python

bin/python:
	python3.7 -mvenv .
	bin/pip install --upgrade wheel setuptools pip
	bin/pip install -r requirements.txt

.PHONY: logger
logger: bin/python
	bin/flask run --host=0.0.0.0

uPyLoader-linux:
	curl -L -o ${@} https://github.com/BetaRavener/uPyLoader/releases/download/v0.1.4/uPyLoader-linux
	chmod +x ${@}
	
.PHONY: uPyLoader
uPyLoader: uPyLoader-linux
	./${^}
	
webrepl/webrepl.html:
	git submodule update --init
	
.PHONY: webrepl
webrepl: webrepl/webrepl.html
	firefox ${^}

BIN:=esp8266-20190529-v1.11.bin
.PHONY: micropython
micropython: esp8266-20190529-v1.11.bin
esp8266-20190529-v1.11.bin:
	wget http://micropython.org/resources/firmware/${BIN}

# You have to set it,
PORT:=/dev/ttyUSB9
.PHONY: flash
flash: micropython
	bin/esptool.py --before default_reset --after hard_reset --baud 115200 --chip esp8266 --port ${PORT} write_flash 0x0 ${BIN}

.PHONY: erase
erase:
	bin/esptool.py --port ${PORT} erase_flash

homeassistant_config:
	mkdir -p ${@}

.PHONY: hass
hass: homeassistant_config
	bin/hass -c homeassistant_config

