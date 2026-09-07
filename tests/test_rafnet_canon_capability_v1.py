from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "scripts/federation/rafnet_canon_validate_v1.py"

spec = importlib.util.spec_from_file_location("rafnet_canon_validate_v1", ADAPTER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class RafNetCanonCapabilityV1Test(unittest.TestCase):
    def _payload(self, root: Path, text: str = module.PAYLOAD_LITERAL) -> Path:
        path = root / "payload.txt"
        path.write_text(text, encoding="utf-8")
        return path

    def _env(self) -> dict[str, str]:
        return {
            "RAFNET_TARGET_CAPABILITY": module.CAPABILITY,
            "RAFNET_MESSAGE_ID": "RFN-COSMOS-SYNTH-0001",
            "RAFNET_SOURCE_COMMIT": "f8744ccf161908d22a7f13c6693e2ce745e0ac49",
        }

    def test_bound_validator_blob_matches_repository_source(self):
        self.assertEqual(
            module.verify_validator_binding(),
            module.EXPECTED_VALIDATOR_GIT_BLOB_SHA1,
        )

    def test_exact_canon_validator_runs_and_remains_bounded(self):
        result, output_hash = module.run_validator()
        self.assertEqual(result["schema"], "rafaelia.cosmos.canon.validation.v1")
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["failures"], [])
        self.assertEqual(len(output_hash), 64)

    def test_wrong_payload_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            payload = self._payload(Path(td), "RUN_ANYTHING")
            with self.assertRaises(module.CapabilityError):
                module.execute(payload, self._env())

    def test_wrong_capability_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            payload = self._payload(Path(td))
            env = self._env()
            env["RAFNET_TARGET_CAPABILITY"] = "cosmos.claim.validate"
            with self.assertRaises(module.CapabilityError):
                module.execute(payload, env)

    def test_missing_message_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            payload = self._payload(Path(td))
            env = self._env()
            env["RAFNET_MESSAGE_ID"] = ""
            with self.assertRaises(module.CapabilityError):
                module.execute(payload, env)

    def test_invalid_source_commit_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            payload = self._payload(Path(td))
            env = self._env()
            env["RAFNET_SOURCE_COMMIT"] = "TOKEN_VAZIO"
            with self.assertRaises(module.CapabilityError):
                module.execute(payload, env)

    def test_success_result_never_promotes_scientific_or_physical_claim(self):
        with tempfile.TemporaryDirectory() as td:
            payload = self._payload(Path(td))
            result = module.execute(payload, self._env())
            self.assertEqual(result["schema"], module.RESULT_SCHEMA)
            self.assertEqual(result["capability"], module.CAPABILITY)
            self.assertEqual(result["validator_status"], "PASS")
            self.assertEqual(
                result["evidence_scope"],
                "EXACT_CANONICAL_COMBINATORIAL_INVARIANTS_ONLY",
            )
            self.assertFalse(result["hypotheses_validated"])
            self.assertFalse(result["physical_claims_proven"])
            self.assertFalse(result["scientific_generalization_allowed"])
            self.assertFalse(result["claim_allowed"])

    def test_result_is_json_serializable(self):
        with tempfile.TemporaryDirectory() as td:
            payload = self._payload(Path(td))
            result = module.execute(payload, self._env())
            json.dumps(result, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    unittest.main()
