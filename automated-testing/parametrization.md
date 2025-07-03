# Parametrized Tests

## Introduction

- Often, we need to test the same logic with different inputs and outputs, such as validating various IP address or hostname formats.
- Writing individual test functions for each case leads to repetitive code and a test suite that is harder to maintain.
- Parametrized tests allow a single test function to run multiple times with different data, adhering to the DRY principle and simplifying test maintenance.

## The Problem: Duplicated Test Logic

- A function that checks valid hostname character codes must be tested across letters, digits, hyphens, and invalid symbols.
- Without parametrization, each input case requires its own test function, duplicating the assertion logic.
- This approach increases verbosity and makes the test suite more error-prone and tedious to update.

## Solution: @pytest.mark.parametrize

- The `@pytest.mark.parametrize(argnames, argvalues)` decorator takes argument names and a list of value tuples to generate multiple test invocations.
- Argument names can be provided as a comma-separated string or as a list of strings.
- Each tuple in the `argvalues` list corresponds to a separate run of the test function, with tuple elements mapped to argument names.
- Running Pytest with `-v` shows each parametrized case as a distinct test, simplifying result interpretation.

## The `pytest.param` Construct

- The `pytest.param()` function wraps a set of parameter values and allows you to attach metadata to that invocation:
  - `id`: a custom label shown in the test report.
  - `marks`: one or more markers (e.g., `pytest.mark.xfail`, `pytest.mark.skip`) applied only to that case.
- This is useful when you want to:
  - Give human-readable names to complex or ambiguous parameter sets.
  - Mark individual cases as expected failures or skip them selectively.

## Customizing Test IDs

- By default, Pytest creates IDs from parameter values, which may be non-descriptive for complex data.
- You can use `pytest.param(..., id="custom_id")` to assign clear, human-readable names to individual cases.
- Alternatively, an `ids` list passed to `parametrize` can specify identifiers in the order of `argvalues`.
- Custom IDs make it easier to identify failing cases in test reports and improve overall readability.
