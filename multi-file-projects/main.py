print("Main script starting...")

from devops_utils import (
    check_file_extension,
    is_host_up,
    check_hosts_from_config,
)
import sys

print(sys.path)

filenames = ["config.yaml", "script.sh"]

for filename in filenames:
    print(f"Checking {filename}")
    print(f"Result: {check_file_extension(filename)}")

print(f"\nIs localhost up? {is_host_up("localhost")}")
print(
    f"Is nonexistenthost12345 up? {is_host_up("nonexistenthost12345")}"
)

print(
    f"\nAre all hosts from servers_config.yaml up? {check_hosts_from_config("servers_config.yaml")}"
)
