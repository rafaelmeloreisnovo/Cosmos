#!/bin/bash
# COSMOS Master Script Runner
# Executes scripts from all categories with a unified interface

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

print_header() {
    echo -e "${MAGENTA}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${MAGENTA}  🌌 COSMOS Master Script Runner${NC}"
    echo -e "${MAGENTA}     Rafael Melo Reis - RAFAELIA Project${NC}"
    echo -e "${MAGENTA}═══════════════════════════════════════════════════════════${NC}"
    echo
}

show_menu() {
    echo -e "${CYAN}Available Categories:${NC}"
    echo
    echo "  1) Technologies    - Technology implementation scripts"
    echo "  2) Techniques      - Technique and methodology scripts"
    echo "  3) Professional    - Professional workflow scripts"
    echo "  4) Academic        - Academic research scripts"
    echo "  5) Formal          - Formal validation scripts"
    echo "  6) Fullstack       - Fullstack application scripts"
    echo
    echo "  7) Run All Tests   - Execute comprehensive test suite"
    echo "  8) View Documentation"
    echo "  0) Exit"
    echo
}

show_technology_scripts() {
    echo -e "${BLUE}Technology Scripts:${NC}"
    echo
    echo "  1) Fibonacci Calculator (Python)"
    echo "  2) Galaxy Pattern Analyzer (Bash)"
    echo "  3) ATOMIC_EX_LIGHT Simulator (Python)"
    echo "  0) Back to main menu"
    echo
}

show_technique_scripts() {
    echo -e "${BLUE}Technique Scripts:${NC}"
    echo
    echo "  1) Pattern Recognition (Python)"
    echo "  0) Back to main menu"
    echo
}

show_professional_scripts() {
    echo -e "${BLUE}Professional Scripts:${NC}"
    echo
    echo "  1) Business Metrics Calculator (Python)"
    echo "  0) Back to main menu"
    echo
}

show_academic_scripts() {
    echo -e "${BLUE}Academic Scripts:${NC}"
    echo
    echo "  1) Scientific Claim Validator (Python)"
    echo "  0) Back to main menu"
    echo
}

show_formal_scripts() {
    echo -e "${BLUE}Formal Scripts:${NC}"
    echo
    echo "  1) Formal Validator (Python)"
    echo "  0) Back to main menu"
    echo
}

show_fullstack_scripts() {
    echo -e "${BLUE}Fullstack Scripts:${NC}"
    echo
    echo "  1) Start API Server"
    echo "  2) Generate Frontend Visualizer"
    echo "  3) Initialize Database"
    echo "  4) Deploy All Services (Docker)"
    echo "  5) Run Integration Tests"
    echo "  0) Back to main menu"
    echo
}

run_script() {
    local script_path="$1"
    local script_args="${@:2}"
    
    echo -e "${GREEN}Running: $script_path${NC}"
    echo
    
    if [[ "$script_path" == *.py ]]; then
        python3 "$script_path" $script_args
    elif [[ "$script_path" == *.sh ]]; then
        bash "$script_path" $script_args
    else
        echo -e "${RED}Unknown script type${NC}"
        return 1
    fi
}

technology_menu() {
    while true; do
        show_technology_scripts
        read -p "Select script: " choice
        
        case $choice in
            1)
                run_script "$SCRIPT_DIR/technologies/01-fibonacci-calculator.py" --sequence 15 --compare
                ;;
            2)
                run_script "$SCRIPT_DIR/technologies/02-galaxy-pattern-analyzer.sh" --galaxy M81
                ;;
            3)
                run_script "$SCRIPT_DIR/technologies/03-atomic-ex-light-simulator.py" --mass 0.001 --verbose
                ;;
            0)
                return
                ;;
            *)
                echo -e "${RED}Invalid choice${NC}"
                ;;
        esac
        
        echo
        read -p "Press Enter to continue..."
        echo
    done
}

technique_menu() {
    while true; do
        show_technique_scripts
        read -p "Select script: " choice
        
        case $choice in
            1)
                echo "Enter comma-separated values (e.g., 1,1,2,3,5,8,13):"
                read data
                run_script "$SCRIPT_DIR/techniques/pattern-recognition.py" --input "$data" --verbose
                ;;
            0)
                return
                ;;
            *)
                echo -e "${RED}Invalid choice${NC}"
                ;;
        esac
        
        echo
        read -p "Press Enter to continue..."
        echo
    done
}

professional_menu() {
    while true; do
        show_professional_scripts
        read -p "Select script: " choice
        
        case $choice in
            1)
                run_script "$SCRIPT_DIR/professional/metrics-calculator.py" --innovation all
                ;;
            0)
                return
                ;;
            *)
                echo -e "${RED}Invalid choice${NC}"
                ;;
        esac
        
        echo
        read -p "Press Enter to continue..."
        echo
    done
}

academic_menu() {
    while true; do
        show_academic_scripts
        read -p "Select script: " choice
        
        case $choice in
            1)
                echo "Enter claim to validate:"
                read claim
                run_script "$SCRIPT_DIR/academic/claim-validator.py" --claim "$claim" --verbose
                ;;
            0)
                return
                ;;
            *)
                echo -e "${RED}Invalid choice${NC}"
                ;;
        esac
        
        echo
        read -p "Press Enter to continue..."
        echo
    done
}

formal_menu() {
    while true; do
        show_formal_scripts
        read -p "Select script: " choice
        
        case $choice in
            1)
                echo "Enter subject (e.g., atomic-ex-light, zipraf):"
                read subject
                echo "Select criteria (academic, technical, legal, business):"
                read criteria
                run_script "$SCRIPT_DIR/formal/formal-validator.py" --subject "$subject" --criteria "$criteria" --verbose
                ;;
            0)
                return
                ;;
            *)
                echo -e "${RED}Invalid choice${NC}"
                ;;
        esac
        
        echo
        read -p "Press Enter to continue..."
        echo
    done
}

fullstack_menu() {
    while true; do
        show_fullstack_scripts
        read -p "Select script: " choice
        
        case $choice in
            1)
                run_script "$SCRIPT_DIR/fullstack/backend/api-server.py"
                ;;
            2)
                run_script "$SCRIPT_DIR/fullstack/frontend/fibonacci-visualizer.sh"
                ;;
            3)
                echo "Database initialization requires PostgreSQL to be running."
                echo "Run: psql -U cosmos -d cosmos_db -f $SCRIPT_DIR/fullstack/database/init-schema.sql"
                ;;
            4)
                run_script "$SCRIPT_DIR/fullstack/deployment/deploy.sh" development
                ;;
            5)
                run_script "$SCRIPT_DIR/fullstack/integration/integration-tests.sh"
                ;;
            0)
                return
                ;;
            *)
                echo -e "${RED}Invalid choice${NC}"
                ;;
        esac
        
        echo
        read -p "Press Enter to continue..."
        echo
    done
}

run_all_tests() {
    echo -e "${YELLOW}Running comprehensive test suite...${NC}"
    echo
    
    echo "1. Testing Fibonacci Calculator..."
    python3 "$SCRIPT_DIR/technologies/01-fibonacci-calculator.py" --sequence 10
    
    echo
    echo "2. Testing Galaxy Analyzer..."
    bash "$SCRIPT_DIR/technologies/02-galaxy-pattern-analyzer.sh" --galaxy M81
    
    echo
    echo "3. Testing Pattern Recognition..."
    python3 "$SCRIPT_DIR/techniques/pattern-recognition.py" --input "1,1,2,3,5,8,13,21" --verbose
    
    echo
    echo -e "${GREEN}✓ All tests completed${NC}"
}

show_documentation() {
    clear
    echo -e "${CYAN}COSMOS Scripts Documentation${NC}"
    echo
    cat "$SCRIPT_DIR/README.md"
    echo
}

main() {
    clear
    print_header
    
    while true; do
        show_menu
        read -p "Select category: " choice
        
        case $choice in
            1)
                technology_menu
                ;;
            2)
                technique_menu
                ;;
            3)
                professional_menu
                ;;
            4)
                academic_menu
                ;;
            5)
                formal_menu
                ;;
            6)
                fullstack_menu
                ;;
            7)
                run_all_tests
                ;;
            8)
                show_documentation
                ;;
            0)
                echo
                echo -e "${GREEN}Thank you for using COSMOS scripts!${NC}"
                echo
                exit 0
                ;;
            *)
                echo -e "${RED}Invalid choice${NC}"
                ;;
        esac
        
        echo
        read -p "Press Enter to continue..."
        clear
        print_header
    done
}

main
