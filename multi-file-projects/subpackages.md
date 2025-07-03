# Importing from Subpackages

## Project Structure with Subpackages

To improve organization, we can group related modules into their own dedicated subpackages. A subpackage is a directory inside a parent package that contains its own `__init__.py` file.

- A top-level package, like `devops_utils`, can contain multiple subpackages.
- For example, we can create a `file_utils` subpackage for file-related modules and a `network_utils` subpackage for networking modules.
- Each of these subdirectories must contain an `__init__.py` file (which can be empty) to be recognized by Python as a package.

## Absolute Imports

An absolute import provides the complete, explicit path to a module starting from a top-level directory that is on Python's search path (`sys.path`).

- The syntax follows the project's directory structure, such as `from package.subpackage.module import function`.
- This is the most recommended and readable way to import modules, particularly in top-level scripts that execute the application's logic.
- Absolute imports are unambiguous and clearly state the origin of the imported code, which greatly improves code maintainability. For example, a script outside the `devops_utils` package would use `from devops_utils.file_utils.file_ops import check_file_extension` to access a function.

## Relative Imports

A relative import specifies the path to a module based on the location of the file performing the import. This is done using dot notation.

- The syntax uses dots to navigate the package hierarchy: `.` refers to the current package, while `..` refers to the parent package.
- An import like `from .sibling_module import name` brings in a name from a module in the same directory. An import like `from ..parent_sibling.module import name` navigates one level up and then down into a sibling package.
- Relative imports are primarily used for communication _within_ a package. Their main advantage is that they make the package self-contained; if you rename the top-level package, the internal relative imports will not break.

## The ImportError Trap with Relative Imports

A significant pitfall arises when you attempt to directly execute a Python file that contains relative imports. This action will almost always result in an error.

- Running a script like `python devops_utils/network_utils/network_ops.py` will raise an `ImportError: attempted relative import with no known parent package`.
- This happens because when a file is run directly, Python sets its name (`__name__`) to `"__main__"` and does not recognize it as being part of a package. Consequently, it cannot resolve relative paths like `.` or `..`.
- The rule of thumb is that relative imports should only be used for intra-package imports, and the application should be started from a top-level script that uses absolute imports to access the package's functionality.
