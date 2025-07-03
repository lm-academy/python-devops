# Adding Type Hints to Decorators and Generators

- Decorators and generators are advanced constructs that require specialized type hints to make their transformations and data flows explicit.
- Properly typed decorators allow MyPy to understand how they preserve or change function signatures.
- Typed generators clarify the types of values yielded, values accepted via `.send()`, and final return values.

## Typing Decorators

- Decorators take a function (`Callable`) and return a new function; using `Callable[..., Any]` types them broadly but loses specific signature information.
- To preserve the original function’s signature, define a `TypeVar` bound to `Callable[..., Any]` and use it for both the decorator’s input and output types.
- Inside the decorator, the wrapper can use `*args: Any, **kwargs: Any -> Any`, while `TypeVar` ensures the decorated function’s overall type remains correct.

## Typing Generators

- Use `Generator[YieldType, SendType, ReturnType]` to specify a generator’s yield type, the type accepted by `.send()`, and its return type on completion.
- If a generator does not use `send()`, set `SendType` to `None`; if it has no explicit `return`, set `ReturnType` to `None`.
- The `count_up` generator is typed as `Generator[int, None, str]`, yielding integers and returning a string message.
- The `accumulate_and_send` generator is typed as `Generator[float, float, None]`, yielding a running total, accepting floats via `send()`, and returning nothing.

## Iterable & Iterator

- For functions that consume sequences of items, use `Iterable[T]` to accept any iterable of `T` (lists, tuples, generators).
- Use `Iterator[T]` when a function specifically expects an iterator object supporting `__next__()`.
