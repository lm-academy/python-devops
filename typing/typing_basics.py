# Section: Basic Type Hint Syntax - Variable Annotations
config_path: str = "/etc/app.conf"
retry_count: int = 3
is_enabled: bool = bool(1)
servers: list[str] = ["web01", "web02"]
settings: dict[str, int | str] = {"port": 8080, "user": "admin"}


# Section: Basic Type Hint Syntax - Function Argument and Return Type Annotations
def get_server_status(hostname: str, port: int) -> str:
    print(f"Checking {hostname}:{port}")
    if port == 80:
        return "Online"
    else:
        return "Unknown"


# Section: Python Remains Dynamically Typed
def process_id(user_id: int) -> None:
    print(
        f"Processing user ID: {user_id} (type: {type(user_id)})"
    )


# Demonstration of dynamic typing
process_id(1234)
# process_id("user-1234") # Uncommenting will lead to a static type checking error.
