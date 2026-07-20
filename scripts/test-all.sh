#!/bin/bash
# Quick test of all main scripts

set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "🧪 Testing COSMOS Scripts"
echo "=========================="
echo

echo "1. Validating Cânone do Cosmos RAFAELIA..."
python3 formal/validate-cosmos-canon.py
echo

echo "2. Testing Fibonacci Calculator..."
python3 technologies/01-fibonacci-calculator.py --sequence 5
echo

echo "3. Testing Galaxy Analyzer..."
bash technologies/02-galaxy-pattern-analyzer.sh --galaxy IC342
echo

echo "4. Testing Business Metrics..."
python3 professional/metrics-calculator.py --innovation zipraf
echo

echo "✅ All core scripts tested successfully!"
