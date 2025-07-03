import sys

# Both relative and absolute import work
# from .network_ops import is_host_up
from devops_utils.network_utils.network_ops import is_host_up


def main():
    print("UPDATED Executing check_host")
    print(sys.path)
    print(is_host_up("localhost"))


if __name__ == "__main__":
    main()
