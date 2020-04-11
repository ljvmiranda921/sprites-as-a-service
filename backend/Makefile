venv:
	python3 -m venv venv
	venv/bin/pip3 install pip-tools

requirements.txt: requirements.in ## create requirements
	venv/bin/pip-compile -o requirements.txt \
	--no-header \
	--no-index \
	--no-emit-trusted-host \
	requirements.in

build: venv requirements.txt ## setup dev environment
	venv/bin/pip-sync requirements.txt

