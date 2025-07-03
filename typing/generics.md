# Introduction to Generics

- Generic types let you write reusable, type-safe functions and classes that work uniformly across different data types.
- They preserve the relationship between input and output types, enabling MyPy to infer precise types instead of falling back to `Any`.
- The `typing` module’s `TypeVar` and `Generic` primitives unlock this capability.

## The Need for Generics

- Annotating with `Any` sacrifices type information, so tools cannot guarantee correct usage of returned values.
- A generic abstraction retains knowledge of the specific type in each context, improving IDE support and static checks.
- For example, a "first-item" function should return `str` for a `list[str]` and `int` for a `list[int]`, not just `Any`.

## Defining Type Variables

- `T = TypeVar('T')` declares a placeholder type variable `T` that can stand for any type.
- A function annotated `def get_first_item_generic(data: List[T]) -> Optional[T]:` returns an element of the same type as the list elements.
- MyPy infers `T` from each call site, preserving specific return types like `Optional[str]` or `Optional[int]`.

## Constrained Type Variables

- When a generic should only accept certain types, constrain it: `NumberType = TypeVar('NumberType', int, float)`.
- Functions like `def add_generic_numbers(x: NumberType, y: NumberType) -> NumberType:` then only accept `int` or `float` and return that same type.
- Constrained type variables combine flexibility with necessary restrictions for safe operations.

## Bounded Type Variables

- When a generic should only accept subclasses of a specific superclass, we can use a type bound, constrain it: `NumberType = TypeVar('NumberType', bound=Superclass)`.
- Functions like `def add_generic_numbers(x: NumberType, y: NumberType) -> NumberType:` then accept any subclass of `Superclass`, and they can be different subclasses for each argument.
- Like constrained type variables, bounded type variables provide useful functionalities combining flexibility and type safety.

## Generic Classes

- Inherit from `Generic[T]` to define a class parameterized by a type variable `T`.
- A class like `SimpleStack[T]` can push, pop, and peek items of type `T`, and MyPy will enforce that only `T` instances are used.
- This pattern creates custom container types that maintain strong type guarantees for their contents.

## Common Pitfalls & How to Avoid Them

- A class that uses `T` in its methods but does not inherit from `Generic[T]` is not recognized as generic by MyPy.
- Unconstrained `TypeVar('T')` can degrade type safety when operations require certain capabilities—use bounds or explicit type lists when appropriate.
