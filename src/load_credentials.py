import os
from logger import logger, log

def load_secret(secret_key):
    log(logger.info, "Loading secret", f"{secret_key=}")
    secret_value = os.environ.get(secret_key)
    if secret_value is None:
        log(logger.critical, "Loading secret failed", f"{secret_key=}")
        raise ValueError
    log(logger.debug, "Secret loaded", f"{secret_value=}")
    return secret_value
