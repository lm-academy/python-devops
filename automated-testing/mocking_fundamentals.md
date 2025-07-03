# Mocking Fundamentals

# Introduction

- When unit testing DevOps scripts that interact with external systems, tests can become slow, unreliable, difficult to set up, or even destructive.
- Mocking replaces these real dependencies with controlled, fake objects so that tests run quickly and deterministically.
- Python’s built-in `unittest.mock` module provides tools to create and configure these mock objects and to track interactions.

# What is Mocking?

- Mocking involves creating objects that mimic the behavior of real functions or classes in a controlled environment.
- When your code calls a mocked object, you can specify what it returns, simulate exceptions, or inspect how it was called.
- This allows you to isolate the logic under test and avoid side effects from actual external calls.

# Using unittest.mock.patch

- The `patch` function replaces a target object with a mock in a specified scope, either for the duration of a function (decorator) or within a context block (`with`).
- As a decorator, `patch` injects the mock into the test function’s parameters; as a context manager, it yields the mock within the `with` block.
- It’s important to patch the object where it is looked up in the module under test, not necessarily where it is originally defined.

# MagicMock and Configuring Mock Objects

- When you patch an object, you typically receive a `MagicMock` instance that you can configure.
- Use `mock.return_value` to define what the mock will return when called.
- Use `mock.side_effect` to simulate an exception being raised by the mock when invoked, to pass different values to be returned by each execution, or to pass a calable to replace the implemented function.
- Assertion methods like `assert_called_with` and `assert_called_once` let you verify interactions with the mock.

# Common Mocking Scenarios in DevOps

- **Network API Calls:** Mock `requests.get` or `requests.post` to simulate successful responses, HTTP errors, or timeouts.
- **Filesystem Operations:** Mock functions like `open()` or `os.path.exists()` to simulate file presence or content.
- **Subprocess Execution:** Mock `subprocess.run` to avoid running real system commands and control return codes.
- **Time-Dependent Code:** Patch `time.sleep` or mock `datetime.now()` to remove delays and make time-based tests deterministic.
