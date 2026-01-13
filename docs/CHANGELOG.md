# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-13

### Added
- Docker and Docker Compose support for easy deployment
- Environment variable configuration with `.env` support
- Comprehensive error handling and logging
- Health check endpoints (`/health`)
- Chat history endpoint (`/history`)
- Unit tests for API endpoints and command parser
- CI/CD pipeline with GitHub Actions
- Code formatting with Black and Prettier
- Linting with Pylint
- API documentation with OpenAPI/Swagger
- Contributing guidelines (CONTRIBUTING.md)
- This changelog

### Changed
- Improved README with better structure
- Enhanced API responses with proper error messages
- Refactored backend to use configuration management
- Updated CORS middleware to support environment-based origins

### Fixed
- Database connection error handling
- Validation error responses
- Chat endpoint response format

## [0.1.0] - 2025-07-XX

### Added
- Initial release
- FastAPI backend with SQLite database
- TinyLlama LLM integration for natural language processing
- Interactive calendar interface
- Chat-based scheduling interface
- Local-only data storage for privacy
- Regex-based command parsing for scheduling
