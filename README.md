# 📅 BSS KI-Agent - AI-Powered Staff Scheduling System

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> 🤖 Intelligent personnel planning assistant with natural language processing and privacy-first local AI

An intelligent staff scheduling system that combines the power of local AI (TinyLlama) with an intuitive chat interface and interactive calendar. Built with privacy in mind - all data stays on your machine.

---

## 📖 About This Project

Developed as a client project for **BSS GmbH** during the Summer Semester 2025 Software Engineering course, this AI-powered scheduling system addresses real-world staff planning challenges in small to medium businesses. The project demonstrates practical application of local LLM technology for natural language workforce management, combining modern web technologies with privacy-conscious AI to create an accessible solution for non-technical users.

**Team:** Koutaibe Alhassan, Gürhan Arabaci, Ayham Salha

---

## ✨ Highlights

- 🤖 **Local AI Processing** - TinyLlama for natural language understanding (no cloud required)
- 💬 **Chat-Based Interface** - Schedule staff with simple commands like "Schedule Ayham on Tuesday"
- 📊 **Interactive Calendar** - Visual planning with drag-and-drop functionality
- 🔒 **Privacy-First** - Complete local operation, no data leaves your system
- 🚀 **Modern Stack** - FastAPI backend, responsive frontend
- 🐳 **Docker Ready** - One-command deployment with Docker Compose
- 🧪 **Well-Tested** - Comprehensive unit tests with pytest

---

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd team-14-personaleinsatzplanung-bss

# Start with Docker Compose
docker-compose up -d

# Access the application
# Frontend: http://localhost
# API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Manual Setup

```bash
# Clone and navigate
git clone <your-repo-url>
cd team-14-personaleinsatzplanung-bss

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Start the server
uvicorn backend.main:app --reload

# Access the application
# Open http://localhost:8000 in your browser
```

---

## 📖 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Development](#-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Features

### Core Functionality
- ✅ **Natural Language Planning** - "Schedule Mustafa on Monday" → Automatic calendar entry
- ✅ **Chat History** - Complete conversation tracking and retrieval
- ✅ **Availability Management** - Click-to-set availability in calendar
- ✅ **Interactive Calendar** - Visual representation of schedules and availability
- ✅ **Error Handling** - Graceful degradation with user-friendly messages
- ✅ **Health Monitoring** - Built-in health check endpoints

### Technical Features
- ✅ **RESTful API** - Clean, documented API with OpenAPI/Swagger
- ✅ **Environment Configuration** - Flexible config via environment variables
- ✅ **Logging** - Comprehensive application logging
- ✅ **Docker Support** - Full containerization with Docker Compose
- ✅ **CI/CD Ready** - GitHub Actions workflow included
- ✅ **Code Quality** - Linting and formatting with Black & Pylint

---

## 🏗 Architecture

```
┌─────────────────┐     HTTP/REST      ┌──────────────────┐
│                 │ ◄─────────────────► │                  │
│   Frontend      │                     │   FastAPI        │
│   (HTML/CSS/JS) │                     │   Backend        │
│                 │                     │                  │
└─────────────────┘                     └────────┬─────────┘
                                                 │
                                                 │
                                        ┌────────▼─────────┐
                                        │                  │
                                        │   TinyLlama      │
                                        │   LLM Model      │
                                        │                  │
                                        └────────┬─────────┘
                                                 │
                                        ┌────────▼─────────┐
                                        │                  │
                                        │   SQLite         │
                                        │   Database       │
                                        │                  │
                                        └──────────────────┘
```

### Components

- **Frontend**: Vanilla JavaScript with interactive calendar and chat UI
- **Backend**: FastAPI Python server with async endpoints
- **AI Layer**: TinyLlama 1.1B for natural language processing
- **Database**: SQLite for local data persistence
- **Deployment**: Docker containers with Nginx reverse proxy

---

## 🛠 Technology Stack

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- [PyTorch](https://pytorch.org/) - Deep learning framework
- [Transformers](https://huggingface.co/transformers/) - HuggingFace library
- [SQLite](https://www.sqlite.org/) - Embedded database

**Frontend**
- HTML5, CSS3, JavaScript (ES6+)
- Fetch API for HTTP requests
- Responsive design

**AI/ML**
- [TinyLlama-1.1B-Chat](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) - Local language model
- Regex-based command parsing
- Natural language understanding

**DevOps**
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Nginx (Production proxy)

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- Git
- Docker (optional, for containerized deployment)

### Detailed Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd team-14-personaleinsatzplanung-bss
   ```

2. **Set up Python environment**
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate it
   # Windows:
   .venv\Scripts\activate
   # Unix/Mac:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   # Copy example environment file
   cp .env.example .env
   
   # Edit .env with your settings (optional)
   ```

5. **Run the application**
   ```bash
   # Start the backend server
   uvicorn backend.main:app --reload
   
   # The server will start at http://localhost:8000
   # API documentation at http://localhost:8000/docs
   ```

6. **Access the application**
   - Open http://localhost:8000 in your web browser
   - The server automatically serves the frontend

---

## 💻 Usage

### Chat Interface

1. Click the chat toggle button to open the chat interface
2. Type natural language commands:
   - `"Schedule Ayham on Tuesday"` - Schedule Ayham on Tuesday
   - `"Schedule Mustafa on Monday"` - Schedule Mustafa on Monday
   - `"Plane mir Sarah am Freitag ein"` - Schedule Sarah on Friday (German)
3. The AI processes your request and creates a calendar entry
4. View the entry in the interactive calendar

### Calendar Management

- **View Schedule**: See all scheduled entries in the current month's calendar
- **Set Availability**: Click on calendar days to add entries manually
- **Edit Entries**: Click on existing entries to modify them
- **Visual Feedback**: Color-coded entries for different availability states
- **Dynamic Calendar**: Automatically shows the current month and year

### API Usage

Access the interactive API documentation at `http://localhost:8000/docs`

**Example API Calls:**

```bash
# Health check
curl http://localhost:8000/health

# Send chat message
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"benutzer": "User", "nachricht": "Plane mir Ayham am Dienstag ein"}'

# Get chat history
curl http://localhost:8000/history?limit=10
```

---

## 📚 API Documentation

### Endpoints

#### `GET /`
Health check endpoint
```json
{
  "message": "KI-Agent läuft",
  "version": "1.0.0",
  "status": "healthy"
}
```

#### `GET /health`
Detailed health check with database status

#### `POST /chat`
Process chat message with AI
```json
// Request
{
  "benutzer": "User",
  "nachricht": "Plane mir Ayham am Dienstag ein"
}

// Response
{
  "response": "Ayham wurde am 2026-01-14 eingeplant.",
  "eintrag": {
    "title": "Geplant (via KI)",
    "datum": "2026-01-14",
    "uhrzeit": "09:00–17:00",
    "mitarbeiter": "Ayham",
    "verfuegbar": "Ja"
  }
}
```

#### `GET /history`
Get chat history (optional `limit` parameter)

Full interactive API docs available at `/docs` when running the server.

---

## 🔧 Development

### Project Structure

```
team-14-personaleinsatzplanung-bss/
├── backend/
│   ├── config.py              # Configuration management
│   ├── main.py                # FastAPI application
│   ├── llm_utils.py           # LLM integration
│   ├── llm_command_parser.py  # Command parsing
│   └── schemas.py             # Pydantic models
├── frontend/
│   ├── index.html             # Main UI
│   ├── script.js              # Frontend logic
│   ├── style.css              # Styling
│   └── image/                 # Assets
├── tests/
│   ├── test_api.py            # API tests
│   └── test_parser.py         # Parser tests
├── .github/
│   └── workflows/
│       └── ci.yml             # CI/CD pipeline
├── Dockerfile                 # Container definition
├── docker-compose.yml         # Multi-container setup
├── requirements.txt           # Python dependencies
├── .env.example               # Environment template
└── README.md                  # This file
```

### Code Formatting

```bash
# Format Python code with Black
black backend/

# Lint Python code
pylint backend/

# Format JavaScript/CSS
prettier --write frontend/
```

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=backend tests/

# Run specific test file
pytest tests/test_api.py -v

# Run tests in Docker
docker-compose run backend pytest
```

---

## 🚢 Deployment

### Docker Deployment

```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

### Production Considerations

- Set `DEBUG=False` in `.env`
- Configure proper CORS origins
- Use a reverse proxy (Nginx included in docker-compose)
- Set up SSL/TLS certificates
- Configure proper logging and monitoring
- Backup SQLite database regularly

---

## 🤝 Contributing

We welcome contributions! Please see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for details.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and formatting
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

- Ayham Salha - [Ayham.Salha@Student.HTW-Berlin.de](mailto:Ayham.Salha@Student.HTW-Berlin.de)
- Gürhan Arabaci - [Guerhan.Arabaci@Student.HTW-Berlin.de](mailto:Guerhan.Arabaci@Student.HTW-Berlin.de)
- Koutaibe Alhassan - [Koutaibe.Alhassan@Student.HTW-Berlin.de](mailto:Koutaibe.Alhassan@Student.HTW-Berlin.de)

---

## 🙏 Acknowledgments

- Developed as part of Software Development Project course
- TinyLlama model by HuggingFace
- FastAPI framework team
- HTW Berlin

---

## 📈 Roadmap

- [ ] User authentication & authorization
- [ ] Multi-tenant support
- [ ] Email notifications
- [ ] Calendar export (PDF/ICS)
- [ ] Mobile app (PWA)
- [ ] Advanced AI features (conflict detection, recommendations)
- [ ] Integration with external calendars (Google, Outlook)

---

**Made with ❤️ at HTW Berlin**
