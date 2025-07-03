from typing import TypedDict, NotRequired


class User(TypedDict):
    id: int
    name: str
    email: str
    phone: NotRequired[str]


user: User = {
    "id": 123,
    "name": "Alice",
    "email": "alice@example.com",
    "phone": "+123456789",
}

print(f"User data: {user.get("email")}")
