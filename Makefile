requirements.txt: pyproject.lock
	mkdir -p build
	python3 -m venv build/.build-env
	. ./build/.build-env/bin/activate
	poetry install --no-dev
	pip freeze > requirements.txt
	deactivate
	rm -rf build/.build-env
