import subprocess
from ..file_utils.file_ops import parse_yaml_file


def is_host_up(hostname: str) -> bool:
    """Pings a host to check if it's reachable."""
    print(f"  - network_ops.is_host_up called for {hostname}")
    try:
        result = subprocess.run(
            [
                "ping",
                "-c",
                "1",
                hostname,
            ],  # on Windows, -n instead of -c
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )

        return result.returncode == 0
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
    ):
        return False


def check_hosts_from_config(config_path: str) -> bool:
    """Checks if all hosts in config file are reachable."""
    print(
        f"  - network_ops.check_hosts_from_config called for {config_path}"
    )

    config_data = parse_yaml_file(config_path)
    hosts = config_data.get("hosts", [])

    if not hosts:
        print("No hosts available")
        return False

    return all(is_host_up(hostname) for hostname in hosts)
