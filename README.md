# Singer Playground

A hands-on laboratory for mastering Singer - the open-source specification for writing scripts that move data between databases, web APIs, files, and more.

## 🎯 Purpose

This playground helps you:
- Understand Singer specification through practical examples
- Learn to work with taps (extractors) and targets (loaders)
- Build custom Singer taps and targets
- Master data replication patterns
- Practice data pipeline development

## 📂 Project Structure

```
singer-playground/
├── basics/
│   ├── 01-spec-exploration/      # Understanding Singer spec
│   ├── 02-tap-basics/           # Working with basic taps
│   ├── 03-target-basics/        # Working with basic targets
│   └── 04-stream-handling/      # Managing data streams
├── taps/
│   ├── api-tap/                 # Building API tap
│   ├── database-tap/            # Building database tap
│   ├── file-tap/               # Building file tap
│   └── custom-tap/             # Custom tap template
├── targets/
│   ├── database-target/        # Building database target
│   ├── file-target/           # Building file target
│   └── custom-target/         # Custom target template
└── advanced/
    ├── incremental/           # Incremental replication
    ├── state-management/      # State handling
    ├── error-handling/        # Error management
    └── testing/              # Tap/target testing
```

## 🎓 Learning Modules

### 1. Singer Fundamentals
- Understanding the Singer spec
- Message types (SCHEMA, RECORD, STATE)
- Stream handling
- Catalog management
- Configuration handling

### 2. Working with Taps
- Using existing taps
- Configuring tap properties
- Managing tap state
- Handling rate limits
- Error recovery

### 3. Working with Targets
- Using existing targets
- Target configuration
- Data type handling
- Batch processing
- Error handling

### 4. Custom Development
- Creating custom taps
- Building custom targets
- Writing tests
- Managing state
- Handling edge cases

## 💻 Hands-on Examples

### Basic Tap Usage
```bash
# Install a tap
pip install tap-github

# Run tap in discovery mode
tap-github --config config.json --discover > catalog.json

# Run tap with catalog
tap-github --config config.json --catalog catalog.json
```

### Basic Target Usage
```bash
# Install a target
pip install target-csv

# Run pipeline
tap-github --config tap-config.json | target-csv --config target-config.json
```

### Custom Tap Example
```python
import singer

def emit_schema():
    schema = {
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        }
    }
    singer.write_schema("users", schema, ["id"])

def emit_record(record):
    singer.write_record("users", record)
```

### State Management
```python
import singer

def save_state(value):
    singer.write_state({
        "bookmarks": {
            "users": {
                "last_record": value
            }
        }
    })
```

## 🔧 Common Patterns

### Configuration
```json
{
    "start_date": "2024-01-01T00:00:00Z",
    "api_token": "${API_TOKEN}",
    "batch_size": 100
}
```

### Catalog Selection
```json
{
    "streams": [
        {
            "tap_stream_id": "users",
            "schema": {...},
            "selected": true,
            "replication_method": "INCREMENTAL",
            "replication_key": "updated_at"
        }
    ]
}
```

## 🚀 Getting Started

1. Clone this repository:
```bash
git clone https://github.com/pesnik/singer-playground.git
cd singer-playground
```

2. Set up virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

3. Install dependencies:
```bash
pip install singer-python singer-tools
```

4. Navigate to a module:
```bash
cd basics/01-spec-exploration
```

## 📚 Resources

### Official Documentation
- [Singer Specification](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md)
- [Singer Best Practices](https://github.com/singer-io/getting-started/blob/master/docs/BEST_PRACTICES.md)
- [Singer Tools](https://github.com/singer-io/singer-tools)

### Community Resources
- [Singer.io](https://www.singer.io/)
- [Singer Taps Registry](https://github.com/singer-io/tap-tester)
- [Singer Slack](https://singer-slackin.herokuapp.com/)

### Related Projects
- [being-dataops-engineer](../being-dataops-engineer)
- [meltano-playground](../meltano-playground)
- [airbyte-playground](../airbyte-playground)

## 🧪 Testing

### Tap Testing
```bash
# Run tap tests
python -m pytest tests/test_tap.py

# Test discovery mode
tap-custom --config config.json --discover

# Test replication
tap-custom --config config.json --catalog catalog.json > output.json
```

### Target Testing
```bash
# Run target tests
python -m pytest tests/test_target.py

# Test with sample data
cat sample_records.json | target-custom --config config.json
```

## 🤝 Contributing

Contributions welcome! You can:
1. Add new examples
2. Improve documentation
3. Fix bugs
4. Add test cases
5. Share best practices

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Next Steps

After completing the modules in this playground:
1. Build a production-ready tap or target
2. Contribute to the Singer community
3. Integrate with other tools (Meltano, Airbyte)
4. Share your learnings
