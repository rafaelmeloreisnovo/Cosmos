# Integration Scripts

End-to-end integration and testing scripts for COSMOS framework.

## Available Scripts

### Integration Testing
- `integration-tests.sh` - Run all integration tests
- `e2e-tests.py` - End-to-end testing suite
- `api-integration-test.py` - API integration tests

### Workflow Automation
- `full-workflow.sh` - Complete workflow from data to visualization
- `batch-processor.sh` - Batch processing workflows
- `pipeline-runner.py` - Data pipeline orchestration

### System Integration
- `health-check-all.sh` - Check health of all components
- `integration-monitor.py` - Monitor integration points
- `service-orchestrator.sh` - Orchestrate microservices

## Usage

```bash
# Run all integration tests
./integration-tests.sh

# Run end-to-end workflow
./full-workflow.sh --input data.csv --output results/

# Check system health
./health-check-all.sh

# Run specific integration test
python api-integration-test.py --test fibonacci
```

## Test Coverage

- Frontend ↔ Backend communication
- Backend ↔ Database queries
- API endpoint validation
- Data flow integrity
- Error handling and recovery
- Performance benchmarks

## Requirements

- All frontend, backend, and database services running
- pytest for Python tests
- curl for API testing
- jq for JSON processing

## CI/CD Integration

These scripts are integrated with GitHub Actions for automated testing on pull requests and deployments.
