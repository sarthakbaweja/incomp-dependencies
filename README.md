# incomp-depend

A Python project built with Python 3.9.

## Project Structure

```
incomp-depend/
├── src/
│   └── incomp_depend/
│       ├── __init__.py
│       └── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

1. Create a virtual environment:
   ```bash
   python3.9 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the project in development mode:
   ```bash
   pip install -e .
   ```

## Running the Project

```bash
python src/incomp_depend/main.py
```

## Development

### Code Formatting
```bash
black src/
```

### Linting
```bash
flake8 src/
```

### Type Checking
```bash
mypy src/
```

### Running Tests
```bash
pytest
```

## License

MIT
