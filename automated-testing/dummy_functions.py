import requests
import os
import subprocess
from typing import Optional, Any


def get_user_data(user_id: str | int) -> dict[str, str | int]:
    response = requests.get(
        f"https://api.example.com/users/{user_id}"
    )
    print(f"Status code: {response.status_code}")
    response.raise_for_status()
    return response.json()


def check_file_exists(filepath: str | os.PathLike[str]) -> bool:
    return os.path.exists(filepath)


def get_external_ip():
    """Fetches the current external IP from an external service."""
    try:
        response = requests.get(
            "https://api.ipify.org?format=json", timeout=5
        )
        response.raise_for_status()
        return response.json().get("ip")
    except requests.exceptions.RequestException:
        return None


def get_current_user() -> Optional[str]:
    try:
        result = subprocess.run(
            ["whoami"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
        return result.stdout.strip()
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
    ):
        return None


def fetch_both_endpoints() -> (
    tuple[dict[str, Any], dict[str, Any]]
):
    """
    Fetch data from two endpoints and return their JSON responses as a tuple.
    """
    response2 = requests.get("https://api.example.com/second")
    response2.raise_for_status()
    data2 = response2.json()

    response1 = requests.get("https://api.example.com/first")
    response1.raise_for_status()
    data1 = response1.json()

    return data1, data2
