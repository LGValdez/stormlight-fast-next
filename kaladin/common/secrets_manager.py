import json
from os import path


def load_secrets() -> dict:
    base_path = path.dirname(__file__)
    file_path = path.abspath(path.join(base_path, "..", "config", "secrets.json"))
    with open(file_path) as secrets_file:
        secrets = json.load(secrets_file)
    return secrets
