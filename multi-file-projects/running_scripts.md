# Running Scripts: `python -m` vs. `python file.py`

## The Core Difference: What is "Entry Point Zero"?

The key to understanding the difference lies in the first entry of `sys.path`. When Python initializes, it needs to know where to start looking for modules. The way you call it determines this "entry point zero".

- When you run a script directly using `python path/to/script.py`, the interpreter's main task is to execute that specific file. It sets the first entry of `sys.path` to be the directory that contains the script.

- When you run a script as a module using `python -m package.module`, the interpreter's goal is to locate and run a module within an importable package. It sets the first entry of `sys.path` to be the current working directory from which the command was executed. This allows absolute imports from the project root to succeed.

## Best Practice: Separating Library Code from Scripts

While you can run any file with `python -m`, it can lead to a `RuntimeWarning` if the file is both a library (meant to be imported) and a script (meant to be run). The best practice is to separate these roles.

- **Library Modules:** These files (like our `file_ops.py` and `network_ops.py`) should contain only reusable functions and classes. They should not contain an `if __name__ == "__main__":` block for complex script logic.
- **Runner Scripts:** For any action you want to make runnable from the command line, create a _new, separate_ script.

## Common Pitfalls & How to Avoid Them

- Running scripts inside packages directly with `python file.py` will often cause `ModuleNotFoundError` for absolute imports. Avoid this by always running packaged scripts from the project root using `python -m`.
- Making a single file both a complex library and a runnable script can lead to `RuntimeWarning`. Avoid this by separating concerns: create dedicated runner scripts that import from your library modules.
- Forgetting the module path when using `-m`. The command must be the full dotted path to the script from the project root (e.g., `python -m package.subpackage.script`).
