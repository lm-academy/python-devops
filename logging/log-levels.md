# Log Levels in Practice

- Python defines five standard levels with increasing severity:
  - **DEBUG (10):** Detailed diagnostic information.
  - **INFO (20):** Confirmation that things are working normally.
  - **WARNING (30):** An indication of potential problems or deprecation.
  - **ERROR (40):** A failure in a specific operation.
  - **CRITICAL (50):** A serious error causing program termination.
- **NOTSET (0)** causes a logger to inherit its parent’s effective level.
- Appropriate use of these levels lets you adjust verbosity without changing code.

## Two-Stage Filtering: Logger vs Handler

- **Logger Level:** First gate: records below `logger.level` are discarded immediately.
- **Handler Level:** Second gate: each handler only emits records at or above its `handler.level`.
- This allows, for example, DEBUG messages to be logged to a file but only WARNING and above to the console.

## Configuring Logger & Handlers

- Use `logger.setLevel(...)` to control which messages the logger accepts.
- Use `handler.setLevel(...)` to control which accepted messages each handler emits.
- Attach multiple handlers for different outputs (e.g., console vs file) with independent levels.
