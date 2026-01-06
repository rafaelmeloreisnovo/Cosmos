#!/usr/bin/env python3
"""
COSMOS - Modified Fibonacci Sequence Calculator
Based on Rafael Melo Reis' modified Fibonacci concept

This script calculates the modified Fibonacci sequence as described in the COSMOS framework.
"""

import sys
import argparse
from typing import List


def modified_fibonacci(n: int, modifier: float = 1.618033988749895) -> List[float]:
    """
    Calculate modified Fibonacci sequence.
    
    Args:
        n: Number of terms to generate
        modifier: Golden ratio modifier (default: φ = 1.618...)
    
    Returns:
        List of modified Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        # Modified Fibonacci: includes golden ratio influence
        next_val = sequence[i-1] + sequence[i-2] * modifier
        sequence.append(next_val)
    
    return sequence


def standard_fibonacci(n: int) -> List[int]:
    """Calculate standard Fibonacci sequence for comparison."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence


def print_comparison(n: int):
    """Print comparison between standard and modified Fibonacci."""
    standard = standard_fibonacci(n)
    modified = modified_fibonacci(n)
    
    print(f"\n{'Index':<6} {'Standard':<15} {'Modified':<20} {'Ratio':<15}")
    print("-" * 60)
    
    for i, (std, mod) in enumerate(zip(standard, modified)):
        if std != 0:
            ratio = mod / std
            print(f"{i:<6} {std:<15} {mod:<20.6f} {ratio:<15.6f}")
        else:
            print(f"{i:<6} {std:<15} {mod:<20.6f} {'N/A':<15}")


def main():
    parser = argparse.ArgumentParser(
        description='COSMOS Modified Fibonacci Calculator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --sequence 10
  %(prog)s --sequence 15 --compare
  %(prog)s --sequence 20 --modifier 1.5
        """
    )
    
    parser.add_argument(
        '--sequence', '-n',
        type=int,
        default=10,
        help='Number of terms to generate (default: 10)'
    )
    
    parser.add_argument(
        '--modifier', '-m',
        type=float,
        default=1.618033988749895,
        help='Golden ratio modifier (default: φ = 1.618...)'
    )
    
    parser.add_argument(
        '--compare', '-c',
        action='store_true',
        help='Compare with standard Fibonacci sequence'
    )
    
    args = parser.parse_args()
    
    print(f"\n🌀 COSMOS Modified Fibonacci Calculator")
    print(f"   Rafael Melo Reis - RAFAELIA Project")
    print(f"   Modifier (φ): {args.modifier}")
    print(f"   Terms: {args.sequence}\n")
    
    if args.compare:
        print_comparison(args.sequence)
    else:
        sequence = modified_fibonacci(args.sequence, args.modifier)
        print("Modified Fibonacci Sequence:")
        for i, val in enumerate(sequence):
            print(f"  F({i}) = {val:.6f}")
    
    print()


if __name__ == '__main__':
    main()
