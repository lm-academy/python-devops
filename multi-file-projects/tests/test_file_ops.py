from pathlib import Path
from devops_utils.file_utils.file_ops import parse_yaml_file


def test_parse_valid_yaml(tmp_path: Path) -> None:
    config_content = "service: my_app\nport: 8080"
    yaml_file: Path = tmp_path / "config.yaml"
    yaml_file.write_text(config_content)

    parsed_data = parse_yaml_file(str(yaml_file))

    assert isinstance(parsed_data, dict)
    assert parsed_data["service"] == "my_app"
    assert parsed_data["port"] == 8080
