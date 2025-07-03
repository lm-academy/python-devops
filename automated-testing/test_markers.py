import pytest
import time

try:
    import some_optional_library  # type: ignore
except ModuleNotFoundError:
    some_optional_library = None
# Section: Skipping Tests Unconditionally: @pytest.mark.skip


@pytest.mark.skip(
    reason="Skipping experimental feature until completion."
)
def test_new_experimental_feature() -> None:
    assert False


# Section: Skipping Tests Conditionally: @pytest.mark.skipif


@pytest.mark.skipif(
    some_optional_library is None,
    reason="Requires 'some_optional_library' to be installed.",
)
def test_with_optional_dependency() -> None:
    print(
        f"Running tests that depends on an optional library..."
    )
    assert some_optional_library


# Section: Expected Failures: @pytest.mark.xfail


@pytest.mark.xfail(
    reason="Bug #123: Division by zero not handled properly."
)
def test_divide_by_zero() -> None:
    _division = 1 / 0
    assert False


@pytest.mark.xfail  # Add strict=True to make XPASS lead to a failure
def test_expected_to_fail() -> None:
    assert True


# Section: Custom Markers and Registration


@pytest.mark.slow
def test_very_long_computations() -> None:
    time.sleep(5)
    assert True


@pytest.mark.api
@pytest.mark.smoke
def test_user_creation() -> None:
    assert True


# Section: Running Tests by Marker (m option)
