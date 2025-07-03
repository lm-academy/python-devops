# Configuring Pytest

- As you start using Pytest extensively, typing `-v` or `-m` on the command line every time becomes tedious.
- Centralize your defaults in `pyproject.toml` under the `[tool.pytest.ini_options]` table.
- A single source of truth means every developer—and your CI system—runs tests with the same settings.
- Putting Pytest alongside other PEP 518 tools (Black, isort, Flake8) keeps your repo tidy and consistent.

## Why a Configuration File?

- **Consistency:** Run `pytest` without remembering flags; everyone gets the same behavior.
- **Simplicity:** Remove boilerplate from docs and CI scripts.
- **Project-specific discovery:** Set `testpaths`, `python_files` and markers in one place.
- **Cleaner output:** Declare markers to silence `PytestUnknownMarkWarning`, enable color and rich tracebacks by default.

## Configuration File Hierarchy

Pytest searches for settings in this order, using the first match from the current or a parent directory:

1. `pyproject.toml` under `[tool.pytest.ini_options]`
2. `pytest.ini`
3. `tox.ini` with a `[pytest]` section
4. `setup.cfg` under `[tool:pytest]`

Embrace `pyproject.toml` as the modern hub for all your tool configurations.

## Creating `pyproject.toml`

1. Create or open `pyproject.toml` at your project root.
2. Add a `[tool.pytest.ini_options]` table.
3. Define your defaults using TOML syntax and inline strings.

## Common Configuration Options

- `addopts`  
  Defines default command-line flags that Pytest applies on every run (verbosity, reporting, color, etc.).

- `markers`  
  Pre-registers custom markers with descriptions so that you can categorize tests and avoid unknown-marker warnings.

- `testpaths`  
  Restricts test discovery to the listed directories, preventing Pytest from scanning other parts of the project.

- `python_files`  
  Specifies filename patterns that Pytest treats as test files (e.g., `test_*.py`).

- `python_classes`  
  Indicates class name patterns Pytest will consider when looking for test classes (e.g., classes starting with `Test`).

- `python_functions`  
  Sets function name patterns Pytest uses to identify individual test functions (e.g., functions beginning with `test_`).

- Other options
  - `norecursedirs`: directories to skip during discovery
  - `minversion`: enforce a minimum Pytest version
  - `filterwarnings`: configure how warnings are handled
  - and many more built-in settings for fine-tuning
