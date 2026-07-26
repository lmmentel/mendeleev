# Mendeleev - Claude Code Assistant Guide

## Project Overview

**mendeleev** is a Pythonic periodic table of elements library that provides a convenient Python API for accessing various properties of elements, ions, and isotopes. It integrates with pandas for data access and offers visualization capabilities through bokeh, plotly, and seaborn.

- **Repository**: https://github.com/lmmentel/mendeleev
- **Documentation**: https://mendeleev.readthedocs.io
- **License**: MIT
- **Current Version**: 1.1.0

## Technology Stack

### Core Dependencies
- **Python**: 3.9 - 3.13
- **pandas**: Data manipulation and analysis (>=1.1.0)
- **SQLAlchemy**: Database ORM and data models (>=1.4.0)
- **pydantic**: Data validation and settings management (^2.9.2)
- **pint**: Unit conversions and physical quantities (^0.24.4)
- **numpy**: Numerical computing (^2.0)

### Development Tools
- **Poetry**: Dependency and environment management
- **pytest**: Testing framework (with pytest-xdist and pytest-cov)
- **Sphinx**: Documentation generation (with sphinx-material theme)
- **pre-commit**: Git hooks for code quality
- **ruff**: Linting and code formatting
- **alembic**: Database migrations
- **invoke**: Task automation

### Optional Visualization Dependencies
- **bokeh**: Interactive visualizations (^3.0)
- **plotly**: Interactive plots (^5.0)
- **seaborn**: Statistical visualizations (>=0.12)

## Project Structure

```
mendeleev/
├── mendeleev/           # Main package source code
│   ├── __init__.py
│   ├── models.py        # SQLAlchemy data models
│   ├── fetch.py         # Data fetching utilities
│   ├── db.py            # Database utilities
│   ├── econf.py         # Electronic configuration
│   ├── elements.db      # SQLite database with element data
│   ├── cli.py           # Command-line interface
│   ├── vis/             # Visualization modules
│   │   ├── bokeh.py
│   │   ├── plotly.py
│   │   ├── seaborn.py
│   │   └── utils.py
│   └── interfaces/      # External data interfaces
├── tests/               # Test suite
│   ├── test_element.py
│   ├── test_isotope.py
│   ├── test_ion.py
│   ├── test_fetch.py
│   ├── test_vis.py
│   └── test_econf/
├── docs/                # Sphinx documentation
│   ├── source/          # Documentation source files
│   │   ├── conf.py      # Sphinx configuration
│   │   ├── notebooks/   # Jupyter notebook tutorials
│   │   └── api/         # API documentation
│   ├── Makefile         # Documentation build commands
│   └── build/           # Generated documentation
├── notebooks/           # Development notebooks (not in docs)
├── alembic/             # Database migration scripts
│   └── versions/
├── tasks.py             # Invoke task definitions
├── pyproject.toml       # Poetry configuration and dependencies
└── CONTRIBUTING.md      # Contribution guidelines
```

## Development Setup

### Prerequisites
- Python 3.9 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- Git

### Initial Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/lmmentel/mendeleev.git
   cd mendeleev
   ```

2. **Install dependencies**
   ```bash
   # Install core dependencies
   poetry install

   # Install with visualization dependencies
   poetry install --with vis
   ```

3. **Activate the virtual environment**
   ```bash
   poetry shell
   ```

## Running Tests

### Basic Test Execution

```bash
# Run all tests
poetry run pytest

# Run tests with coverage report
poetry run pytest --cov=mendeleev

# Run tests in parallel (using pytest-xdist)
poetry run pytest -n auto

# Run tests with duration reporting (slowest 10 tests)
poetry run pytest --durations=10
```

### Run Specific Tests

```bash
# Run tests in a specific file
poetry run pytest tests/test_element.py

# Run a specific test function
poetry run pytest tests/test_element.py::test_function_name

# Run tests matching a pattern
poetry run pytest -k "element"
```

### Test Configuration

Tests are configured in `pyproject.toml`:
```toml
[tool.pytest.ini_options]
minversion = "8.0"
addopts = "--durations=10 -n auto"
```

## Building Documentation

### Prerequisites

Documentation requires additional dependencies beyond the core package:

```bash
# Install documentation dependencies (one-time setup)
poetry run pip install -r docs/requirements.txt
```

Required packages include:
- sphinx, nbsphinx (documentation generator)
- sphinx-material (documentation theme)
- myst-parser (Markdown support)
- sphinxcontrib-bibtex (bibliography)
- bokeh, plotly, seaborn (for visualization examples)
- ipython, ipykernel (for notebook examples)

### Local Documentation Build

**Prerequisites:**

First, install documentation dependencies (one-time setup):
```bash
poetry run pip install -r docs/requirements.txt
```

This includes:
- `sphinx` - Documentation builder
- `sphinx-material` - Material theme
- `sphinx-design` - Grid and card layouts for modern UI
- `nbsphinx` - Jupyter notebook support
- `sphinxcontrib-bibtex` - Bibliography support
- `myst-parser` - Markdown support
- Visualization libraries (bokeh, plotly, seaborn)

**Building the Docs:**

```bash
# Navigate to docs directory
cd docs

# Build HTML documentation using poetry
poetry run make html

# View the documentation
# Open docs/build/html/index.html in your browser
```

**Important Notes:**
- Always use `poetry run make html` (not just `make html`)
- First build may take longer as it processes all notebooks
- Build produces warnings (572 warnings is normal)
- Successfully built docs show: "build succeeded, 572 warnings"

### Other Documentation Formats

```bash
# Build as single HTML page
poetry run make singlehtml

# Build PDF (requires LaTeX)
poetry run make latexpdf

# Check for broken links
poetry run make linkcheck

# Clean build artifacts
poetry run make clean
```

### Rendering Data Documentation

After updating the `PropertyMetadata` model, regenerate the data documentation:

```bash
# From project root
poetry run inv render-data-docs

# Then rebuild docs
cd docs && poetry run make html
```

### Documentation Build Troubleshooting

**Issue: "sphinx-build command not found"**
```bash
# Install doc dependencies
poetry run pip install -r docs/requirements.txt
```

**Issue: "No module named 'myst_parser'"**
```bash
# Ensure all doc dependencies are installed
cd docs
poetry run pip install -r requirements.txt
```

**Issue: "Build failed with SQLAlchemy errors"**
- This should be fixed by the autodoc event handlers in `conf.py`
- If you see `NotImplementedError: <built-in function getitem>`, the skip_hybrid_properties handler may need updating

**Issue: "WARNING: duplicate object description"**
- These are cosmetic warnings from autosummary
- They don't prevent documentation from building
- Safe to ignore

### Documentation Structure

The documentation includes:
- **Overview & Installation**: Getting started guides
- **Tutorials**: Jupyter notebook tutorials covering key features
- **Data Reference**: Complete property listings with units and citations
- **Data Access**: How to fetch and query data
- **Units**: Working with physical units (pint integration)
- **Electronegativity**: Comprehensive guide to 15+ electronegativity scales
- **FAQ**: Frequently asked questions
- **Troubleshooting**: Common issues and solutions
- **API Overview**: Architecture, patterns, and decision guide
- **API Reference**: Complete API documentation
- **Contributing Guide**: How to contribute to the project

## Database Management

The project uses SQLAlchemy with SQLite (`mendeleev/elements.db`) for data storage.

### Creating Database Migrations

When adding new models or modifying existing ones:

```bash
# Create a new migration
alembic revision -m "Description of changes"

# Apply migrations
alembic upgrade head

# Check migration status
alembic current

# Compare databases (against master branch)
inv sqldiff
```

## Invoke Tasks

The project includes custom invoke tasks defined in `tasks.py`:

```bash
# Export data to multiple formats (csv, json, html, markdown, sql)
inv export

# Render data documentation from PropertyMetadata
inv render-data-docs

# Compare database with master branch
inv sqldiff

# Time import performance
inv timeimport
```

## Code Quality

### Pre-commit Hooks

The project uses pre-commit hooks for code quality:

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually on all files
pre-commit run --all-files

# Run specific hook
pre-commit run ruff --all-files
```

### Linting and Formatting

The project uses **ruff** for both linting and formatting (configured via pre-commit).

## Common Development Tasks

### Adding a New Element Property

1. Update the data model in `mendeleev/models.py`
2. Create an alembic migration: `alembic revision -m "Add property X"`
3. Implement migration logic in `alembic/versions/`
4. Apply migration: `alembic upgrade head`
5. Update `PropertyMetadata` table if needed
6. Regenerate data docs: `inv render-data-docs`
7. Add tests in appropriate test file
8. Run tests: `poetry run pytest`

### Working with the CLI

The package provides a command-line tool:

```bash
# Get element information by symbol
element.py Si

# Get element by atomic number
element.py 14

# Get element by name
element.py Silicon
```

## CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/main.yml`):
- **Runs on**: Ubuntu, macOS, Windows
- **Python versions**: 3.9, 3.10, 3.11, 3.12, 3.13
- **Steps**:
  1. Install dependencies with Poetry
  2. Run pre-commit hooks (ruff linting)
  3. Run pytest with coverage
  4. Publish to PyPI on tagged releases

## Key Data Models

The project uses SQLAlchemy models (`mendeleev/models.py`):

- **Element**: Main element properties and attributes
- **Isotope**: Isotope-specific data
- **Ion**: Ionic species data
- **IonicRadius**: Ionic radii for different oxidation states
- **IonizationEnergy**: Ionization energies
- **OxidationState**: Oxidation states
- **ScreeningConstant**: Nuclear screening constants
- **PropertyMetadata**: Metadata about element properties

## Important Files

- **pyproject.toml**: Poetry configuration, dependencies, and tool settings
- **tasks.py**: Invoke task definitions for common operations
- **docs/source/conf.py**: Sphinx documentation configuration
- **mendeleev/elements.db**: SQLite database with all element data
- **.github/workflows/main.yml**: CI/CD pipeline configuration
- **CONTRIBUTING.md**: Detailed contribution guidelines

## Testing Strategy

The test suite covers:
- Element property access and validation
- Isotope data and calculations
- Ion charge states and properties
- Electronic configuration parsing
- Database queries and fetching
- Visualization functions
- CLI functionality

## Useful Commands Summary

```bash
# Setup
poetry install --with vis

# Testing
poetry run pytest --cov=mendeleev

# Documentation
cd docs && make html

# Code quality
pre-commit run --all-files

# Database
alembic upgrade head

# Tasks
inv render-data-docs
inv export
```

## Resources

- **Main Documentation**: https://mendeleev.readthedocs.io
- **Interactive Tutorials**: Available as Jupyter notebooks on Binder
- **API Reference**: https://mendeleev.readthedocs.io/en/stable/api/api.html
- **Data Sources**: https://github.com/lmmentel/mendeleev-data
- **Issues**: https://github.com/lmmentel/mendeleev/issues
- **Discussions**: https://github.com/lmmentel/mendeleev/discussions

## Notes for Claude Code

- The database file `mendeleev/elements.db` is the core data store - handle with care
- When modifying models, always create alembic migrations
- Documentation notebooks in `docs/source/notebooks/` are part of the documentation
- Development notebooks in root `notebooks/` are for experimentation
- The project follows semantic versioning (currently v1.1.0)
- All property metadata should include units, descriptions, and citations
- Tests should pass on all supported Python versions (3.9-3.13)
- Pre-commit hooks must pass before committing
