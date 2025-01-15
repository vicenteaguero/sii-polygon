# install.sh

pip install poetry

poetry config virtualenvs.in-project true
poetry install

# To run python scripts
# poetry run python {path_to_script}