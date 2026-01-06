# Backend Scripts

Backend API and processing scripts for COSMOS framework.

## Available Scripts

### API Services
- `api-server.py` - Main REST API server
- `fibonacci-api.py` - Fibonacci calculation API
- `galaxy-analysis-api.py` - Galaxy pattern analysis API
- `energy-simulator-api.py` - Energy conversion simulation API

### Data Processing
- `data-processor.py` - General data processing engine
- `pattern-analyzer.py` - Pattern analysis backend
- `calculation-engine.py` - Mathematical calculations

### Authentication
- `auth-service.py` - Authentication and authorization
- `token-manager.py` - JWT token management

## Technology

- FastAPI / Flask
- SQLAlchemy (ORM)
- Celery (async tasks)
- Redis (caching)

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Start API server
python api-server.py

# Run with auto-reload
uvicorn api-server:app --reload
```

## API Endpoints

- `GET /api/fibonacci?n=10&modifier=1.618` - Calculate Fibonacci
- `GET /api/galaxy/{name}` - Get galaxy analysis
- `POST /api/energy/simulate` - Simulate energy conversion
- `GET /api/health` - Health check

## Testing

```bash
pytest tests/
```
