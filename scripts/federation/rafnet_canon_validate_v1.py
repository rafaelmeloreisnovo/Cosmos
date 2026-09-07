#!/usr/bin/env python3
"""Bounded RafNet consumer for the exact COSMOS canon validator.

Capability: cosmos.canon.validate
Payload: the literal UTF-8 string CANON_EXACT_V1

This adapter validates only the exact/combinatorial [E] canon already enforced by
scripts/formal/validate-cosmos-canon.py. It does not validate physical,
cosmological, legal, academic, market, or patent claims.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CAPABILITY = "cosmos.canon.validate"
PAYLOAD_LITERAL = "CANON_EXACT_V1"
VALIDATOR = ROOT / "scripts/formal/validate-cosmos-canon.py"
EXPECTED_VALIDATOR_GIT_BLOB_SHA1 = "be1713d517af16dbc9ca204fa2c0e6a71e054314"
EXPECTED_BASE_COMMIT = "de1c5a88913f5d6ee6e90b7b09750923c91cb4df"
RESULT_SCHEMA = "rafaelia.cosmos.rafnet-canon-result.v1"
MAX_PAYLOAD_BYTES = 64


class CapabilityError(RuntimeError):
    pass


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_payload(path: Path) -> str:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise CapabilityError("payload unreadable") from exc
    if not raw or len(raw) > MAX_PAYLOAD_BYTES:
        raise CapabilityError("payload outside bounded size")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CapabilityError("payload must be UTF-8") from exc
    if text != PAYLOAD_LITERAL:
        raise CapabilityError("payload literal mismatch")
    return text


def verify_validator_binding(path: Path = VALIDATOR) -> str:
    if not path.is_file():
        raise CapabilityError("canon validator missing")
    observed = git_blob_sha1(path)
    if observed != EXPECTED_VALIDATOR_GIT_BLOB_SHA1:
        raise CapabilityError("canon validator binding drift")
    return observed


def run_validator(path: Path = VALIDATOR) -> tuple[dict[str, Any], str]:
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        reason = result.stderr.strip().replace("\n", " ")[:512]
        raise CapabilityError(f"canon validator failed: {reason}")
    try:
        doc = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise CapabilityError("canon validator output is not JSON") from exc
    if doc.get("schema") != "rafaelia.cosmos.canon.validation.v1":
        raise CapabilityError("canon validator result schema mismatch")
    if doc.get("status") != "PASS" or doc.get("failures") != []:
        raise CapabilityError("canon exact invariants did not pass")
    return doc, sha256_bytes(result.stdout.encode("utf-8"))


def execute(payload_path: Path, env: dict[str, str] | None = None) -> dict[str, Any]:
    environment = os.environ if env is None else env
    if environment.get("RAFNET_TARGET_CAPABILITY", "").strip() != CAPABILITY:
        raise CapabilityError("target capability confirmation missing or mismatched")

    message_id = environment.get("RAFNET_MESSAGE_ID", "").strip()
    source_commit = environment.get("RAFNET_SOURCE_COMMIT", "").strip()
    if not message_id:
        raise CapabilityError("RAFNET_MESSAGE_ID required")
    if len(source_commit) != 40 or any(ch not in "0123456789abcdef" for ch in source_commit):
        raise CapabilityError("RAFNET_SOURCE_COMMIT must be a lowercase 40-hex commit")

    load_payload(payload_path)
    validator_blob = verify_validator_binding()
    validator_result, output_sha256 = run_validator()

    return {
        "schema": RESULT_SCHEMA,
        "capability": CAPABILITY,
        "message_id": message_id,
        "source_commit": source_commit,
        "consumer_repository": "rafaelmeloreisnovo/Cosmos",
        "consumer_base_commit": EXPECTED_BASE_COMMIT,
        "validator_path": "scripts/formal/validate-cosmos-canon.py",
        "validator_git_blob_sha1": validator_blob,
        "validator_result_schema": validator_result["schema"],
        "validator_status": validator_result["status"],
        "validator_output_sha256": output_sha256,
        "evidence_scope": "EXACT_CANONICAL_COMBINATORIAL_INVARIANTS_ONLY",
        "hypotheses_validated": False,
        "physical_claims_proven": False,
        "scientific_generalization_allowed": False,
        "claim_allowed": False,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {Path(argv[0]).name} PAYLOAD_FILE", file=sys.stderr)
        return 2
    try:
        result = execute(Path(argv[1]).resolve())
    except CapabilityError as exc:
        print(f"COSMOS_RAFNET_CAPABILITY=BLOCKED reason={exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
