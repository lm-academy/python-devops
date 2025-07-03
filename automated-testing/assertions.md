# Assertions in Pytest

- Pytest uses Python’s built-in `assert` statement to declare expected conditions in tests, making test code concise and readable.
- When an `assert` expression evaluates to `True`, execution continues; if it evaluates to `False`, an `AssertionError` is raised and Pytest marks the test as failed.
- Pytest intercepts assertion failures to provide detailed, introspective feedback on why an assertion failed.

## The `assert` Statement

- The `assert` keyword checks that an expression is truthy; if it’s falsy, Python raises `AssertionError`.
- You can append an optional message: `assert expression, "message"`, which will be shown if the assertion fails.
- In plain Python, `assert x == 5` does nothing when true, while `assert x == 10, "x should be 10"` raises an error with that message if the condition is false.

## Pytest and `assert`

- Pytest enhances the built-in `assert` by inspecting the expression’s values and rewriting the failure message to show variable states.
- Common assertion patterns include:
  - Equality and inequality checks to compare expected versus actual values.
  - Truthiness or falsiness checks to verify that objects are non-empty or evaluate to `False`.
  - Membership checks using `in` or `not in` to assert presence or absence in containers.
  - Comparison operators (`<`, `>`, `<=`, `>=`) to verify ordering conditions.

## Pytest’s Rich Failure Output

- When an assertion fails, Pytest displays the values from the expression and highlights exactly where they differ.

## Asserting Floating-Point Numbers (`pytest.approx`)

- Floating-point arithmetic can yield tiny precision errors, so direct equality comparisons may fail unexpectedly.
- Pytest provides `pytest.approx` to compare floats within a tolerance, supporting both relative and absolute tolerances.

## Asserting Exceptions (`pytest.raises`)

- Use `with pytest.raises(ExpectedException):` as a context manager to assert that a block of code raises a specific exception.
- You can include `match="regex"` to verify that the exception message matches a given pattern.
- This allows testing both that the correct error type is raised and that its message contains expected details.

## Common Pitfalls & How to Avoid Them

- Avoid overly complex expressions in a single `assert`; break them into multiple simpler assertions for clarity.
- Always use `pytest.approx` for floating-point comparisons to prevent false negatives from tiny precision differences.
