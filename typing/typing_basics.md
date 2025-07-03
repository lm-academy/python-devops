# Introduction

- Python is a dynamically typed language, meaning you can assign values to variables without declaring their types, and type checking happens at runtime.
- While this offers rapid development and flexibility, it can lead to ambiguity and late discovery of type-related bugs in larger or collaborative projects.
- Type hints (PEP 484, introduced in Python 3.5) let you optionally annotate your code with expected types for variables, function parameters, and return values without changing Python’s runtime behavior.
- These annotations are leveraged by static type checkers (e.g., MyPy), IDEs for better autocompletion and error highlighting, and by developers for clearer, more maintainable code.

## Why Use Type Hints?

- Type hints improve readability by making explicit what data types functions expect and return, which is invaluable when navigating unfamiliar or legacy code.
- Static type checkers like MyPy can catch mismatches between hinted and actual types before the code runs, surfacing bugs early in the development cycle.
- IDEs (e.g., VS Code, PyCharm) use hints to enhance autocompletion accuracy, provide inline type checking, and support safe refactoring.
- Explicit annotations act as a contract in collaborative environments, helping team members understand and correctly use each other’s code.
- For example, annotating a function as `def process_user_data(user: dict) -> bool:` makes it clear that the function expects a `dict` and returns a `bool`.

## Basic Type Hint Syntax

- To annotate a variable, use `variable_name: type = value`. This syntax (variable annotations) was introduced in Python 3.6 (PEP 526).
- Example: `config_path: str = "/etc/app.conf"` indicates that `config_path` is intended to be a string.
- Function parameters are annotated with `param_name: param_type`, and the return type is specified after `->` before the colon.
- Example: `def get_server_status(hostname: str, port: int) -> str:` declares that the function takes a `str` and an `int`, and returns a `str`.

## Common Built-in Types for Hinting

- Standard built-ins such as `int`, `float`, `bool`, `str`, and `bytes` are directly usable in annotations.
- Collections can be hinted with `list`, `tuple`, `set`, and `dict`. For more precise element types:
  - In Python 3.9 and later (PEP 585), you can use built-in generics: `list[int]`, `dict[str, int]`.
  - In earlier versions, import from the `typing` module: `from typing import List, Dict` and use `List[int]`, `Dict[str, int]`.
- The special type `None` is used for functions that do not return a meaningful value (e.g., `-> None`).
- Advanced types like `Optional`, `Union`, and others will be covered when exploring the `typing` module in a later lecture.

## Python Remains Dynamically Typed

- Type hints do not alter Python’s runtime behavior; passing arguments of the wrong type won’t raise a hint-related error unless an operation in the code fails for the actual type.
- For instance, calling `process_id("user-123")` on a function annotated as `def process_id(user_id: int) -> None:` runs without a hint-triggered error, though passing a string where an integer is expected may lead to a `TypeError` later if arithmetic is attempted.
- Static analysis tools flag these mismatches before execution, but Python itself enforces types only when invalid operations occur at runtime.

## Common Pitfalls & How to Avoid Them

- **Believing hints enforce types at runtime:** Hints guide tools and developers, but Python ignores them unless you use a runtime checking library.
- **Over-hinting or incorrect hints:** Overly complex or wrong annotations can confuse readers and static checkers; start simple and use `Any` for truly dynamic values.
- **Forgetting `typing` imports:** When using `List[int]`, `Optional[str]`, etc., remember to import them from the `typing` module (unless you rely on built-in generics in Python 3.9+).
- **Relying on hints for untyped libraries:** If a third-party library lacks type hints or has them in separate stub files, static analysis may be limited—consult documentation or stub packages.
