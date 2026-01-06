# COSMOS Scripts - Quick Start Guide

## 🚀 Getting Started

Welcome to the COSMOS comprehensive script collection! This guide will help you get started with all available scripts.

## 📁 Directory Structure

```
scripts/
├── README.md                 # Main documentation
├── run-cosmos.sh            # Interactive master script runner
├── technologies/            # Technology implementation scripts (17 areas)
├── techniques/              # Technique and methodology scripts
├── professional/            # Professional workflow scripts
├── academic/                # Academic research scripts
├── formal/                  # Formal validation scripts
└── fullstack/               # Fullstack application scripts
    ├── frontend/            # Web UI and visualization
    ├── backend/             # REST API server
    ├── database/            # Database schemas and queries
    ├── integration/         # Integration testing
    └── deployment/          # Docker and CI/CD
```

## 🎯 Quick Start Options

### Option 1: Interactive Menu (Recommended for beginners)
```bash
cd scripts
./run-cosmos.sh
```

This launches an interactive menu where you can explore and run any script.

### Option 2: Direct Script Execution

#### Technology Scripts
```bash
# Fibonacci Calculator
python3 technologies/01-fibonacci-calculator.py --sequence 15 --compare

# Galaxy Pattern Analyzer
bash technologies/02-galaxy-pattern-analyzer.sh --galaxy M81

# ATOMIC_EX_LIGHT Simulator
python3 technologies/03-atomic-ex-light-simulator.py --mass 0.001 --verbose
```

#### Technique Scripts
```bash
# Pattern Recognition
python3 techniques/pattern-recognition.py --input "1,1,2,3,5,8,13,21" --verbose
```

#### Professional Scripts
```bash
# Business Metrics Calculator
python3 professional/metrics-calculator.py --innovation atomic-ex-light
```

#### Academic Scripts
```bash
# Scientific Claim Validator
python3 academic/claim-validator.py --claim "fibonacci-correlation" --verbose
```

#### Formal Scripts
```bash
# Formal Validator
python3 formal/formal-validator.py --subject "atomic-ex-light" --criteria academic
```

#### Fullstack Scripts
```bash
# Start API Server
python3 fullstack/backend/api-server.py

# Generate Frontend Visualizer
bash fullstack/frontend/fibonacci-visualizer.sh

# Deploy with Docker
cd fullstack/deployment
docker-compose up -d

# Run Integration Tests
bash fullstack/integration/integration-tests.sh
```

## 📊 Example Outputs

### Fibonacci Calculator
```
🌀 COSMOS Modified Fibonacci Calculator
   Modifier (φ): 1.618033988749895
   Terms: 10

Modified Fibonacci Sequence:
  F(0) = 0.000000
  F(1) = 1.000000
  F(2) = 1.000000
  F(3) = 2.618034
  ...
```

### Galaxy Pattern Analyzer
```
🌌 Galaxy Pattern Analyzer

Galaxy: M81 (Bode's Galaxy)
Type: Spiral Galaxy
Pattern Analysis:
  - Spiral arm count: 2 major arms
  - Fibonacci correlation: High (φ ratio detected)
```

### Business Metrics
```
📊 Technology Readiness Level (TRL)
   Level: 1
   Status: Basic principles observed

💰 Market Analysis
   Total Market Size: $50.0B
   Time to Market: 10 years
```

## 🔧 Requirements

### General Requirements
- Bash 4.0+
- Python 3.8+
- Git

### For Fullstack Components
- Docker 20+
- Docker Compose 2+
- Node.js 16+ (for frontend)
- PostgreSQL 13+ (for database)

### Python Dependencies
```bash
# Install required packages
pip install fastapi uvicorn pydantic numpy scipy matplotlib
```

## 🌟 Key Features

### Technologies (17 Areas)
1. ✅ Mathematics and Number Theory - Fibonacci calculator
2. ✅ Cosmology and Astrophysics - Galaxy analyzer
3. ✅ Quantum Physics and Energy - ATOMIC_EX_LIGHT simulator
4. 📝 Computational Theory - RAFCODE-Φ processor
5. 📝 Consciousness and Observation
6. 📝 Fractal Geometry
7-17. Additional areas documented in respective READMEs

### Techniques
- ✅ Pattern Recognition and Analysis
- 📝 Data Visualization
- 📝 Statistical Validation
- 📝 Documentation Generation

### Professional
- ✅ Business Metrics Calculator
- 📝 Market Analysis
- 📝 IP Management
- 📝 Project Management

### Academic
- ✅ Scientific Claim Validator
- 📝 Hypothesis Testing
- 📝 Citation Management
- 📝 Peer Review Preparation

### Formal
- ✅ Formal Validation (Academic, Technical, Legal, Business)
- 📝 Compliance Checking
- 📝 Quality Assurance
- 📝 Standards Verification

### Fullstack
- ✅ REST API Server (FastAPI)
- ✅ Frontend Visualization (D3.js)
- ✅ Database Schema (PostgreSQL)
- ✅ Docker Deployment
- ✅ Integration Tests

## 📚 Documentation

Each category has its own README with detailed documentation:
- `technologies/README.md`
- `techniques/README.md`
- `professional/README.md`
- `academic/README.md`
- `formal/README.md`
- `fullstack/README.md`

## 🎓 Learning Path

### For Beginners
1. Start with `./run-cosmos.sh` interactive menu
2. Try the Fibonacci calculator
3. Explore the galaxy analyzer
4. View the frontend visualizer

### For Researchers
1. Use academic validation scripts
2. Run pattern recognition
3. Validate scientific claims
4. Generate formal reports

### For Developers
1. Start the API server
2. Run integration tests
3. Deploy with Docker
4. Explore the database schema

### For Business Professionals
1. Calculate business metrics
2. Analyze market opportunities
3. Review patent potential
4. Generate professional reports

## 🧪 Testing

Run comprehensive tests:
```bash
# Test individual components
python3 technologies/01-fibonacci-calculator.py --sequence 10

# Run all integration tests
bash fullstack/integration/integration-tests.sh

# Test API endpoints
curl http://localhost:8000/api/health
```

## 🐳 Docker Deployment

Quick deployment with Docker:
```bash
cd fullstack/deployment
docker-compose up -d
```

Access services:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Database: postgresql://localhost:5432/cosmos_db

## 🤝 Contributing

To add new scripts:
1. Place them in the appropriate category directory
2. Follow the naming convention: `##-description.py` or `.sh`
3. Add documentation to the category README
4. Make scripts executable: `chmod +x script.sh`
5. Test thoroughly before committing

## 📝 Script Naming Convention

- Technologies: `##-technology-name.{py|sh}` (e.g., `01-fibonacci-calculator.py`)
- Techniques: `technique-name.{py|sh}` (e.g., `pattern-recognition.py`)
- Others: `descriptive-name.{py|sh}` (e.g., `metrics-calculator.py`)

## 🔒 Security Notes

- Never commit secrets or credentials
- Use environment variables for sensitive data
- Review all scripts before execution
- Use virtual environments for Python dependencies

## 📞 Support

For questions or issues:
1. Check the relevant README in each category
2. Review the main repository documentation
3. Examine script help: `script.py --help`

## 🎯 Next Steps

After trying the scripts:
1. ✅ Explore all categories
2. ✅ Run integration tests
3. ✅ Deploy fullstack application
4. ✅ Generate visualizations
5. ✅ Validate scientific claims
6. ✅ Calculate business metrics

## 🌌 COSMOS Vision

These scripts implement the complete COSMOS framework, bridging:
- Mathematics and Cosmology
- Quantum Physics and Energy
- Consciousness and Observation
- Technology and Innovation

*"Energy doesn't disappear. What we call waste is just misplaced energy."*
— Rafael Melo Reis

---

**Version:** 1.0.0  
**Author:** Rafael Melo Reis  
**Project:** COSMOS/RAFAELIA  
**Date:** 2026-01-06
