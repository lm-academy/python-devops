# Python Virtual Environments with `venv`

## Why Virtual Environments?

Managing dependencies for different projects can be challenging. For instance:

- Project A might need an older version of a library (like `boto3`).
- Project B might need the latest version of the same library.

Installing libraries globally can lead to version conflicts, often called "dependency hell," where updating a library for one project breaks another.

Virtual environments solve this by creating isolated directories for each project. Each environment contains:

- A specific Python interpreter.
- Its own set of installed packages (`site-packages`).

This ensures that project dependencies are kept separate and self-contained.

## Using `venv`

Python 3 includes a built-in module, `venv`, which is the standard way to create virtual environments.

### Creating an Environment

1.  Navigate to your project's root directory in your terminal.
2.  Run the command:
    ```bash
    python3 -m venv .venv
    ```
    - `python3 -m venv`: Executes the `venv` module.
    - `.venv`: The conventional name for the directory containing the virtual environment files. This directory will hold a copy/link of the Python interpreter and associated package directories.

### Activating the Environment

Creating the environment isn't enough; you must _activate_ it for your current shell session. Activation modifies your shell's `PATH` environment variable, ensuring that the `python` and `pip` commands prioritize the versions inside the `.venv` directory.

- **How to Activate:** Use the activation script located within the environment's directory (e.g., inside `.venv/bin/` or `.venv/Scripts/`, depending on the OS where it was created). The exact command depends on your shell.
- **Indication:** Once activated, your shell prompt typically changes to show the name of the active environment (e.g., `(.venv)`).

### Installing Dependencies

With the environment active, use `pip` to install packages. They will be installed _only_ within the active virtual environment:

```bash
pip install <package_name>
# Example: pip install boto3
```

### Deactivating the Environment

To exit the virtual environment and return to your global Python context, simply run:

```bash
deactivate
```

The indicator (e.g., `(.venv)`) will disappear from your prompt.

## Avoid `sudo pip`

Using `venv` means packages are installed within your project's `.venv` directory, which is owned by your user. This eliminates the need and the risks associated with using `sudo pip install`. Always install project dependencies into an activated virtual environment using `pip install <package>`.
