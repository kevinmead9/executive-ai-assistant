import yaml
from pathlib import Path

_CONFIG_PATH = Path(__file__).parent / "config.yaml"

# Pre-load config at import time to avoid blocking I/O in async context
with open(_CONFIG_PATH) as _stream:
    _DEFAULT_CONFIG = yaml.safe_load(_stream)


def get_config(config: dict):
    # This loads things either ALL from configurable, or
    # all from the config.yaml
    # This is done intentionally to enforce an "all or nothing" configuration
    if "email" in config["configurable"]:
        return config["configurable"]
    else:
        return _DEFAULT_CONFIG
