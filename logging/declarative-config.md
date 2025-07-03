# Declarative Logging Configuration

- Declarative configuration separates setup from code, making it easier to maintain and adjust.
- Python’s `logging.config` module supports both INI-style (`fileConfig`) and dictionary-based (`dictConfig`) configurations.
- Configuration objects can be loaded from files (INI, JSON, YAML) or defined in code.
- Benefits include environment-specific overrides, less boilerplate, and clearer visibility of logger/handler relationships.

## INI-Style Configuration with `fileConfig`

- Uses an INI-format file to define loggers, handlers, and formatters.
- Sections: `[loggers]`, `[handlers]`, `[formatters]`, plus one section per named logger/handler/formatter.
- Good for simple setups and backwards compatibility, but less flexible for dynamic structures.

## Dictionary-Based Configuration with `dictConfig`

- Configuration defined as a Python dict, offering full programmatic control.
- Keys: `version`, `disable_existing_loggers`, and mappings for `formatters`, `handlers`, `loggers`, and optionally `root`.
- Easy to build or modify at runtime, and to serialize/deserialize via JSON/YAML.

## Loading Configuration from JSON or YAML

- Store the same dict-based schema in a JSON/YAML file for external editing.
- Read and parse the file, then pass the resulting dict to `dictConfig`.
- Enables separation of concerns: ops teams can tweak logging without touching code.

## Dynamic and Programmatic Adjustments

- You can modify the config dict at runtime before calling `dictConfig`.
- Handlers, formatters, and levels can be added, removed, or tweaked based on environment variables or feature flags.
- Example: switch file logging on/off depending on a `DEBUG` flag.
