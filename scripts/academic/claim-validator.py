#!/usr/bin/env python3
"""
COSMOS - Scientific Claim Validator
Validates scientific claims against available evidence and established criteria
"""

import argparse
import json
from typing import Dict, List, Tuple
from enum import Enum


class ValidationLevel(Enum):
    """Validation levels for scientific claims."""
    VERIFIED = "Verified"
    PROBABLE = "Probable"
    PLAUSIBLE = "Plausible"
    SPECULATIVE = "Speculative"
    UNSUBSTANTIATED = "Unsubstantiated"
    REFUTED = "Refuted"


class ClaimValidator:
    """Validator for scientific claims in COSMOS framework."""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.validation_criteria = {
            'empirical_evidence': 0.4,
            'theoretical_foundation': 0.3,
            'peer_review': 0.2,
            'reproducibility': 0.1
        }
    
    def log(self, message: str):
        if self.verbose:
            print(f"[DEBUG] {message}")
    
    def validate_claim(
        self,
        claim: str,
        evidence: Dict[str, any]
    ) -> Tuple[ValidationLevel, float, Dict]:
        """
        Validate a scientific claim.
        
        Args:
            claim: The claim to validate
            evidence: Dictionary of available evidence
            
        Returns:
            Tuple of (validation_level, confidence_score, details)
        """
        self.log(f"Validating claim: {claim}")
        
        score = 0.0
        details = {}
        
        # Check empirical evidence
        if evidence.get('empirical_data'):
            data_quality = evidence['empirical_data'].get('quality', 0)
            score += self.validation_criteria['empirical_evidence'] * data_quality
            details['empirical_evidence'] = {
                'present': True,
                'quality': data_quality,
                'contribution': self.validation_criteria['empirical_evidence'] * data_quality
            }
        else:
            details['empirical_evidence'] = {'present': False, 'contribution': 0}
        
        # Check theoretical foundation
        if evidence.get('theory'):
            theory_strength = evidence['theory'].get('strength', 0)
            score += self.validation_criteria['theoretical_foundation'] * theory_strength
            details['theoretical_foundation'] = {
                'present': True,
                'strength': theory_strength,
                'contribution': self.validation_criteria['theoretical_foundation'] * theory_strength
            }
        else:
            details['theoretical_foundation'] = {'present': False, 'contribution': 0}
        
        # Check peer review
        if evidence.get('peer_reviewed'):
            review_quality = evidence['peer_reviewed'].get('quality', 0)
            score += self.validation_criteria['peer_review'] * review_quality
            details['peer_review'] = {
                'present': True,
                'quality': review_quality,
                'contribution': self.validation_criteria['peer_review'] * review_quality
            }
        else:
            details['peer_review'] = {'present': False, 'contribution': 0}
        
        # Check reproducibility
        if evidence.get('reproducibility'):
            repro_rate = evidence['reproducibility'].get('success_rate', 0)
            score += self.validation_criteria['reproducibility'] * repro_rate
            details['reproducibility'] = {
                'present': True,
                'rate': repro_rate,
                'contribution': self.validation_criteria['reproducibility'] * repro_rate
            }
        else:
            details['reproducibility'] = {'present': False, 'contribution': 0}
        
        # Determine validation level
        if score >= 0.8:
            level = ValidationLevel.VERIFIED
        elif score >= 0.6:
            level = ValidationLevel.PROBABLE
        elif score >= 0.4:
            level = ValidationLevel.PLAUSIBLE
        elif score >= 0.2:
            level = ValidationLevel.SPECULATIVE
        else:
            level = ValidationLevel.UNSUBSTANTIATED
        
        return level, score, details
    
    def generate_report(
        self,
        claim: str,
        level: ValidationLevel,
        score: float,
        details: Dict
    ) -> str:
        """Generate validation report."""
        report = []
        report.append("\n" + "=" * 70)
        report.append("  SCIENTIFIC CLAIM VALIDATION REPORT")
        report.append("=" * 70)
        report.append(f"\nClaim: {claim}")
        report.append(f"\nValidation Level: {level.value}")
        report.append(f"Confidence Score: {score:.2%}")
        report.append("\n" + "-" * 70)
        report.append("\nEvidence Assessment:")
        
        for criterion, info in details.items():
            criterion_name = criterion.replace('_', ' ').title()
            if info['present']:
                report.append(f"\n  ✓ {criterion_name}:")
                for key, value in info.items():
                    if key != 'present':
                        report.append(f"      {key.title()}: {value:.2%}" if isinstance(value, float) else f"      {key.title()}: {value}")
            else:
                report.append(f"\n  ✗ {criterion_name}: Not available")
        
        report.append("\n" + "-" * 70)
        report.append("\nRecommendations:")
        
        if score < 0.4:
            report.append("  • Requires significant empirical validation")
            report.append("  • Develop stronger theoretical foundation")
            report.append("  • Seek peer review and expert validation")
        elif score < 0.6:
            report.append("  • Continue empirical testing")
            report.append("  • Expand reproducibility studies")
            report.append("  • Prepare for peer review submission")
        elif score < 0.8:
            report.append("  • Ready for peer review")
            report.append("  • Consider publication in academic journals")
            report.append("  • Expand validation to additional contexts")
        else:
            report.append("  • Strong validation achieved")
            report.append("  • Ready for publication and application")
            report.append("  • Consider patent protection if applicable")
        
        report.append("\n" + "=" * 70 + "\n")
        
        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description='COSMOS Scientific Claim Validator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example evidence JSON structure:
{
  "empirical_data": {"quality": 0.7},
  "theory": {"strength": 0.8},
  "peer_reviewed": {"quality": 0.0},
  "reproducibility": {"success_rate": 0.0}
}

Values should be between 0.0 and 1.0
        """
    )
    
    parser.add_argument(
        '--claim', '-c',
        required=True,
        help='Scientific claim to validate'
    )
    
    parser.add_argument(
        '--evidence', '-e',
        help='Path to evidence JSON file or JSON string'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Parse evidence
    evidence = {}
    if args.evidence:
        try:
            # Try to load as file
            with open(args.evidence, 'r') as f:
                evidence = json.load(f)
        except (FileNotFoundError, PermissionError) as e:
            try:
                # Try to parse as JSON string
                evidence = json.loads(args.evidence)
            except json.JSONDecodeError:
                print(f"Error: Could not parse evidence: {args.evidence}")
                return 1
    
    # Create validator
    validator = ClaimValidator(verbose=args.verbose)
    
    print("\n🔬 COSMOS Scientific Claim Validator")
    print("   Academic Validation Tool")
    print("   Rafael Melo Reis - RAFAELIA Project")
    
    # Validate claim
    level, score, details = validator.validate_claim(args.claim, evidence)
    
    # Generate and print report
    report = validator.generate_report(args.claim, level, score, details)
    print(report)
    
    # Return exit code based on validation level
    if level in [ValidationLevel.VERIFIED, ValidationLevel.PROBABLE]:
        return 0
    elif level == ValidationLevel.PLAUSIBLE:
        return 0
    else:
        return 1


if __name__ == '__main__':
    exit(main())
