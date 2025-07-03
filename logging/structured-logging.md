# Introduction to Structured Logging

- Plain-text logs are hard to parse and brittle to format changes.
- Structured logging records events as key-value data, making machine parsing trivial.
- JSON is a de-facto standard: human-readable yet easily ingested by ELK, Splunk, DataDog, etc.
- Python’s `python-json-logger` integrates JSON output into the standard `logging` workflow.

## Configuring `python-json-logger`

- Install via `pip install python-json-logger==3.3.0` (for consistency, I'm pinning the version; removing it will install the latest version available).
- Replace `logging.Formatter` with `pythonjsonlogger.JsonFormatter`.
- Specify a format string listing the LogRecord attributes you want as JSON keys.
- Attach to any `Handler` just like a normal `Formatter`.

## Logging with Extra Context

- Pass a dict to the `extra` parameter of `logger.<level>()`.
- Keys in `extra` become top-level JSON fields.
- Use for request IDs, user IDs, session tokens, or any domain data.

## Logging Exceptions as JSON

- Use `logger.exception(...)` inside an `except` block.
- The `JsonFormatter` automatically adds an `exc_info` key with the traceback.
- This preserves full error context for downstream analysis.
