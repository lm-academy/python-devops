import pytest
from typing import Iterable

ManagedResource = dict[str, str]


@pytest.fixture
def managed_resource() -> Iterable[ManagedResource]:
    print("  [SHARED FIXTURE]: acquiring resource lock")
    resource = {"status": "lock_acquired"}
    yield resource
    print("  [SHARED FIXTURE]: releasing resource lock")
    resource["status"] = "lock_released"
