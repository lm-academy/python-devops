from typing import (
    Callable,
    Any,
    TypeVar,
    ParamSpec,
    Generator,
    Iterable,
)
import functools

# Section: Typing Decorators (simple_logging_decorator)


def simple_logging_decorator(
    func: Callable[..., Any],
) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"LOG: Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__} returned {result}")

        return result

    return wrapper


@simple_logging_decorator
def add(x: int, y: int) -> int:
    return x + y


result_add = add(3, 5)

# Section: Typing Decorators (better_logging_decorator with TypeVar)

P = ParamSpec("P")
R = TypeVar("R")


def better_logging_decorator(
    func: Callable[P, R],
) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
        print(f"LOG: Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__} returned {result}")

        return result

    return wrapper


@better_logging_decorator
def subtract(x: int, y: int) -> int:
    return x - y


result_subtract = subtract(3, 5)


# Section: Typing Generators


def count_up_to(limit: int) -> Generator[int, None, str]:
    for i in range(limit):
        yield i

    return "Counting complete!"


def accumulate_and_send() -> (
    Generator[float, float | None, None]
):
    total = 0.0

    try:
        while True:
            sent = yield total

            if sent:
                total += sent
    except GeneratorExit:
        pass


test_accumulate = accumulate_and_send()
next(test_accumulate)
print(test_accumulate.send(1.0))
print(next(test_accumulate))
print(test_accumulate.send(2.0))
print(test_accumulate.send(3.0))
print(next(test_accumulate))

# Section: Iterable & Iterator


def process_items(items: Iterable[str]) -> list[str]:
    return [item.upper() for item in items]


print(process_items(["a", "b"]))
print(process_items(("a", "b")))
print(process_items({"a", "b"}))
print(process_items({"a": "b", "hello": "world"}))
