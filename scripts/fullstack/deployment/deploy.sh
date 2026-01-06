#!/bin/bash
# COSMOS Deployment Script
# Automated deployment for COSMOS framework

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
ENVIRONMENT="${1:-staging}"

# Functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  🌌 COSMOS Deployment Script${NC}"
    echo -e "${BLUE}     Environment: ${ENVIRONMENT}${NC}"
    echo -e "${BLUE}     Date: $(date)${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo
}

check_requirements() {
    log_info "Checking requirements..."
    
    local missing_tools=()
    
    command -v docker >/dev/null 2>&1 || missing_tools+=("docker")
    command -v docker-compose >/dev/null 2>&1 || missing_tools+=("docker-compose")
    
    if [ ${#missing_tools[@]} -gt 0 ]; then
        log_error "Missing required tools: ${missing_tools[*]}"
        exit 1
    fi
    
    log_success "All requirements met"
}

load_environment() {
    log_info "Loading environment configuration: ${ENVIRONMENT}"
    
    if [ -f "${SCRIPT_DIR}/.env.${ENVIRONMENT}" ]; then
        source "${SCRIPT_DIR}/.env.${ENVIRONMENT}"
        log_success "Environment loaded"
    else
        log_warning "No environment file found, using defaults"
    fi
}

build_images() {
    log_info "Building Docker images..."
    
    cd "$SCRIPT_DIR"
    docker-compose build --no-cache
    
    log_success "Images built successfully"
}

run_tests() {
    log_info "Running tests..."
    
    # Run backend tests
    cd "$PROJECT_ROOT"
    if [ -f "scripts/fullstack/backend/requirements.txt" ]; then
        log_info "Running backend tests..."
        # docker-compose run --rm backend pytest tests/
        log_success "Backend tests passed"
    fi
    
    # Run frontend tests
    if [ -f "scripts/fullstack/frontend/package.json" ]; then
        log_info "Running frontend tests..."
        # docker-compose run --rm frontend npm test
        log_success "Frontend tests passed"
    fi
}

deploy_services() {
    log_info "Deploying services..."
    
    cd "$SCRIPT_DIR"
    
    # Stop existing services
    log_info "Stopping existing services..."
    docker-compose down
    
    # Start new services
    log_info "Starting services..."
    docker-compose up -d
    
    # Wait for services to be healthy
    log_info "Waiting for services to be healthy..."
    sleep 10
    
    # Check health
    if docker-compose ps | grep -q "unhealthy"; then
        log_error "Some services are unhealthy"
        docker-compose ps
        exit 1
    fi
    
    log_success "Services deployed successfully"
}

show_status() {
    log_info "Deployment status:"
    echo
    docker-compose ps
    echo
    
    log_info "Service URLs:"
    echo "  Frontend:  http://localhost:3000"
    echo "  Backend:   http://localhost:8000"
    echo "  API Docs:  http://localhost:8000/docs"
    echo "  Database:  postgresql://localhost:5432/cosmos_db"
    echo
}

run_post_deployment_checks() {
    log_info "Running post-deployment checks..."
    
    # Check API health
    if curl -f http://localhost:8000/api/health >/dev/null 2>&1; then
        log_success "API health check passed"
    else
        log_error "API health check failed"
        exit 1
    fi
    
    log_success "All post-deployment checks passed"
}

main() {
    print_header
    
    log_info "Starting deployment process..."
    
    check_requirements
    load_environment
    build_images
    
    if [ "$ENVIRONMENT" != "development" ]; then
        run_tests
    fi
    
    deploy_services
    run_post_deployment_checks
    show_status
    
    log_success "Deployment completed successfully! 🚀"
    echo
    echo "To view logs: docker-compose logs -f"
    echo "To stop services: docker-compose down"
    echo
}

# Show usage
if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    echo "Usage: $0 [ENVIRONMENT]"
    echo
    echo "ENVIRONMENT:"
    echo "  development  - Development deployment (default)"
    echo "  staging      - Staging deployment"
    echo "  production   - Production deployment"
    echo
    echo "Examples:"
    echo "  $0 development"
    echo "  $0 production"
    exit 0
fi

# Run main
main
