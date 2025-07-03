# Pytest Markers

- Markers are decorators (`@pytest.mark.<markername>`) applied to tests to attach metadata.
- Built-in markers like `skip`, `skipif`, `xfail`, and `parametrize` provide predefined behaviors.
- Custom markers (e.g., `slow`, `integration`, `api`) help categorize tests by project-specific criteria.
- Applying markers allows Pytest (and plugins) to filter, select, or modify tests during collection and execution.

## Skipping Tests Unconditionally: `@pytest.mark.skip`

- The `skip` marker unconditionally prevents a test from running, useful when a feature is disabled or under refactor.
- Skipped tests show an `s` in the summary along with the provided reason.
- Use `@pytest.mark.skip(reason="...")` to disable tests without removing their code.

## Skipping Tests Conditionally: `@pytest.mark.skipif`

- The `skipif` marker skips tests only when a specified condition evaluates to true at collection time.
- Conditions can be expressions like `sys.platform != "linux"` or checks for optional dependencies.
- This enables platform-specific, version-specific, or resource-dependent test filtering.

## Expected Failures: `@pytest.mark.xfail`

- The `xfail` marker marks tests expected to fail due to known bugs or unimplemented features.
- Expected failures are reported as `XFAIL` and don’t cause the suite to fail; unexpected passes are reported as `XPASS`.

## Custom Markers and Registration

- Custom markers (e.g., `slow`, `api`, `integration`) help organize and categorize tests by functionality or runtime.
- Tests can have multiple markers for fine-grained control (e.g., `@pytest.mark.api` and `@pytest.mark.integration`).
- To avoid warnings, register custom markers in `pytest.ini` or `pyproject.toml` under the `markers` option.

## Running Tests by Marker (m option)

- The `-m <expression>` CLI option selects tests matching a marker expression.
- Expressions support logical operators: `and`, `or`, and negation with `not`.
- Examples: `pytest -m slow`, `pytest -m "not slow"`, `pytest -m "api and integration"`.

## Common Pitfalls & How to Avoid Them

- Overusing `skip` hides failures; prefer `xfail` for known bugs to maintain visibility.
- Complex `skipif` conditions reduce readability; delegate logic to helper functions when needed.
- Typos in marker names create unregistered markers; register all custom markers to catch errors early.
- Forgetting to register markers leads to warnings; always define marker descriptions in configuration files.
