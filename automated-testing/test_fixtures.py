import pytest
import tempfile
from pathlib import Path
from typing import Iterable
from conftest import ManagedResource

# Section: Defining a Simple Fixture with @pytest.fixture

ConfigDict = dict[str, int | str]


@pytest.fixture
def sample_config_dict() -> ConfigDict:
    return {
        "api_url": "https://test.api.example.com",
        "timeout": 30,
        "retries": 3,
    }


def test_api_url_is_present(sample_config_dict: ConfigDict):
    print("  [TEST]: test_api_url_is_present running...")
    assert "api_url" in sample_config_dict
    assert (
        sample_config_dict["api_url"]
        == "https://test.api.example.com"
    )


@pytest.fixture
def temp_config_file() -> Iterable[Path]:
    temp_file = tempfile.NamedTemporaryFile(
        mode="w+t",
        encoding="utf-8",
        suffix=".yaml",
        delete=False,
    )
    temp_file_path = Path(temp_file.name)
    print(
        f"\n   [FIXTURE SETUP]: temp_config_file created at {temp_file_path}"
    )
    temp_file.write("setting1: value1\nsetting2: value2\n")
    temp_file.close()
    yield temp_file_path
    print(
        f"\n   [FIXTURE TEARDOWN]: temp_config_file deleting {temp_file_path}"
    )
    if temp_file_path.exists():
        temp_file_path.unlink()


# Section: Using Fixtures in Test Functions


def test_read_from_temp_file(temp_config_file: Path):
    print("  [TEST] test_read_from_temp_file running...")
    assert temp_config_file.exists()
    content = temp_config_file.read_text(encoding="utf-8")
    assert "setting1: value1" in content


# Section: Fixture Scope and Lifecycle


@pytest.fixture(scope="session")
def expensive_resource() -> Iterable[ConfigDict]:
    print(
        "\n  [SESSION FIXTURE]: expensive_resource - creating..."
    )
    yield {"id": "session_resource", "value": 123}
    print(
        "\n  [SESSION FIXTURE]: expensive_resource - deleting..."
    )


def test_expensive_resource_id(expensive_resource: ConfigDict):
    print("  [TEST] test_expensive_resource_id running...")
    assert expensive_resource["id"] == "session_resource"


def test_expensive_resource_value(
    expensive_resource: ConfigDict,
):
    print("  [TEST] test_expensive_resource_value running...")
    assert expensive_resource["value"] == 123


@pytest.fixture(scope="session", autouse=True)
def global_setup() -> Iterable[None]:
    print("\n  [SESSION FIXTURE]: global_setup - creating...")
    yield
    print("\n  [SESSION FIXTURE]: global_setup - deleting...")


# Section: Sharing Fixtures with conftest.py
def test_managed_resource_status(
    managed_resource: ManagedResource,
):
    assert managed_resource["status"] == "lock_acquired"
