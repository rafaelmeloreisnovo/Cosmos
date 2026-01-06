#!/bin/bash
# COSMOS Integration Tests
# End-to-end integration testing for all COSMOS components

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuration
API_BASE_URL="${API_BASE_URL:-http://localhost:8000}"
FRONTEND_URL="${FRONTEND_URL:-http://localhost:3000}"
TIMEOUT=30

# Test counters
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0

# Functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[PASS]${NC} $1"
}

log_error() {
    echo -e "${RED}[FAIL]${NC} $1"
}

print_header() {
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  🧪 COSMOS Integration Test Suite${NC}"
    echo -e "${BLUE}     Running comprehensive integration tests${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo
}

run_test() {
    local test_name="$1"
    shift
    local test_command=("$@")
    
    TESTS_RUN=$((TESTS_RUN + 1))
    
    echo -n "Running: $test_name... "
    
    if "${test_command[@]}" > /dev/null 2>&1; then
        log_success "PASSED"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        log_error "FAILED"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

test_api_health() {
    log_info "Testing API Health..."
    
    run_test "API Health Endpoint" \
        curl -f -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/health"
}

test_fibonacci_api() {
    log_info "Testing Fibonacci API..."
    
    run_test "Fibonacci Calculation (n=10)" \
        curl -f -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/fibonacci?n=10"
    
    run_test "Fibonacci with Custom Modifier" \
        curl -f -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/fibonacci?n=15&modifier=1.7"
}

test_galaxy_api() {
    log_info "Testing Galaxy Analysis API..."
    
    run_test "Galaxy Info - M81" \
        curl -f -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/galaxy/M81"
    
    run_test "Galaxy Info - IC342" \
        curl -f -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/galaxy/IC342"
    
    run_test "Galaxy Info - NGC628" \
        curl -f -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/galaxy/NGC628"
}

test_energy_api() {
    log_info "Testing Energy Simulation API..."
    
    local payload='{"mass_kg":0.001,"wavelength_nm":550,"duration_seconds":1}'
    
    run_test "Energy Simulation" \
        curl -f -s --max-time "$TIMEOUT" -X POST "${API_BASE_URL}/api/energy/simulate" \
         -H "Content-Type: application/json" \
         -d "$payload"
}

test_pattern_detection() {
    log_info "Testing Pattern Detection..."
    
    local data="1,1,2,3,5,8,13,21,34"
    
    run_test "Pattern Detection - Fibonacci" \
        curl -f -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/patterns/detect?data=${data}&pattern_type=fibonacci"
}

test_api_documentation() {
    log_info "Testing API Documentation..."
    
    run_test "OpenAPI Docs Available" \
        curl -f -s --max-time "$TIMEOUT" "${API_BASE_URL}/docs"
}

test_frontend_availability() {
    log_info "Testing Frontend Availability..."
    
    run_test "Frontend Home Page" \
        curl -f -s --max-time "$TIMEOUT" "${FRONTEND_URL}"
}

test_database_connectivity() {
    log_info "Testing Database Connectivity..."
    
    # This assumes the API has a database connection
    # If API health check passes and includes DB check, this is verified
    run_test "Database Connection via API" \
        curl -f -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/health"
}

test_error_handling() {
    log_info "Testing Error Handling..."
    
    # Test invalid galaxy name
    TESTS_RUN=$((TESTS_RUN + 1))
    echo -n "Running: Invalid Galaxy Name (404 Expected)... "
    if curl -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/galaxy/INVALID" | grep -q '404\|not found'; then
        log_success "PASSED"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        log_error "FAILED"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    
    # Test invalid fibonacci parameters
    TESTS_RUN=$((TESTS_RUN + 1))
    echo -n "Running: Invalid Fibonacci Parameters... "
    if curl -s --max-time "$TIMEOUT" "${API_BASE_URL}/api/fibonacci?n=-1" | grep -q '422\|error'; then
        log_success "PASSED"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        log_error "FAILED"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

test_performance() {
    log_info "Testing Performance..."
    
    local start_time=$(date +%s%N)
    curl -f -s --max-time $TIMEOUT "${API_BASE_URL}/api/fibonacci?n=20" > /dev/null
    local end_time=$(date +%s%N)
    local duration=$(( (end_time - start_time) / 1000000 ))
    
    if [ $duration -lt 1000 ]; then
        log_success "Response time: ${duration}ms (< 1000ms)"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        log_error "Response time: ${duration}ms (>= 1000ms)"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    TESTS_RUN=$((TESTS_RUN + 1))
}

print_summary() {
    echo
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  Test Summary${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo
    echo "  Total Tests Run:    $TESTS_RUN"
    echo -e "  ${GREEN}Tests Passed:${NC}       $TESTS_PASSED"
    echo -e "  ${RED}Tests Failed:${NC}       $TESTS_FAILED"
    
    if [ $TESTS_FAILED -eq 0 ]; then
        echo
        echo -e "${GREEN}✓ All integration tests passed! 🎉${NC}"
        echo
        return 0
    else
        echo
        echo -e "${RED}✗ Some integration tests failed${NC}"
        echo
        return 1
    fi
}

main() {
    print_header
    
    log_info "API Base URL: $API_BASE_URL"
    log_info "Frontend URL: $FRONTEND_URL"
    log_info "Timeout: ${TIMEOUT}s"
    echo
    
    # Check if services are running (with longer timeout for startup)
    local startup_timeout=10
    if ! curl -f -s --max-time "$startup_timeout" "${API_BASE_URL}/api/health" > /dev/null 2>&1; then
        log_error "API is not responding. Please ensure all services are running."
        echo "  Run: docker-compose up -d"
        echo "  Wait a few seconds for services to start, then try again."
        exit 1
    fi
    
    # Run all tests
    test_api_health
    test_fibonacci_api
    test_galaxy_api
    test_energy_api
    test_pattern_detection
    test_api_documentation
    test_frontend_availability
    test_database_connectivity
    test_error_handling
    test_performance
    
    # Print summary and exit with appropriate code
    print_summary
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --api-url)
            API_BASE_URL="$2"
            shift 2
            ;;
        --frontend-url)
            FRONTEND_URL="$2"
            shift 2
            ;;
        --timeout)
            TIMEOUT="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 [OPTIONS]"
            echo
            echo "OPTIONS:"
            echo "  --api-url URL         API base URL (default: http://localhost:8000)"
            echo "  --frontend-url URL    Frontend URL (default: http://localhost:3000)"
            echo "  --timeout SECONDS     Request timeout (default: 30)"
            echo "  -h, --help           Show this help"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

main
