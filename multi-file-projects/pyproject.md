# Editable Installs with `pyproject.toml`

In the previous lecture, we established a clean pattern for running packaged scripts using `python -m`, which solved common import and warning issues. While this method works, it's a workaround for a more fundamental problem: the Python interpreter doesn't automatically know about our project's structure. The modern and most robust solution is to formally define our project as an installable package. By creating a standard `pyproject.toml` metadata file, we can perform an "editable install" using the command `pip install -e .`. This seamlessly links our source code into the virtual environment, making our packages importable from anywhere without manual path hacks or special commands. This is the standard, professional workflow for developing Python applications.

## The `pyproject.toml` File

The `pyproject.toml` file is the modern, unified standard for configuring Python projects, replacing older files like `setup.py`.

- It is written in the simple and readable TOML (Tom's Obvious, Minimal Language) format.
- It defines the project's build system, such as `setuptools`, in the `[build-system]` table.
- It specifies essential project metadata, like the package name, version, and dependencies, in the `[project]` table.
- It can also serve as a central location for configuring development tools like formatters and linters.

## Editable Installs: `pip install -e .`

An "editable" or "development" install is a special mode for installing packages with `pip`.

- The command `pip install -e .` installs the project from the current directory in "editable" mode.
- Instead of copying files, it creates a special link from the virtual environment's `site-packages` directory back to the original source code.
- The main benefit is that any changes made to the source `.py` files are immediately reflected in the installed package without needing to run `pip install` again.

## Solving the Import Problem Permanently

Performing an editable install provides a definitive solution to the path and import issues encountered during development.

- After an editable install, the project is effectively on `sys.path` for the entire activated virtual environment.
- There is no longer any need to manually set the `PYTHONPATH` environment variable.
- You can now run scripts that are inside packages directly, and they will be able to use absolute imports from the project root.
- This approach creates a self-contained and reproducible environment, which is the standard for professional Python development.

## Console Scripts vs. `python -m`

While a script with an `if __name__ == "__main__"` block can be run with `python -m`, defining a console script in `pyproject.toml` is the preferred professional approach.

- **User Experience:** A console script (`ping-check`) is short and intuitive. A `python -m` command is long, exposes the internal module path, and is easy to mistype.
- **Abstraction:** A console script hides your project's internal structure. You can refactor your code internally, and as long as you update the `pyproject.toml` file, the command remains the same for the user. The `python -m` command breaks if you rename or move the target file.
- **Clarity of Intent:** Declaring a script in `pyproject.toml` clearly marks it as a public, supported command-line interface for your package.
