# Deployment Scripts

Deployment, CI/CD, and infrastructure scripts for COSMOS framework.

## Available Scripts

### Docker
- `Dockerfile.frontend` - Frontend container
- `Dockerfile.backend` - Backend container
- `docker-compose.yml` - Multi-container orchestration

### CI/CD
- `github-actions-ci.yml` - GitHub Actions workflow
- `deploy.sh` - Automated deployment script
- `rollback.sh` - Rollback to previous version

### Cloud Deployment
- `deploy-aws.sh` - AWS deployment
- `deploy-azure.sh` - Azure deployment
- `deploy-gcp.sh` - Google Cloud deployment

### Monitoring
- `setup-monitoring.sh` - Setup monitoring stack
- `health-check.sh` - Health check script
- `log-aggregation.sh` - Log aggregation setup

## Quick Start

### Docker Deployment
```bash
# Build all containers
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Deployment
```bash
# Deploy to production
./deploy.sh production

# Check status
./health-check.sh

# Rollback if needed
./rollback.sh
```

## Requirements

- Docker 20+
- Docker Compose 2+
- Kubernetes (optional, for k8s deployment)
- Cloud CLI tools (AWS CLI, Azure CLI, or gcloud)

## Configuration

Environment variables in `.env`:
```
ENVIRONMENT=production
API_URL=https://api.cosmos.example.com
DATABASE_URL=postgresql://user:pass@host:5432/db
REDIS_URL=redis://localhost:6379
```

## Monitoring

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000
- Application logs: /var/log/cosmos/
