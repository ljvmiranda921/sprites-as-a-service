venv:
	python3 -m venv venv
	venv/bin/pip3 install pip-tools

requirements.txt: requirements.in ## create requirements
	venv/bin/pip-compile -o requirements.txt \
	--no-header \
	--no-index \
	--no-emit-trusted-host \
	requirements.in


requirements-dev.txt: requirements-dev.in ## create requirements
	venv/bin/pip-compile -o requirements-dev.txt \
	--no-header \
	--no-index \
	--no-emit-trusted-host \
	requirements-dev.in

build: venv requirements.txt ## setup environment
	venv/bin/pip-sync requirements.txt

dev: venv requirements-dev.txt # setup dev environment
	venv/bin/pip-sync requirements-dev.txt

