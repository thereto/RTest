import yaml

def load_config():
    with open("config/config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)

CONFIG = load_config()
BASE_URL = CONFIG["base_url"]
DEFAULT_HEADERS = CONFIG["default_headers"]
LOGIN_INFO = CONFIG["login"]
