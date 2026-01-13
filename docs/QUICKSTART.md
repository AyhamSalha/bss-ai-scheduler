# Quick Start Guide

This guide will help you get the BSS KI-Agent running quickly.

## Prerequisites

- Python 3.11+ installed
- Git installed
- 4GB+ free disk space (for AI model)

## Installation (5 minutes)

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd team-14-personaleinsatzplanung-bss
```

### 2. Set Up Python Environment

**Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

*Note: This will download ~2.2GB TinyLlama model on first run*

### 4. Configure Environment (Optional)

```bash
cp .env.example .env
```

Edit `.env` if needed, but defaults work fine.

### 5. Start the Server

```bash
uvicorn backend.main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 6. Open the Frontend

Open `frontend/index.html` in your browser, or:

```bash
# Using Python's built-in server
cd frontend
python -m http.server 3000
```

Then visit: `http://localhost:3000`

## Usage

1. **Click the chat icon** in the bottom-right corner
2. **Type a command** like:
   - `"Plane mir Ayham am Dienstag ein"`
   - `"Plane mir Mustafa am Montag ein"`
3. **See the result** in both chat and calendar

## Troubleshooting

### Server won't start
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000  # Windows
lsof -i :8000  # Mac/Linux
```

### AI model download is slow
- First run downloads 2.2GB model
- Subsequent runs use cached model
- Set `HF_HOME` in `.env` to change cache location

### Import errors
```bash
# Ensure virtual environment is activated
# You should see (.venv) in your terminal prompt

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Database errors
```bash
# Delete and recreate database
rm chat.db
# Server will recreate it on next start
```

## Docker Alternative (Advanced)

For a one-command setup:

```bash
docker-compose up -d
```

Access at:
- Frontend: http://localhost
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

## Next Steps

- Explore API docs at `http://localhost:8000/docs`
- Check out [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Read [README.md](README.md) for full documentation

## Need Help?

- Check the [Issues](../../issues) page
- Contact the team (see README.md)
