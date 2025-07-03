# Fixtures in Pytest

- As tests grow more complex, repeating setup and cleanup steps makes tests harder to read and maintain.
- Pytest fixtures allow centralizing shared setup and teardown logic, promoting DRY code.
- Fixtures prepare resources or data before tests and can optionally clean up after tests complete.

## What is a Fixture?

- A fixture in Pytest is a function decorated with `@pytest.fixture` that provides a baseline environment or data for tests.
- Fixtures can supply test data, manage the test environment (e.g., temporary files, mock services), and provide reusable resources (e.g., client objects).
- Tests request fixtures by declaring them as function arguments, and Pytest handles executing the fixture and injecting its result.

## Defining a Simple Fixture with `@pytest.fixture`

- Use `@pytest.fixture` above a function to mark it as a fixture that can return or yield resources.
- A fixture that returns a value runs its setup code, returns the value, and skips teardown logic.
- A fixture that yields a value transforms into a generator: code before `yield` is setup, the yielded value goes to the test, and code after `yield` is teardown.

## Using Fixtures in Test Functions

- Tests receive fixture results by naming them as parameters; Pytest locates and executes matching fixtures automatically.
- This approach removes boilerplate setup code from tests and keeps test functions concise.

## Fixture Scope and Lifecycle

- Fixture scope controls how often setup and teardown run: `function` (default), `class`, `module`, or `session`.
- A `function`-scoped fixture runs for each test function; a `session`-scoped fixture runs only once for the entire test session.
- Choosing the right scope balances resource isolation (function scope) against efficiency (session scope).

## Fixture Teardown (Cleanup)

- To ensure cleanup logic executes after tests, define fixtures with `yield` rather than `return`.
- Code after `yield` always runs, even if the test fails or raises an error.
- This pattern mimics a `try...finally` block, ensuring resources like temporary files or connections are properly released.

## `conftest.py`: Sharing Fixtures

- Defining fixtures in a `conftest.py` file makes them available across multiple test modules without explicit imports.
- Placing `conftest.py` in a test directory or its parent enables automatic discovery of shared fixtures.
- This structure keeps fixture definitions centralized and tests cleaner.
