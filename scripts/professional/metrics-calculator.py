#!/usr/bin/env python3
"""
COSMOS - Business Metrics Calculator
Calculates key business and technology metrics for COSMOS innovations
"""

import argparse
from typing import Dict, List
from enum import IntEnum


class TRL(IntEnum):
    """Technology Readiness Levels (1-9)."""
    BASIC_PRINCIPLES = 1
    CONCEPT_FORMULATED = 2
    PROOF_OF_CONCEPT = 3
    LABORATORY_VALIDATION = 4
    RELEVANT_ENVIRONMENT = 5
    DEMONSTRATION = 6
    PROTOTYPE_READY = 7
    SYSTEM_COMPLETE = 8
    OPERATIONAL = 9


class MetricsCalculator:
    """Calculate business and technology metrics for COSMOS projects."""
    
    def __init__(self):
        self.innovations = {
            'atomic-ex-light': {
                'name': 'ATOMIC_EX_LIGHT Energy Conversion',
                'trl': TRL.BASIC_PRINCIPLES,
                'patent_potential': 4,
                'market_size_b': 50,
                'development_cost_k': 500,
                'time_to_market_years': 10
            },
            'galaxy-analysis': {
                'name': 'Galaxy Pattern Recognition',
                'trl': TRL.CONCEPT_FORMULATED,
                'patent_potential': 6,
                'market_size_b': 0.1,
                'development_cost_k': 100,
                'time_to_market_years': 3
            },
            'zipraf': {
                'name': 'ZIPRAF/ZRF Compression',
                'trl': TRL.BASIC_PRINCIPLES,
                'patent_potential': 5,
                'market_size_b': 5,
                'development_cost_k': 150,
                'time_to_market_years': 4
            },
            'rafcode-phi': {
                'name': 'RAFCODE-Φ System',
                'trl': TRL.CONCEPT_FORMULATED,
                'patent_potential': 5,
                'market_size_b': 2,
                'development_cost_k': 200,
                'time_to_market_years': 5
            }
        }
    
    def get_trl_description(self, trl: int) -> str:
        """Get description for TRL level."""
        descriptions = {
            1: "Basic principles observed and reported",
            2: "Technology concept and/or application formulated",
            3: "Analytical and experimental critical function proof of concept",
            4: "Component and/or breadboard validation in laboratory",
            5: "Component and/or breadboard validation in relevant environment",
            6: "System/subsystem model or prototype demonstration",
            7: "System prototype demonstration in operational environment",
            8: "Actual system completed and qualified",
            9: "Actual system proven in operational environment"
        }
        return descriptions.get(trl, "Unknown")
    
    def calculate_patent_cost(self, num_patents: int = 1, international: bool = False) -> Dict:
        """
        Calculate patent filing costs.
        
        Args:
            num_patents: Number of patents to file
            international: Include international filings (PCT)
            
        Returns:
            Cost breakdown
        """
        # Cost estimates in USD
        provisional_cost = 5000  # Per patent
        utility_cost = 15000  # Per patent
        pct_cost = 30000  # International filing
        
        costs = {
            'provisional': provisional_cost * num_patents,
            'utility': utility_cost * num_patents,
            'total_domestic': (provisional_cost + utility_cost) * num_patents
        }
        
        if international:
            costs['international'] = pct_cost * num_patents
            costs['total'] = costs['total_domestic'] + costs['international']
        else:
            costs['total'] = costs['total_domestic']
        
        return costs
    
    def calculate_roi(
        self,
        development_cost: float,
        market_size: float,
        market_share: float = 0.01,
        profit_margin: float = 0.20
    ) -> Dict:
        """
        Calculate potential ROI.
        
        Args:
            development_cost: Total development cost
            market_size: Total addressable market
            market_share: Expected market share (default 1%)
            profit_margin: Profit margin (default 20%)
            
        Returns:
            ROI analysis
        """
        revenue = market_size * market_share
        profit = revenue * profit_margin
        roi = ((profit - development_cost) / development_cost) * 100
        
        return {
            'development_cost': development_cost,
            'market_size': market_size,
            'market_share_percent': market_share * 100,
            'expected_revenue': revenue,
            'expected_profit': profit,
            'roi_percent': roi,
            'breakeven_years': development_cost / profit if profit > 0 else float('inf')
        }
    
    def generate_innovation_report(self, innovation_key: str) -> Dict:
        """Generate comprehensive report for an innovation."""
        if innovation_key not in self.innovations:
            return {'error': f'Innovation {innovation_key} not found'}
        
        innovation = self.innovations[innovation_key]
        
        report = {
            'name': innovation['name'],
            'trl': {
                'level': innovation['trl'],
                'description': self.get_trl_description(innovation['trl'])
            },
            'patent_potential': {
                'score': innovation['patent_potential'],
                'rating': f"{innovation['patent_potential']}/10"
            },
            'market': {
                'size_billion': innovation['market_size_b'],
                'time_to_market_years': innovation['time_to_market_years']
            },
            'costs': {
                'development_k': innovation['development_cost_k'],
                'patent_filing': self.calculate_patent_cost(1, False)
            }
        }
        
        # Calculate ROI
        roi = self.calculate_roi(
            development_cost=innovation['development_cost_k'] * 1000,
            market_size=innovation['market_size_b'] * 1e9
        )
        report['roi'] = roi
        
        return report


def print_innovation_report(report: Dict):
    """Print formatted innovation report."""
    print("\n" + "=" * 70)
    print(f"  INNOVATION REPORT: {report['name']}")
    print("=" * 70)
    
    print(f"\n📊 Technology Readiness Level (TRL)")
    print(f"   Level: {report['trl']['level']}")
    print(f"   Status: {report['trl']['description']}")
    
    print(f"\n💡 Patent Potential")
    print(f"   Score: {report['patent_potential']['rating']}")
    
    print(f"\n💰 Market Analysis")
    print(f"   Total Market Size: ${report['market']['size_billion']:.1f}B")
    print(f"   Time to Market: {report['market']['time_to_market_years']} years")
    
    print(f"\n💵 Cost Analysis")
    print(f"   Development Cost: ${report['costs']['development_k']}K")
    print(f"   Patent Filing Cost: ${report['costs']['patent_filing']['total']:,}")
    
    print(f"\n📈 ROI Projection")
    print(f"   Expected Revenue (1% market): ${report['roi']['expected_revenue']/1e6:.1f}M")
    print(f"   Expected Profit (20% margin): ${report['roi']['expected_profit']/1e6:.1f}M")
    print(f"   ROI: {report['roi']['roi_percent']:.1f}%")
    print(f"   Breakeven: {report['roi']['breakeven_years']:.1f} years")
    
    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description='COSMOS Business Metrics Calculator',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--innovation', '-i',
        choices=['atomic-ex-light', 'galaxy-analysis', 'zipraf', 'rafcode-phi', 'all'],
        default='all',
        help='Innovation to analyze'
    )
    
    parser.add_argument(
        '--metric', '-m',
        choices=['trl', 'patent', 'roi', 'all'],
        default='all',
        help='Specific metric to calculate'
    )
    
    args = parser.parse_args()
    
    calculator = MetricsCalculator()
    
    print("\n🌌 COSMOS Business Metrics Calculator")
    print("   Rafael Melo Reis - RAFAELIA Project")
    
    if args.innovation == 'all':
        innovations = list(calculator.innovations.keys())
    else:
        innovations = [args.innovation]
    
    for innovation_key in innovations:
        report = calculator.generate_innovation_report(innovation_key)
        print_innovation_report(report)
    
    print()


if __name__ == '__main__':
    main()
