# Common Types in Python

- Python’s built-in dynamic typing allows rapid development without declaring variable types, but it can lead to ambiguous code and late discovery of type errors in larger projects.
- The `typing` module provides specialized type constructors to precisely describe the contents of collections (`list`, `dict`, `tuple`, `set`) and other complex scenarios.
- By using these constructors, you gain clearer documentation, stronger static analysis with tools like MyPy, and richer IDE support without changing Python’s runtime behavior.

## The `typing` Module

- On Python 3.9+, built-in generics (`list[int]`, `dict[str, str]`, `tuple[int, ...]`, `set[str]`, `frozenset[int]`) are available via PEP 585, deprecating `typing.List` etc. for these cases.
- Import specific constructors from `typing`, for example: `List`, `Dict`, `Tuple`, `Set`, `FrozenSet`, `Optional`, `Union`, `Any`.
- Using `typing` remains necessary for compatibility with older versions (Python 3.7/3.8) and for constructs like `Optional`, `Union`, `Literal`, and `TypedDict`.

## Typing Lists

- Use `list[X]` (or `List[X]` in Python < 3.9) to indicate a list whose elements are of type `X`.
- This makes it explicit if a function expects a list of strings (`list[str]`) or integers (`list[int]`), enabling static checkers to catch mismatches.

## Typing Dictionaries

- Use `dict[K, V]` (or `Dict[K, V]` in Python < 3.9) to specify a dictionary with keys of type `K` and values of type `V`.
- You can nest generics, for example `dict[int, list[str]]`, to model complex structures like mapping user IDs to role lists.

## Typing Tuples

- Fixed-length tuples with heterogeneous types use `tuple[T1, T2, ...]` (or `Tuple[T1, T2, ...]` in Python < 3.9).
- Variable-length tuples of a uniform type use `tuple[T, ...]` (or `Tuple[T, ...]`), though lists are often more natural for that use case.

## Typing Sets

- Use `set[X]` (or `Set[X]` in Python < 3.9) to indicate a set containing elements of type `X`.
- This clarifies that operations like membership checks (`in`) will compare values of the declared type.
- _Note:_ For immutable sets, use `frozenset[X]` (or `FrozenSet[X]` in Python < 3.9).

## Union[X, Y, ...] for Multiple Possible Types

- Use `Union[...]` when a value may be exactly one of several types (excluding `None` unless explicitly included).
- As of Python 3.10 you can write `int | str` instead of `Union[int, str]`.

## Optional[X] for Values That Can Be None

- `Optional[X]` is shorthand for `Union[X, None]`, indicating a value may be of type `X` or `None`.
- Static checkers will warn if you use an `Optional` value without first checking for `None`.

## Any for Unrestricted Types

- `Any` disables type checking for the annotated part, useful during gradual typing of legacy code or when truly dynamic types are needed.
- Overuse negates the benefits of static analysis, so prefer specific types whenever possible.

## Common Pitfalls & How to Avoid Them

- **Built-in Generics on Older Python:** Syntax like `list[int]` only works on Python 3.9+; use `typing.List[int]` for Python 3.7/3.8 compatibility.
- **Subtle Optional Defaults:** `def func(arg: Optional[str] = None)` clearly allows `None` as a default, whereas `def func(arg: str = None)` may confuse static checkers.
- **Excessive `Any`:** Reserving `Any` for truly dynamic cases preserves the value of static checking elsewhere in your code.
