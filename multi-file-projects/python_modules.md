# Python Modules and the `import` System

## What is a Module?

- A module in Python corresponds directly to a single file containing Python code.
- The module's name is derived from its filename.
- Any file with a `.py` extension can be treated as a module.
- The name used to import the module is the filename without the `.py` suffix. For example, a file named `file_ops.py` is imported as the `file_ops` module.

## The `import` Statement

- The most straightforward way to import a module is with `import module_name`
- To use functions, variables, or classes from the imported module, you must prefix them with the module name and a dot, such as `module_name.function_name`.
- This method creates a dedicated namespace for the imported module, which is highly effective at preventing name collisions. For instance, a variable named `CONFIG` in your script will not conflict with `module_name.CONFIG`.
- It enhances code clarity by making it obvious where each function or variable originates, which is especially helpful in larger projects.

## The from...import Statement

- It's possible to bring only specific objects from a module with `from ... import ...`.
- You can use the `as` keyword to rename an imported object, for example, `from file_ops import parse_yaml_file as parse_yaml`.
- This approach can make code more concise because it requires less typing (`parse_yaml()` instead of `file_ops.parse_yaml_file()`).
- The primary drawback is the increased risk of name collisions. If you import a function named `my_function` and later define your own function with the same name, the original import will be overwritten.
- Using `from module import *` is strongly discouraged because it imports all public names from the module, which can pollute the local namespace and make the code difficult to read and debug.

## How Python Finds Modules: sys.path

When you execute an `import` statement, Python needs to locate the corresponding module file. It does this by searching through a specific list of directories.

- The search path is stored in a list of strings called `sys.path`, which is part of the standard `sys` module.
- The `sys.path` list is automatically populated and typically includes the directory of the script that is currently running, directories specified in the `PYTHONPATH` environment variable, and the default locations where Python and third-party packages are installed.
- The fact that the script's own directory is the first entry on this path is why a script like `main.py` can seamlessly import `utils.py` when both files are located in the same folder.
