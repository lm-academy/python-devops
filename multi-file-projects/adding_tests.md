# Adding Tests to a Multi-File Project

## Standard Project Layout with Tests

To maintain a clean and organized codebase, it is standard practice to separate your application code from your test code. This is typically achieved by creating a dedicated `tests` directory at the project's root level.

- The project root contains the main application package (e.g., `devops_utils`) and the `tests` directory as siblings.
- The `tests` directory houses all the test files. It is common for the structure inside `tests` to mirror the structure of the application package to keep tests organized as the project grows.
- It is also good practice to place an empty `__init__.py` file inside the `tests` directory to ensure it can be treated as a package if needed, although `pytest`'s discovery mechanism is powerful enough to work without it in most cases.

## Importing Application Code into Tests

To test your application code, your test files must import the functions, classes, and variables that need to be verified. The standard and most robust way to do this is by using absolute imports that start from the project root.

- A test file, such as `tests/test_file_ops.py`, will use an import statement like `from devops_utils.file_ops import check_file_extension`.
- This import syntax assumes that the project's root directory is on Python's module search path (`sys.path`).
- Attempting to run a test file directly as a Python script will fail with a `ModuleNotFoundError`, because the project root is not automatically added to the path in that context. This is why a test runner like `pytest` is necessary.

## Running `pytest` for Project Discovery

The `pytest` framework is designed to handle the complexities of testing structured projects. When you run `pytest` from your project's root directory, it intelligently prepares the environment for test execution.

- Pytest begins by scanning upwards from the current directory to find a configuration file (like `pyproject.toml` or `pytest.ini`), which it uses to identify the project's root.
- Once the root is identified, `pytest` automatically adds this directory to `sys.path`.
- With the path correctly configured, the absolute imports within your test files will resolve successfully, allowing your tests to find and execute the application code.

## Robust Test Execution with `python -m pytest`

While running `pytest` directly is often sufficient, an even more reliable method is to invoke it as a module using the `python -m` flag. This approach is highly recommended, especially in automated environments like CI/CD pipelines.

- The command `python -m pytest` guarantees that the current working directory is added to `sys.path` before `pytest` begins its execution.
- This method eliminates many path-related ambiguities that can arise in complex project structures or different operating environments.
- It is considered the most robust and explicit way to run your test suite, ensuring consistent behavior across different machines and setups.

## Common Pitfalls & How to Avoid Them

When setting up tests for a multi-file project, there are several common issues that can be easily avoided.

- **`ModuleNotFoundError` during test runs:** This is the most frequent problem and is almost always caused by running `pytest` from the wrong directory. To avoid this, always run `pytest` from the project root, or preferably use `python -m pytest`. An editable install (`pip install -e .`) provides the most robust solution.
- **Tests importing other tests:** This is considered an anti-pattern as it creates implicit dependencies between tests. If you need to share test logic or data, use `conftest.py` to define shared fixtures.
- **Using relative imports in tests:** Imports like `from ..devops_utils import ...` are fragile and should be avoided in test files. Always use absolute imports from the project root (e.g., `from devops_utils.file_utils import ...`).
