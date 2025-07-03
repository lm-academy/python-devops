# Introduction

- As our Python automation projects grow, defining custom classes helps model complex objects and should be reflected in type hints for clearer code and stronger static checking.
- Annotating functions and methods with user-defined classes lets MyPy verify correct usage of attributes and methods.

# Classes as Type Hints

- Any class you define becomes a valid type; you can annotate parameters and return values with it.
- MyPy will ensure that calls to such functions pass instances of the expected class and that attribute access matches the class definition.

# Hinting Methods Within a Class

- Inside class methods, `self` is implicitly the class type; annotate other parameters and return types normally.
- MyPy checks method bodies to ensure you only access attributes and call methods that exist on the class.
- **New in Python 3.11**: You can use `typing.Self` for methods that return the instance, for example `def clone(self) -> Self:`.

# Forward References (Strings)

- Use string literals for type hints when referring to a class that is defined later in the file or in circular scenarios.
- Enabling `from __future__ import annotations` defers evaluation of all annotations, simplifying forward references.
