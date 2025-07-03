print("Main script starting...")

from devops_utils import check_file_extension
import sys

print(sys.path)

filenames = ["config.yaml", "script.sh"]

for filename in filenames:
    print(f"Checking {filename}")
    print(f"Result: {check_file_extension(filename)}")
