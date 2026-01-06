#!/usr/bin/env python3
"""
COSMOS - Pattern Recognition Tool
Detects and analyzes patterns in data, particularly spiral and Fibonacci patterns
"""

import argparse
import json
import math
from typing import List, Tuple, Dict


class PatternRecognizer:
    """Pattern recognition for COSMOS framework."""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.patterns_found = []
    
    def log(self, message: str):
        if self.verbose:
            print(f"[DEBUG] {message}")
    
    def detect_fibonacci_sequence(self, sequence: List[float], tolerance: float = 0.1) -> bool:
        """
        Detect if a sequence follows Fibonacci pattern.
        
        Args:
            sequence: List of numbers to analyze
            tolerance: Acceptable deviation from golden ratio
            
        Returns:
            True if Fibonacci pattern detected
        """
        if len(sequence) < 3:
            return False
        
        golden_ratio = 1.618033988749895
        ratios = []
        
        for i in range(2, len(sequence)):
            if sequence[i-1] != 0:
                ratio = sequence[i] / sequence[i-1]
                ratios.append(ratio)
        
        # Check if ratios converge to golden ratio
        if ratios:
            avg_ratio = sum(ratios) / len(ratios)
            deviation = abs(avg_ratio - golden_ratio)
            
            self.log(f"Average ratio: {avg_ratio:.4f}, Deviation: {deviation:.4f}")
            
            if deviation <= tolerance:
                self.patterns_found.append({
                    'type': 'fibonacci',
                    'confidence': 1 - (deviation / golden_ratio),
                    'avg_ratio': avg_ratio
                })
                return True
        
        return False
    
    def detect_spiral_pattern(self, points: List[Tuple[float, float]]) -> Dict:
        """
        Detect spiral patterns in 2D points.
        
        Args:
            points: List of (x, y) coordinates
            
        Returns:
            Dictionary with spiral analysis
        """
        if len(points) < 4:
            return {'detected': False}
        
        # Convert to polar coordinates
        angles = []
        radii = []
        
        for x, y in points:
            r = math.sqrt(x**2 + y**2)
            theta = math.atan2(y, x)
            angles.append(theta)
            radii.append(r)
        
        # Check if radii grow logarithmically (characteristic of logarithmic spiral)
        if len(radii) >= 3:
            # Check growth rate
            growth_rates = []
            for i in range(1, len(radii)):
                if radii[i-1] > 0:
                    growth = radii[i] / radii[i-1]
                    growth_rates.append(growth)
            
            if growth_rates:
                avg_growth = sum(growth_rates) / len(growth_rates)
                golden_ratio = 1.618033988749895
                
                # Check if growth rate is close to golden ratio
                if abs(avg_growth - golden_ratio) < 0.2:
                    result = {
                        'detected': True,
                        'type': 'logarithmic_spiral',
                        'growth_rate': avg_growth,
                        'fibonacci_correlation': abs(avg_growth - golden_ratio) < 0.1
                    }
                    self.patterns_found.append(result)
                    return result
        
        return {'detected': False}
    
    def analyze_data(self, data: List[float]) -> Dict:
        """
        Comprehensive pattern analysis.
        
        Args:
            data: Data to analyze
            
        Returns:
            Analysis results
        """
        results = {
            'data_points': len(data),
            'fibonacci_detected': False,
            'patterns': []
        }
        
        # Test for Fibonacci sequence
        if self.detect_fibonacci_sequence(data):
            results['fibonacci_detected'] = True
            results['patterns'].append('fibonacci_sequence')
        
        # Test for golden ratio in consecutive values
        golden_ratio = 1.618033988749895
        for i in range(1, len(data)):
            if data[i-1] != 0:
                ratio = data[i] / data[i-1]
                if abs(ratio - golden_ratio) < 0.05:
                    if 'golden_ratio_pairs' not in results:
                        results['golden_ratio_pairs'] = []
                    results['golden_ratio_pairs'].append({
                        'index': i,
                        'ratio': ratio,
                        'values': (data[i-1], data[i])
                    })
        
        results['patterns_found'] = self.patterns_found
        return results


def main():
    parser = argparse.ArgumentParser(
        description='COSMOS Pattern Recognition Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Input data (comma-separated values or JSON file)'
    )
    
    parser.add_argument(
        '--pattern', '-p',
        choices=['fibonacci', 'spiral', 'auto'],
        default='auto',
        help='Pattern type to detect (default: auto)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Initialize recognizer
    recognizer = PatternRecognizer(verbose=args.verbose)
    
    # Parse input
    try:
        # Try to parse as comma-separated values
        data = [float(x.strip()) for x in args.input.split(',')]
    except:
        # Try to read as file
        try:
            with open(args.input, 'r') as f:
                data = json.load(f)
        except:
            print(f"Error: Could not parse input: {args.input}")
            return 1
    
    print("\n🔍 COSMOS Pattern Recognition")
    print("=" * 60)
    print(f"Data points: {len(data)}")
    print(f"Pattern type: {args.pattern}")
    print()
    
    # Analyze
    results = recognizer.analyze_data(data)
    
    print("Results:")
    print(f"  Fibonacci detected: {results['fibonacci_detected']}")
    print(f"  Patterns found: {len(results.get('patterns_found', []))}")
    
    if results.get('golden_ratio_pairs'):
        print(f"\n  Golden Ratio pairs found: {len(results['golden_ratio_pairs'])}")
        for pair in results['golden_ratio_pairs'][:5]:  # Show first 5
            print(f"    Index {pair['index']}: {pair['values'][0]:.2f} → {pair['values'][1]:.2f} (ratio: {pair['ratio']:.4f})")
    
    print("\n✓ Analysis complete")
    print()


if __name__ == '__main__':
    main()
