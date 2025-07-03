# Advanced Mocking Concepts

## Using `side_effect`

- The `side_effect` attribute on a mock allows you to control its behavior beyond a single return value.
- **List of values:** When `side_effect` is set to a list, each call to the mock returns the next item in that list, in order.
- **Callable:** When `side_effect` is a function, it is called with the same arguments as the mock, and its return value is used as the mock’s return.
- **Exception:** When `side_effect` is an exception, it will raise that exception when the original function is called.
- Use a list when you know the sequence and order of calls; use a function when behavior should vary based on arguments.

## Choosing between Mock and MagicMock

- **`Mock`:** A simple replacement that only creates attributes when accessed, and raises errors for undefined methods or attributes.
- **`MagicMock`:** Inherits from `Mock` and implements Python’s magic methods (`__len__`, `__enter__`, etc.) by default.
- Use `Mock` by default for stubbing external dependencies to catch unintended interactions.
- Use `MagicMock` only when mocking objects that require special behavior, such as context managers or iterables.
