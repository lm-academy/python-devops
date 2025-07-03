print("Module file_ops is being imported")

from typing import Any

try:
    import yaml
except (ModuleNotFoundError, ImportError):
    print(
        "Warning: PyYAML not found, parse_yaml_file will not work."
    )
    yaml = None


SUPPORTED_EXTENSIONS: list[str] = [".json", ".yaml", ".txt"]


def check_file_extension(filename: str) -> bool:
    """Checks if a file has a supported extension"""
    print(
        f"  - file_ops.check_file_extension called for {filename}"
    )
    return any(
        filename.endswith(ext) for ext in SUPPORTED_EXTENSIONS
    )


def parse_yaml_file(path_str: str) -> dict[str, Any]:
    """Parses a YAML file and returns its contents."""
    print(f"  - file_ops.parse_yaml_file called for {path_str}")
    if yaml:
        with open(path_str, "r") as file:
            return yaml.safe_load(file)
    else:
        return {}
