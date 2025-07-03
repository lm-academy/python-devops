print("Main script starting...")

from file_ops import check_file_extension as check_file
import sys

print(sys.path)

filenames = ["config.yaml", "script.sh"]

for filename in filenames:
    print(f"Checking {filename}")
    print(f"Result: {check_file(filename)}")
