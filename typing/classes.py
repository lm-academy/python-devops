from __future__ import annotations
from typing import Self, Optional

# Section: Classes as Type Hints


class Server:
    def __init__(
        self,
        hostname: str,
        ip_address: str,
        os_type: str = "Linux",
    ):
        self.hostname: str = hostname
        self.ip_address: str = ip_address
        self.os_type: str = os_type
        self.is_online: bool = False

    def connect(self) -> None:
        print(
            f"Connecting to {self.hostname} (IP address: {self.ip_address})"
        )
        self.is_online = True
        print(f"{self.hostname} is online.")

    def get_status(self) -> str:
        return "online" if self.is_online else "offline"


def deploy_app_to_server(
    target_server: Server, app_name: str
) -> bool:
    print(
        f"Deploying {app_name} to server: {target_server.hostname}"
    )

    if not target_server.is_online:
        target_server.connect()

    print(
        f"Deployment of {app_name} to {target_server.hostname} successful."
    )
    return True


web_server = Server(
    hostname="web01.dev.local", ip_address="10.0.1.10"
)
db_server = Server(
    hostname="db01.dev.local", ip_address="10.0.2.20"
)

deploy_app_to_server(web_server, "FrontendApp")
deploy_app_to_server(db_server, "UserDBApi")


# Section: Hinting Methods Within a Class


class Calculator:
    def __init__(self, initial_value: int | float = 0):
        self.total: int | float = initial_value

    def add(self, value: int | float) -> Self:
        self.total += value

        return self

    def subtract(self, value: int | float) -> Self:
        self.total -= value

        return self

    def multiply_by(self, value: int | float) -> Self:
        self.total *= value

        return self

    def divide_by(self, value: int | float) -> Self:
        self.total /= value

        return self

    def get_total(self) -> int | float:
        return self.total


my_calc = Calculator(1)

print(my_calc.add(2).subtract(1).multiply_by(10).get_total())

# Section: Forward References (Strings)


class Employee:
    def __init__(
        self, name: str, manager: Optional[Employee] = None
    ) -> None:
        self.name: str = name
        self.manager: Optional[Employee] = manager
        self.reports: list[Employee] = []

    def add_report(self, report: Employee) -> None:
        self.reports.append(report)


ceo = Employee("ceo")
manager1 = Employee("Alice", ceo)
ceo.add_report(manager1)
