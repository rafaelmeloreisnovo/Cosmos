#!/usr/bin/env python3
"""Validate exact invariants declared by the Cânone do Cosmos RAFAELIA.

This validator checks only [E] exact/combinatorial statements. It does not
promote conventions, hypotheses or parables to physical claims.
"""

from __future__ import annotations

import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/canonicos/01_CANONE_DO_COSMOS_RAFAELIA.manifest.json"

BITRAF64 = "AΔBΩΔTTΦIIBΩΔΣΣRΩRΔΔBΦΦFΔTTRRFΔBΩΣΣAFΦARΣFΦIΔRΦIFBRΦΩFIΦΩΩFΣFAΦΔ"


def distinct_permutations(text: str) -> int:
    result = math.factorial(len(text))
    for count in Counter(text).values():
        result //= math.factorial(count)
    return result


def entropy(text: str) -> float:
    counts = Counter(text)
    total = len(text)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


def choose2(value: int) -> int:
    return value * (value - 1) // 2


def to_base7(value: int) -> str:
    if value == 0:
        return "0"
    digits: list[str] = []
    while value:
        value, digit = divmod(value, 7)
        digits.append(str(digit))
    return "".join(reversed(digits))


def require(condition: bool, label: str, failures: list[str]) -> None:
    if not condition:
        failures.append(label)


def main() -> int:
    data: dict[str, Any] = json.loads(MANIFEST.read_text(encoding="utf-8"))
    exact = data["exact_invariants"]
    failures: list[str] = []

    # Character-chain universes.
    for text, expected in exact["string_permutations"].items():
        require(distinct_permutations(text) == expected, f"permutations:{text}", failures)

    # Matrix/tensor combinatorics.
    matrix = exact["matrices"]
    a_rows, a_cols = matrix["A_shape"]
    b_rows, b_cols = matrix["B_shape"]
    a_states = a_rows * a_cols
    b_states = b_rows * b_cols

    require(a_states == matrix["A_states"], "A_states", failures)
    require(b_states == matrix["B_states"], "B_states", failures)
    require(choose2(a_states) == matrix["A_internal_pairs"], "A_internal_pairs", failures)
    require(choose2(b_states) == matrix["B_internal_pairs"], "B_internal_pairs", failures)
    require(a_states * b_states == matrix["cross_relations"], "cross_relations", failures)
    require(
        choose2(a_states) * choose2(b_states) == matrix["pair_of_pairs"],
        "pair_of_pairs",
        failures,
    )
    require((a_rows - 1) * (a_cols - 1) * math.factorial(4) == matrix["A_adjacent_2x2_permutations"], "A_adjacent", failures)
    require((b_rows - 1) * (b_cols - 1) * math.factorial(4) == matrix["B_adjacent_2x2_permutations"], "B_adjacent", failures)
    require(math.comb(a_rows, 2) * math.comb(a_cols, 2) * math.factorial(4) == matrix["A_general_2x2_permutations"], "A_general", failures)
    require(math.comb(b_rows, 2) * math.comb(b_cols, 2) * math.factorial(4) == matrix["B_general_2x2_permutations"], "B_general", failures)

    # 7D x 6 operators = 42 hyperforms.
    hyper = exact["hyperforms"]
    require(hyper["dimensions"] * hyper["operators_per_dimension"] == hyper["total"], "hyperforms_42", failures)

    # Base-seven representations.
    cycle = exact["cycle_70x7"]
    require(70 * 7 == cycle["total"], "cycle_total", failures)
    require(to_base7(cycle["half_axis_70_decimal"]) == cycle["half_axis_70_base7"], "half_axis_base7", failures)
    require(to_base7(cycle["half_total_decimal"]) == cycle["half_total_base7"], "half_total_base7", failures)

    # BITRAF64 exact count, frequencies and first-order entropy.
    bitraf = exact["bitraf64"]
    alphabet = bitraf["alphabet_order"]
    observed = Counter(BITRAF64)
    frequencies = [observed[symbol] for symbol in alphabet]
    require(len(BITRAF64) == bitraf["length"], "bitraf_length", failures)
    require(frequencies == bitraf["frequencies"], "bitraf_frequencies", failures)
    require(abs(entropy(BITRAF64) - bitraf["entropy_bits_per_symbol_approx"]) < 0.0001, "bitraf_entropy", failures)

    # Geometry constants must remain separate.
    lambda_h = math.sqrt(3.0) / 2.0
    lambda_a = math.sqrt(3.0 / 2.0)
    require(0.0 < lambda_h < 1.0, "lambda_h_contracts", failures)
    require(lambda_a > 1.0, "lambda_a_expands", failures)

    result = {
        "schema": "rafaelia.cosmos.canon.validation.v1",
        "manifest": str(MANIFEST.relative_to(ROOT)),
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "checked": {
            "permutation_universes": 3,
            "matrix_invariants": 10,
            "hyperforms": 42,
            "bitraf64_length": len(BITRAF64),
            "bitraf64_entropy": round(entropy(BITRAF64), 6),
            "lambda_h": round(lambda_h, 9),
            "lambda_a": round(lambda_a, 9),
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
