# Project Structure

```
team-14-personaleinsatzplanung-bss/
│
├── README.md                      # Main documentation
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
├── .env.example                   # Environment variables template
├── requirements.txt               # Python dependencies
├── docker-compose.yml             # Multi-container orchestration
│
├── backend/                       # FastAPI application
│   ├── __init__.py
│   ├── main.py                   # FastAPI app entry point
│   ├── config.py                 # Configuration management
│   ├── schemas.py                # Pydantic models
│   ├── llm_utils.py              # LLM integration
│   └── command_parser.py         # NLP command parser
│
├── frontend/                      # Web interface
│   ├── index.html                # Main UI
│   ├── script.js                 # Frontend logic
│   ├── style.css                 # Styling
│   └── image/                    # Assets
│       └── Chat-Toggle-Icon.png
│
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── test_api.py               # API endpoint tests
│   └── test_parser.py            # Command parser tests
│
├── scripts/                       # Utility scripts
│   ├── clean_chat.py             # Clean database entries
│   └── show_chat.py              # Display chat history
│
├── docker/                        # Docker configuration
│   ├── Dockerfile                # Backend container
│   ├── .dockerignore             # Docker ignore rules
│   └── nginx.conf                # Nginx configuration
│
├── config/                        # Tool configurations
│   ├── pytest.ini                # Pytest settings
│   ├── pyproject.toml            # Black & Pylint config
│   └── .prettierrc               # Prettier config
│
├── docs/                          # Documentation
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   ├── CHANGELOG.md              # Version history
│   ├── QUICKSTART.md             # Quick start guide
│   ├── PORTFOLIO_IMPROVEMENTS.md # Enhancement summary
│   ├── REORGANIZATION_SUMMARY.md # Translation changes
│   └── FUNCTION_REFERENCE.md     # API reference
│
└── .github/                       # GitHub workflows
    └── workflows/
        └── ci.yml                # CI/CD pipeline
```

## Directory Descriptions

### `/backend`
Core FastAPI application with AI integration and business logic.

### `/frontend`
Vanilla JavaScript web interface with chat and calendar components.

### `/tests`
Comprehensive test suite using pytest for unit and integration tests.

### `/scripts`
Utility scripts for database management and maintenance.

### `/docker`
Docker containerization files for deployment.

### `/config`
Configuration files for development tools (testing, linting, formatting).

### `/docs`
Project documentation, guides, and references.

### `/.github`
GitHub Actions workflows for CI/CD automation.

## Root Files

- **README.md** - Main project documentation
- **LICENSE** - MIT license
- **.gitignore** - Git ignore patterns
- **.env.example** - Environment variable template
- **requirements.txt** - Python package dependencies
- **docker-compose.yml** - Docker multi-container setup

## Usage

All paths are now properly organized for:
- ✅ Easy navigation
- ✅ Clear separation of concerns
- ✅ Professional project structure
- ✅ Scalable architecture
