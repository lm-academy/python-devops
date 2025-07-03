from typing import Optional, Any

# Section: Typing Lists

hostnames: list[str] = ["web01.example.com", "db01.example.com"]
open_ports: list[int] = [80, 443, 22]


def process_hostnames(hosts: list[str]) -> None:
    for host in hosts:
        print(f"Processing host: {host.upper()}")


process_hostnames(hostnames)
# process_hostnames(open_ports) # Uncommenting will lead to type error

# Section: Typing Dictionaries

server_config: dict[str, str] = {
    "hostname": "app01.prod",
    "ip_address": "10.0.5.20",
    "os_type": "Linux",
}

user_roles: dict[str, list[str]] = {
    "user-123": ["admin", "editor"],
    "user-456": ["dev", "viewer"],
}

# Section: Typing Tuples

server_status: tuple[str, int, bool] = (
    "api.example.com",
    443,
    True,
)

ip_parts: tuple[int, ...] = (192, 168, 1, 100)

# Section: Typing Sets

admin_users: set[str] = {"alice", "bob", "charlie"}


def is_admin(username: str, admins: set[str]) -> bool:
    return username in admins


# Section: Union[X, Y, ...] for Multiple Possible Types

identifier: str | int = "abcde-1234"
identifier = 1234


def process_mixed_data(data: list[int | str]) -> None:
    for item in data:
        if isinstance(item, str):
            print(f"Processing string: {item.upper()}")
        else:
            print(f"Processing int: {item * 2}")


# Section: Optional[X] for Values That Can Be None


def find_user(user_id: str) -> Optional[dict[str, str]]:
    if user_id == "123":
        return {
            "id": "123",
            "name": "Admin user",
            "email": "admin@example.com",
        }

    return None


found_user = find_user("123")

if found_user:
    print(f"Found user: {found_user["name"]}")


# Section: Any for Unrestricted Types
def print_anything(item: Any) -> None:
    print(f"Item: {item}, type: {type(item)}")


print_anything(1)
print_anything("hello")
