from text_analysis import calculate_text_attributes
import pytest

# Section: The `assert` Statement

# Uncomment to play around with Python assertions

# x: int = 5

# assert x == 5  # Nothing will happen, because this is True
# assert (
#     x == 10
# ), "x should be 10, but it's not!"  # Raise an AssertionError

# Section: Pytest and `assert`


def test_string_equality() -> None:
    expected_status = "SUCCESS"
    actual_status = "success".upper()

    assert actual_status == expected_status


def test_word_count() -> None:
    text = "Deploying microservice to Kubernetes cluster."
    text_empty = ""

    assert (calculate_text_attributes(text)["word_count"]) == 5
    assert (
        calculate_text_attributes(text_empty)["word_count"]
    ) == 0


def test_unique_words() -> None:
    text = "Deploying microservice to Kubernetes cluster."
    text_with_duplicates = "Deploying deploying."
    text_empty = ""

    text_results = calculate_text_attributes(text)
    text_with_duplicates_result = calculate_text_attributes(
        text_with_duplicates
    )
    text_empty_results = calculate_text_attributes(text_empty)

    assert (len(text_results["unique_words"])) == 5
    assert (
        len(text_with_duplicates_result["unique_words"])
    ) == 1
    assert (len(text_empty_results["unique_words"])) == 0


def test_average_word_length() -> None:
    text = "Deploying microservice to Kubernetes cluster."  # 40 / 5 = 8
    text_with_duplicates = "Deploying deploying."  # 18 / 2 = 9
    text_empty = ""  # 0

    text_results = calculate_text_attributes(text)
    text_with_duplicates_result = calculate_text_attributes(
        text_with_duplicates
    )
    text_empty_results = calculate_text_attributes(text_empty)

    assert (text_results["average_word_length"]) == 8.0
    assert (
        text_with_duplicates_result["average_word_length"]
    ) == 9.0
    assert (text_empty_results["average_word_length"]) == 0.0


def test_longest_word() -> None:
    text = "Deploying microservice to Kubernetes cluster."  # microservice
    text_with_duplicates = "Deploying deploying."  # deploying
    text_empty = ""

    text_results = calculate_text_attributes(text)
    text_with_duplicates_result = calculate_text_attributes(
        text_with_duplicates
    )
    text_empty_results = calculate_text_attributes(text_empty)

    assert (
        text_results["longest_word"].lower()
    ) == "microservice"
    assert (
        text_with_duplicates_result["longest_word"].lower()
    ) == "deploying"
    assert (text_empty_results["longest_word"]) == ""


# Section: Pytest’s Rich Failure Output


@pytest.mark.xfail  # We're marking the test as an expected failure
def test_string_mismatch() -> None:
    expected = "HEllo WOrlD"
    actual = "hello world"

    assert expected == actual


# Section: Asserting Floating-Point Numbers (`pytest.approx`)


def test_float_with_approx() -> None:
    calculated_val = 0.1 + 0.2
    expected_val = 0.3

    assert calculated_val == pytest.approx(expected_val)  # type: ignore


# Section: Asserting Exceptions (`pytest.raises`)


def test_raises_exception() -> None:
    with pytest.raises(ZeroDivisionError):
        _division = 1 / 0
