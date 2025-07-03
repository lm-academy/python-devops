print("Module file_ops is being imported")

SUPPORTED_EXTENSIONS: list[str] = [".json", ".yaml", ".txt"]


def check_file_extension(filename: str) -> bool:
    """Checks if a file has a supported extension"""
    print(
        f"  - file_ops.check_file_extension called for {filename}"
    )
    return any(
        filename.endswith(ext) for ext in SUPPORTED_EXTENSIONS
    )
