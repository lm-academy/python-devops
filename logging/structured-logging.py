# Configuring python-json-logger
print("Configuring python-json-logger")
print("---------\n")

import logging
import sys
from pythonjsonlogger.json import JsonFormatter


json_logger = logging.getLogger("demo.json")
json_logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
json_formatter = JsonFormatter(
    "{asctime}{levelname}{message}",
    style="{",
    json_indent=4,
    rename_fields={"asctime": "timestamp", "levelname": "level"},
)
handler.setFormatter(json_formatter)

json_logger.addHandler(handler)

json_logger.info("Structured logging initialized")

# Logging with extra context
print("Logging with extra context")
print("---------\n")

extra_context = {
    "user_id": "devops1",
    "request_id": "request-12345abc",
    "source_ip": "10.0.0.5",
}

json_logger.warning(
    "Request took longer than 5s to complete",
    extra=extra_context,
)

# Logging exceptions as JSON
print("Logging exceptions as JSON")
print("---------\n")

try:
    result = 1 / 0
except ZeroDivisionError:
    json_logger.exception(
        "Unexpected calculation error",
        extra={"operation": "division"},
    )
