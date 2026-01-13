# Contributing to BSS KI-Agent

Thank you for considering contributing to the BSS KI-Agent project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Bugs

- Use the issue tracker
- Describe the bug in detail
- Include steps to reproduce
- Mention your environment (OS, Python version, etc.)

### Suggesting Features

- Open an issue with the "enhancement" label
- Clearly describe the feature and its benefits
- Provide examples if possible

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
   - Follow the code style (Black for Python, Prettier for JS)
   - Add tests for new features
   - Update documentation as needed
4. **Run tests**
   ```bash
   pytest tests/
   ```
5. **Format code**
   ```bash
   black backend/
   ```
6. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
7. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```
8. **Open a Pull Request**

## Code Style

### Python
- Follow PEP 8
- Use Black formatter (line length: 100)
- Add docstrings to functions and classes
- Type hints are encouraged

### JavaScript
- Use Prettier for formatting
- Use meaningful variable names
- Add comments for complex logic

## Testing

- Write unit tests for new features
- Maintain or improve code coverage
- Test both success and error cases

## Commit Messages

- Use clear and descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove, etc.)
- Keep the first line under 50 characters
- Add detailed description if needed

Example:
```
Add user authentication feature

- Implement JWT-based authentication
- Add login/logout endpoints
- Update tests
```

## Questions?

Feel free to open an issue for any questions or concerns!
